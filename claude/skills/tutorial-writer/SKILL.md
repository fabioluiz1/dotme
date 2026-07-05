---
name: tutorial-writer
description: >
  Write a didactic, hands-on tutorial post for the garden (fabioluiz.dev) in Fabio's teaching
  voice. Use when a draft teaches how a tool or technique works to a reader who was not there:
  reproducible commands, generalizable knowledge, the value is the knowledge itself. This is the
  voice of the "Claude Code vs Pi", "Running a coding model locally with Ollama", and "Ralph loop"
  posts. Usually dispatched by journal-router; can be invoked directly. NOT for first-person
  experience or reflection pieces, that is journal-writer.
---

# tutorial-writer

Turn a session draft into a polished tutorial: the reader can reproduce every step and walk away
knowing how the thing works. Reader-centric, not author-centric. The post teaches; it does not
recount your day.

## When this voice, not journal-writer

Reach for this skill when the draft is a **how-it-works**:

- the value is a reusable technique or a mental model, not the author's experience
- every claim can be shown with a command and its real output
- a stranger could follow it and get the same result
- the natural title is "How X works" or "X, explained by doing it"

If the draft is instead about what happened to you, a decision you made, or a struggle you had, that
is [journal-writer], not this.

## The didactic method (the core)

This is the whole reason the tutorial voice exists. Every section is built the same way:

- **Progressive disclosure.** One idea at a time, each building on the last. Never forward-reference
  a term you have not defined yet.
- **Define every term on first use.** Bold it, then define it inline, in the same sentence:
  "The **harness** is everything wrapped around the language model to turn it into an agent." No
  bold term is left undefined.
- **Example before theory.** Show the command and its real output first, then explain what it means.
  The reader sees the thing behave, then learns why.
- **Theory through the example.** Do not lecture in the abstract. Anchor every concept to the
  concrete artifact on screen: this line of output, this file, this token count.

## The repeating section pattern

Most sections follow this micro-structure. Use it as the default shape, not a rigid rule:

1. **Concept** — one sentence naming the idea, with its term defined.
2. **Hands-on** — the command a user types, then its real captured output.
3. **Mental model** — the one-line analogy or framing that makes it stick.
4. **Tradeoff** — what you gain and what you give up, as a short bullet pair.

## Structure of the post

- **Intro (2-4 sentences).** State the single idea the whole post turns on. Deliver on the title's
  promise immediately. No throat-clearing.
- **Claim-heading spine.** Section headings are assertions, not labels: "The gate is the hard half",
  "The one idea that explains everything". Never the generic `## The Problem` / `## What I Learned`.
- **Body.** Each section teaches one facet with the pattern above.
- **## Key takeaways.** Bullet the conceptual conclusions, the ones defensible without re-running
  anything.
- **## Try it yourself.** A numbered path the reader can walk end to end.
- **## References.** Primary sources, verified links.

## Visual-first

The reader (and the author) read visually. Any enumeration of 2+ items becomes a real structure:

- **Mermaid** for flow, state, and architecture.
- **ASCII** for file trees and layouts.
- **Tables** for side-by-side comparisons.
- Break embedded lists out of prose into real bullets.

## Editorial guardrails (self-contained, do not rely on outside memory)

- **No em-dashes** (`—` or `--`). Use a comma, colon, semicolon, period, or a connective ("and",
  "but", "so", "because").
- **Never self-justify in the prose.** The text states things; it does not defend its own
  construction. No "I dropped X to keep it sharp", no headings that argue for the post's own
  structure.
- **No self-promotion.** Do not name the author's own projects (harnx, a review gate, aleksander,
  etc.) as a "transfer note." A post about topic X stays about X. Teach the transferable idea
  without the "my thing that I built" framing.
- **Show how a user drives the tool, not its internals.** Lead every example with the plain-English
  ask or the command a user types, plus real output. Do not quote a tool's source code to make a
  point.
- **Examples must be real.** Run them, capture actual output (real ids, real logs). Verify quotes
  verbatim against the source. When a run has not happened yet, mark the spot with a
  `<!-- pilot: ... -->` comment and keep `draft: true`; never invent output.
- **Never promise future posts.** Naming an open question is fine; committing to answer it later is
  not.

## Frontmatter, wikilinks, tags

```yaml
---
title: "Sentence-case, LinkedIn-attractive, no clickbait"
date: YYYY-MM-DD
tags:
  - primary-topic
  - deep-dive
draft: true
---
```

- **Title:** sentence case, promises value by outcome or a bold-but-true claim. Good: "Claude Code
  ships the batteries, Pi hands you the wires." Avoid generic "How to use X" and Title Case.
- **Wikilinks:** link technical terms and tools on first mention (`[[Pi]]`, `[[Ollama]]`).
- **Tags:** lowercase, hyphenated; `deep-dive` for long explorations.
- Keep `draft: true` until every `<!-- pilot -->` is resolved with real output.
