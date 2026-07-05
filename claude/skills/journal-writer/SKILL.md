---
name: journal-writer
description: >
  Write a first-person reflective journal post for the garden (fabioluiz.dev) in Fabio's personal
  voice, the "confessions / how was my experience" style: what I set out to do, what actually
  happened, what surprised or confused me, and what I now believe. Use when a draft is about the
  author's own experience, decision, or struggle rather than a reusable how-to. Usually dispatched
  by journal-router; can be invoked directly. NOT for teach-a-tool tutorials, that is
  tutorial-writer.
---

# journal-writer

Turn a session draft into a first-person entry that recounts an experience and what it taught the
author. Author-centric. The post reflects; it is not a manual.

## When this voice, not tutorial-writer

Reach for this skill when the draft is a **lived experience**:

- the value is the reflection, the opinion, or the decision, not a reproducible procedure
- it carries a feeling: what confused me, what I got wrong first, what surprised me, what I now think
- the natural title is "What X taught me" or "Why I switched to Y", not "How X works"

If the draft is instead a generalizable how-it-works a stranger could reproduce, that is
[tutorial-writer], not this.

## Voice

- **First person, honest.** "I set out to...", "I assumed X and was wrong", "the part that bit me
  was...". The struggle is the content here, not a weakness to hide.
- **Show the failure first.** What you tried that did not work, and why, is often the most useful
  paragraph. This is the one place "what failed first" belongs; keep it out of tutorials.
- **Conversational but technical.** Explain plainly without dumbing down. Real code and real
  commands still earn their place; a reflection with no artifact is a diary, not a journal.
- **Land on a belief.** End where the experience left you: a changed mind, a new rule of thumb, a
  question you now hold. Not a summary, a conviction.

## The arc (a shape, not a skeleton)

Do not force `## The Problem` / `## What I Learned` headings. Let the entry follow the experience:

1. **The setup.** What I was trying to do and why it mattered to me.
2. **What actually happened.** The turns, the wrong first guess, the moment it clicked. This is the
   body, and it can be several claim-headed sections.
3. **What I now believe.** The takeaway as a conviction I carry forward.

Use claim-headings ("The wrong mental model I started with"), never generic labels.

## Editorial guardrails (self-contained)

- **No em-dashes** (`—` or `--`). Comma, colon, semicolon, period, or a connective instead.
- **Reflecting on my own building is the point; plugging products is not.** Writing about a thing I
  made and what it taught me is fair game in this voice. Turning the post into a pitch for a
  commercial project is not. Keep the reflection, drop the sales.
- **No self-justification about the writing itself.** Confess the experience, not the editorial
  choices ("I dropped a section to keep it tight" is meta, cut it).
- **Never promise future posts.** Naming an open question is fine; committing to a follow-up is not.
- **Examples must be real.** Real commands, real output, real ids. Verify any quote verbatim.

## Frontmatter, wikilinks, tags

```yaml
---
title: "Sentence-case, LinkedIn-attractive, honest not clickbait"
date: YYYY-MM-DD
tags:
  - primary-topic
  - til
draft: true
---
```

- **Title:** sentence case, outcome or belief forward. Good: "Stacked PRs changed how I ship code."
  Avoid Title Case and generic how-tos.
- **Wikilinks:** link tools and concepts on first mention to build the graph.
- **Tags:** lowercase, hyphenated; `til` for a short "today I learned" reflection, topic tags
  otherwise.
- Keep `draft: true` for review before publish.

## Content checklist

1. **Extract the insight:** the one thing worth remembering from the experience.
2. **Keep an artifact:** at least one real command or code block that grounds the story.
3. **Link liberally:** technical terms become wikilinks.
4. **Keep it scannable:** claim-headings, bullets, code blocks.
5. **End on a conviction,** with wikilinks to related entries.
