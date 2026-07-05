# Generate Journal Entry

Generate a polished journal entry from the journal plan.

## Usage

```
/journal N
```

Where N is the entry number from the journal plan.

## Execution

**CRITICAL**: This command MUST run in a subagent with fresh context to avoid exhausting the main conversation's context window.

Use the Task tool with:
- `subagent_type`: "general-purpose"
- `prompt`: Include all instructions below plus the entry number N

## Subagent Instructions

The subagent should:

1. Read `~/garden/drafts/YYYYMMDD-journal-plan.md` (today's date)
2. Find Entry N in the plan
3. Read only the drafts listed for that entry
4. Load the journal-router skill from `~/.me/claude/skills/journal-router/SKILL.md`. It classifies
   the draft's voice (tutorial vs first-person reflection vs both) and loads the right writing
   skill: `tutorial-writer` and/or `journal-writer`. Do not hardcode a voice; let the router decide.
5. Synthesize those drafts into a focused journal entry (or two, if the router calls "both")
6. Follow the voice, style, structure, and guardrails from the chosen skill(s)
7. Add appropriate wikilinks to technical terms
8. Save to `~/garden/journal/YYYY-MM-DD-slug.md`
9. Set `draft: true` in frontmatter for review
10. Run `pre-commit run mdformat --files ~/garden/entries/YYYY-MM-DD-slug.md` to format the entry

## Output Location

Save the generated entry to: `~/garden/journal/YYYY-MM-DD-descriptive-slug.md`

The slug should be derived from the entry title (lowercase, hyphenated). For a "both" split, save
two files and cross-link them with wikilinks.

## After Generation

1. Show the entry path
2. Move entry N's draft files from `~/garden/drafts/gardening/` to `~/garden/drafts/archive/`
3. Return summary: entry title, path, and suggestion to run `/publish`
