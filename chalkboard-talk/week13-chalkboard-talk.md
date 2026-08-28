# Week 13 — Searching: Linear and Binary Search

> **Read this before you start the Week 13 homework.** The party's inventory has
> grown huge. This week you build **search** so heroes can find an item
> instantly — and race **linear** search against **binary** search to see which
> is faster.
>
> Homework packet: [week13-homework.md](../homework-packets/student/week13-homework.md)

## What you'll learn this week

- What a search algorithm does.
- How **linear search** checks items one by one.
- How **binary search** halves a *sorted* list each step.
- How to count the steps each search takes.
- When to choose one search over the other.

## 1. What "search" means

A **search algorithm** finds where a target value lives in a collection, or
reports that it is missing. By convention, our searches **return the index** of
the target, or **-1** if it is not found.

## 2. Linear search: check one at a time

**Linear search** walks the list from the front, comparing each item to the
target. It works on **any** list, sorted or not.

```python
def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i          # found it -> return the index
    return -1                 # never matched -> not found

print(linear_search(["map", "rope", "key"], "rope"))   # 1
```

In the worst case (the item is last or missing), linear search checks **every**
item. For a list of 100 items, that is up to 100 comparisons.

## 3. Binary search: halve the list each step

**Binary search** is much faster, but it requires a **sorted** list. It looks at
the middle item and, because the list is sorted, throws away half the list each
step:

```python
def binary_search(items, target):
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid              # found
        if items[mid] < target:
            lo = mid + 1            # target is in the upper half
        else:
            hi = mid - 1            # target is in the lower half
    return -1                       # not found

print(binary_search(["coin", "key", "map", "rope"], "map"))   # 2
```

How it works each loop:

1. Look at the middle item (`mid`).
2. If it matches, done.
3. If the target is larger, ignore the lower half (`lo = mid + 1`).
4. If the target is smaller, ignore the upper half (`hi = mid - 1`).

Because it discards half the remaining items each time, a list of 100 items takes
about **7** steps instead of 100.

## 4. Counting steps (efficiency)

To compare the two, count each comparison. Add a counter that increments once per
check:

```python
def linear_steps(items, target):
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            break
    return steps
```

Do the same inside binary search's loop. On a sorted list, binary search will use
noticeably fewer steps — that difference is what computer scientists call
**efficiency**. Linear search grows in step with the list size; binary search
grows much more slowly (roughly doubling the list adds just one step).

## 5. When to use which

| Situation                         | Best choice     | Why                              |
| --------------------------------- | --------------- | -------------------------------- |
| Small or **unsorted** list        | Linear search   | Simple; no sorting required      |
| Large **sorted** list             | Binary search   | Far fewer comparisons            |
| You only search once, data random | Linear search   | Sorting first may not be worth it|
| You search many times, sorted     | Binary search   | Pays off repeatedly              |

## Common mistakes to avoid

- **Binary search on an unsorted list:** it only works when the list is sorted —
  otherwise the "throw away half" logic is wrong.
- **Off-by-one in bounds:** `hi` starts at `len(items) - 1`, and the loop runs
  while `lo <= hi`.
- **Forgetting the not-found case:** return `-1` when the target is absent.
- **Counting steps in the wrong place:** increment the counter once per
  comparison, inside the loop.

## Official Python documentation

- `enumerate()` (used in linear search): <https://docs.python.org/3/library/functions.html#enumerate>
- The `bisect` module (Python's built-in binary search on sorted lists): <https://docs.python.org/3/library/bisect.html>
- Sorting HOW TO (context for "sorted data"): <https://docs.python.org/3/howto/sorting.html>
- `list` methods, including `.index()`: <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

## How this connects to your homework

- **Problem 1 (`week13_p1_linear_search.py`)** — return the index or `-1`.
- **Problem 2 (`week13_p2_binary_search.py`)** — binary search on a sorted list.
- **Problem 3 (`week13_p3_compare_steps.py`)** — count and compare the steps each
  search uses.
- **Problem 4 (`week13_p4_search_app.py`)** — ask the user for a target and print
  the found index or a not-found message.
- **Problem 5 (`week13_p5_analysis.txt`)** — explain when to use each search
  (note binary search's sorted-data requirement).

## Quick reference

```python
# Linear: works on any list, checks each item
for i, item in enumerate(items):
    if item == target:
        return i
return -1

# Binary: sorted list only, halves the range each step
lo, hi = 0, len(items) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if items[mid] == target: return mid
    if items[mid] < target:  lo = mid + 1
    else:                    hi = mid - 1
return -1
```
