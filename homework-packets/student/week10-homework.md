# Week 10 Homework Packet

> **Story so far:** Ada reviews Cave Quest and nods: "Good — now make it clean
> before we expand it." Real studios refactor before adding features, so you
> tidy the code the whole party will build on next.

**Quest branch:** Branch `quest/week10-refactor` off your Week 9 Cave Quest work.
When the quest is done, open a merge request titled
`Week 10 - Firstname Lastname - Refactor` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Refactor the intro module

**Setup:** Cave Quest is growing; move the intro logic into its own function.
Refactor Week 9 intro code into its own function.

### Example stdout

```text
=== Cave Quest ===
```

## Problem 2 - Refactor turn logic

**Setup:** Duplicated choice code is slowing the party down.
Move choice logic into `play_turn()` returning item found.

### Example stdout

```text
You found: rope
```

## Problem 3 - Refactor the ending system

**Setup:** Endings should depend on what the hero collected.
Move ending logic into `show_ending(inventory)`.

### Example stdout

```text
Ending: Explorer rank achieved.
```

## Problem 4 - Document with docstrings

**Setup:** The whole party will build on this code, so make it easy to read.
Add docstrings to all functions.

### Example output target

```text
"""Plays one turn and returns discovered item."""
```

## Problem 5 - Engineering change notes

**Setup:** Ada asks what improved after the refactor.
Write `week10_p5_refactor_notes.txt` with at least 5 improvements.

### Example output target

```text
Improvement 1: Removed duplicated choice code.
```

## Level up (optional)

- **Side-quest:** add a `main()` that calls `show_intro()`, `play_turn()`, and `show_ending()` in order.
- **Stuck?** refactor in small steps — move one block into a function, run the game, then move the next.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
