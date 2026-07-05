# List Pending Drafts

Show captured session drafts and suggest journal entries.

## Instructions

1. List draft captures from the month folders: `~/garden/drafts/YYYY-MM/DD_HHMMSS.md`
   (e.g. `find ~/garden/drafts -type f -path '*/[0-9][0-9][0-9][0-9]-[0-9][0-9]/*.md'`).
   Drafts are grouped by month; do NOT read `archive/`, `gardening/`, or the top-level
   `*-journal-plan.md` and working files.
2. Read each draft's frontmatter (project, date) and content
3. Group drafts by learning theme (not just project name)
4. Suggest journal entries with summaries
5. Save analysis to `~/garden/drafts/YYYYMMDD-journal-plan.md`
6. Move all analyzed draft files to `~/garden/drafts/gardening/`

## Output Format

### Section 1: Draft Count
Show total drafts and date range.

### Section 2: Suggested Journal Entries
For each suggested entry:

**Entry N: Suggested Title**
Summary: 1-2 sentence description of the learning/insight.
Based on drafts:
- filename.md (project)
- filename.md (project)

### Grouping Guidelines
- Group by learning theme, not project name
- Combine duplicate captures (same session_id)
- Separate work tasks from personal tooling
- Mark trivial sessions as "skippable"

## Save Plan

After analysis, save to `~/garden/drafts/YYYYMMDD-journal-plan.md`:

```markdown
---
date: YYYY-MM-DD
status: pending
---

# Journal Plan

## Entry 1: Title
Summary: description
Drafts:
- filename.md

## Entry 2: Title
...

## Skippable
- filename.md (reason)
```

## Actions

After reviewing:
- Run `/journal N` to generate entry N from the plan

## Context Management

**CRITICAL**: After completing this command, immediately run `/compact` to free context space. This command reads many files and exhausts context quickly.
