#!/usr/bin/env bash
# Capture Claude Code session data for journal generation
# Triggered by SessionEnd hook
#
# Reads hook JSON from stdin, extracts transcript path, and embeds
# the raw conversation content into a self-contained draft file.

set -euo pipefail

DRAFTS_DIR="$HOME/garden/drafts"
DATE=$(date +%Y-%m-%d)
MONTH=$(date +%Y-%m)          # drafts are grouped by month: drafts/YYYY-MM/
DAY_TIME=$(date +%d_%H%M%S)   # file within the month folder: DD_HHMMSS.md
MONTH_DIR="$DRAFTS_DIR/$MONTH"
DRAFT_FILE="$MONTH_DIR/${DAY_TIME}.md"

mkdir -p "$MONTH_DIR"

# Read hook metadata from stdin
HOOK_INPUT=$(cat)

# Extract transcript path from hook JSON
TRANSCRIPT_PATH=$(echo "$HOOK_INPUT" | jq -r '.transcript_path // empty')

if [[ -z "$TRANSCRIPT_PATH" || ! -f "$TRANSCRIPT_PATH" ]]; then
    echo "No transcript found, skipping capture" >&2
    exit 0
fi

# Extract session summary (first line of JSONL usually has it)
SUMMARY=$(jq -r 'select(.type == "summary") | .summary // empty' "$TRANSCRIPT_PATH" | head -1)

# Extract conversation: user questions and assistant responses
# Filter out meta messages, commands, and system content
CONVERSATION=$(jq -r '
    select(.type == "user" or .type == "assistant") |
    select(.message.content != null) |
    select(.isMeta != true) |
    # Handle user messages (strings) - skip command/system messages
    if .type == "user" then
        if (.message.content | type) == "string" and
           (.message.content | startswith("<command-") | not) and
           (.message.content | startswith("<local-command") | not) and
           (.message.content | startswith("Caveat:") | not) then
            "**Human**: " + .message.content
        else
            empty
        end
    # Handle assistant messages (usually arrays with text/thinking blocks)
    elif .type == "assistant" then
        (if (.message.content | type) == "array" then
            [.message.content[] | select(.type == "text") | .text] | join("\n")
        else
            .message.content
        end) as $text |
        if ($text | length) > 0 then
            "**Assistant**: " + $text
        else
            empty
        end
    else
        empty
    end
' "$TRANSCRIPT_PATH" 2>/dev/null)

# Only save if there's actual conversation content
if [[ -z "$CONVERSATION" ]]; then
    echo "No conversation content found, skipping capture" >&2
    exit 0
fi

cat > "$DRAFT_FILE" << EOF
---
captured: $(date -Iseconds)
project: ${PWD##*/}
session_id: $(echo "$HOOK_INPUT" | jq -r '.session_id // empty')
status: draft
---

# Session Capture - $DATE

${SUMMARY:+## Summary
$SUMMARY

}## Conversation

$CONVERSATION
EOF

echo "Captured session to $DRAFT_FILE" >&2
