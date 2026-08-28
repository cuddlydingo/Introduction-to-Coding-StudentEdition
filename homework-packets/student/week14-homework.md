# Week 14 Homework Packet

> **Story so far:** The Guild wants a BranchQuest leaderboard. You build sorting
> to rank scores — then combine it with last week's search to find any rank
> fast.

**Quest branch:** Work on a branch named `quest/week14-leaderboard`. When the
quest is done, open a merge request titled
`Week 14 - Firstname Lastname - Leaderboard` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Bubble sort engine

**Setup:** Sort quest times from slowest to fastest.
Create `week14_p1_bubble_sort.py`.

### Example stdout

```text
Before: [5, 2, 4]
After: [2, 4, 5]
```

## Problem 2 - Insertion sort practice

**Setup:** Keep the leaderboard ordered as new scores arrive.
Create `week14_p2_insertion_sort.py`.

### Example stdout

```text
Before: [9, 1, 6]
After: [1, 6, 9]
```

## Problem 3 - Leaderboard sorter

**Setup:** The Guild wants BranchQuest scores ranked each week.
Create `week14_p3_leaderboard.py` sorting scores ascending.

### Example stdout

```text
Scores before: [42, 17, 31]
Scores after: [17, 31, 42]
```

## Problem 4 - Sort, then search

**Setup:** Reuse your Week 13 binary search: sort the scores, then find a target.
Create `week14_p4_sort_then_search.py` and search in sorted output.

### Example stdout

```text
Sorted: [3, 8, 11, 14]
Target 11 found at index 2
```

## Problem 5 - Sorting tradeoffs reflection

**Setup:** Share what you learned about sorting tradeoffs with next semester's apprentices.
Create `week14_p5_reflection.txt` on sorting tradeoffs.

### Example output target

```text
Bubble sort is easy to understand but can be slow for large lists...
```

## Level up (optional)

- **Side-quest:** add a descending option (highest score first).
- **Stuck?** print the list after each pass to watch the largest value move to the end.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
