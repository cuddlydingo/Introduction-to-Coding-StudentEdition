# Week 8 Homework Packet

> **Story so far:** Disaster! The night before the first demo, the Glitch swarms
> BranchQuest and three scripts crash. Grace — the Guild's Chief Bug-Hunter, who
> gave the "bug" its name long ago — teaches you to hunt them down one traceback
> at a time.

**Quest branch:** Work on a branch named `quest/week08-bug-hunt`. When the quest
is done, open a merge request titled
`Week 08 - Firstname Lastname - Bug Hunt` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Bug hunt: the missing hero (NameError)

**Setup:** A teammate's script crashes before launch — a hero's name will not print.
Fix `week08_p1_name_error.py` (provided buggy file).
Buggy starter files are provided in `course-materials/week08-buggy-files/`.

### Example stdout

```text
Player: Alex
```

## Problem 2 - Bug hunt: broken score math (TypeError)

**Setup:** The score calculator treats numbers as text and refuses to add.
Fix `week08_p2_type_error.py` so numeric math works.
Use the provided buggy file from `course-materials/week08-buggy-files/`.

### Example stdout

```text
Total: 18
```

## Problem 3 - Bug hunt: inventory crash (IndexError)

**Setup:** The inventory display reaches for an item that is not there.
Fix `week08_p3_index_error.py` with safe list access.
Use the provided buggy file from `course-materials/week08-buggy-files/`.

### Example stdout

```text
No fourth item found.
```

## Problem 4 - Bug-hunter's report

**Setup:** Grace keeps an incident log for every Glitch attack.
Create `week08_p4_debug_log.txt` describing at least 3 fixes.

### Example output target

```text
Bug 1: NameError because variable name mismatch
Fix: changed playerName to player_name
```

## Problem 5 - Debrief with Grace

**Setup:** Grace asks every apprentice to reflect after a bug hunt.
Create `week08_p5_reflection.txt` (8-10 sentences).

### Example output target

```text
I learned to read the traceback from top to bottom...
```

## Level up (optional)

- **Side-quest:** wrap one risky line in `try`/`except` so the program prints a friendly message instead of crashing.
- **Stuck?** read the traceback from the bottom up; the last line names the error type and line number.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
