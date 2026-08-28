# Week 13 Homework Packet

> **Story so far:** The party's inventory has grown huge. You build search so
> heroes can find an item instantly — and race linear against binary search to
> see which is faster.

**Quest branch:** Work on a branch named `quest/week13-search`. When the quest is
done, open a merge request titled
`Week 13 - Firstname Lastname - Search` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Linear search tool

**Setup:** Search an unsorted backpack for an item.
Create `week13_p1_linear_search.py` returning index or -1.

### Example stdout

```text
linear_search(['map', 'rope', 'key'], 'rope') -> 1
```

## Problem 2 - Binary search tool

**Setup:** Search a sorted artifact vault quickly.
Create `week13_p2_binary_search.py` for sorted lists.

### Example stdout

```text
binary_search(['coin', 'key', 'map', 'rope'], 'map') -> 2
```

## Problem 3 - Search race

**Setup:** Race the two searches and count how many checks each one needs.
Create `week13_p3_compare_steps.py` counting steps used by each search.

### Example stdout

```text
Linear steps: 5
Binary steps: 3
```

## Problem 4 - Item finder app

**Setup:** Build a command-line finder for BranchQuest items.
Create `week13_p4_search_app.py` asking user target item.

### Example stdout

```text
Enter target: key
Found at index 2
```

## Problem 5 - Search strategy write-up

**Setup:** Grace asks when each search type should be used.
Create `week13_p5_analysis.txt` comparing when to use each search.

### Example output target

```text
Use linear search when data is small or unsorted...
```

## Level up (optional)

- **Side-quest:** make your item finder case-insensitive so "Key" and "key" both match.
- **Stuck?** binary search needs a sorted list; sort it first or it will miss items.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
