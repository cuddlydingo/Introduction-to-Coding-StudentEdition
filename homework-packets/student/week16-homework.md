# Week 16 Homework Packet

> **Story so far:** A neighboring guild speaks other "dialects" — Lua, C++, and
> Java. Ada sends you to learn how BranchQuest could be ported so you can read
> code in any language you meet.

**Quest branch:** Work on a branch named `quest/week16-dialects`. When the quest
is done, open a merge request titled
`Week 16 - Firstname Lastname - Dialects` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Dialect pattern finder

**Setup:** Compare how the same idea looks in two dialects.
Create `week16_p1_constructs.txt` listing variables/loops/functions in Python vs Java.
Use the provided examples in `course-materials/week16-cross-language-samples/`.

### Example output target

```text
Python variable: score = 10
Java variable: int score = 10;
```

## Problem 2 - Translate the logic

**Setup:** Show the party that logic transfers across syntax.
Create `week16_p2_translation.txt` showing pseudocode for a loop in both Python and C++ style.

### Example output target

```text
FOR i from 1 to 5
Python: for i in range(1, 6)
C++: for (int i = 1; i <= 5; i++)
```

## Problem 3 - Dialect difference chart

**Setup:** Build a quick-reference chart for makers learning a new dialect.
Create `week16_p3_differences.txt` with at least 5 syntax differences.

### Example output target

```text
Difference: Java uses braces {}, Python uses indentation.
```

## Problem 4 - Why concepts travel

**Setup:** Explain to a friend why learning one dialect helps with all the others.
Create `week16_p4_shared_concepts.txt` (8-10 sentences).

### Example output target

```text
Even though syntax differs, conditionals and loops solve the same decision/repetition problems...
```

## Problem 5 - Cross-dialect takeaway

**Setup:** Give Ada your final insights on reading other dialects.
Create `week16_p5_summary.txt` with 3 similarities, 3 differences, and 1 takeaway.

### Example output target

```text
Takeaway: Learn concepts first; syntax can be learned later.
```

## Bonus challenge (optional) - Public API explorer with Python requests

**Setup:** Ada offers a side-quest: pull live data into BranchQuest for dynamic
flavor — a creature codex, weather events, or character data.
Use starter files in `course-materials/week16-api-bonus/` and build one script that fetches live data.

Choose one API source from the curated list in `course-materials/week16-api-bonus/README.md`.

Create `week16_bonus_api_explorer.py` that:

1. Accepts one user input (for example Pokemon name, city, or character id).
2. Sends a `GET` request with `requests.get(..., timeout=10)`.
3. Handles status codes with at least `200` and one non-200 case.
4. Parses JSON and prints 3-5 useful fields.

### Example stdout target (PokeAPI)

```text
Pokemon name: ditto
Name: Ditto
ID: 132
Weight: 40
Primary Type: normal
```

## Level up (optional)

- **Side-quest:** add a third language (Lua) to one of your comparisons.
- **Stuck?** look for the same three parts in every language — a variable, a loop, and a function; the words change, the ideas do not.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
