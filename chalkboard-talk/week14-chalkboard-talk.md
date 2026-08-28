# Week 14 — Sorting: Bubble Sort and Insertion Sort

> **Read this before you start the Week 14 homework.** The Guild wants a
> BranchQuest leaderboard. This week you build **sorting** to rank scores — then
> combine it with last week's binary search to find any rank fast.
>
> Homework packet: [week14-homework.md](../homework-packets/student/week14-homework.md)

## What you'll learn this week

- What a sorting algorithm does.
- How **bubble sort** works.
- How **insertion sort** works.
- How to swap two values in Python.
- The tradeoffs between simple sorts and Python's built-in sort.

## 1. What "sort" means

A **sorting algorithm** arranges items in order — smallest to largest (ascending)
or largest to smallest (descending). Sorting powers leaderboards, and it is what
makes binary search (Week 13) possible.

### Swapping two values

Both sorts swap neighbors. Python swaps in one clean line, no temporary variable
needed:

```python
a, b = b, a         # swap the two values
arr[i], arr[i + 1] = arr[i + 1], arr[i]   # swap two list positions
```

## 2. Bubble sort

**Bubble sort** repeatedly compares neighboring pairs and swaps them if they are
out of order. Large values "bubble" to the end pass by pass.

```python
def bubble_sort(data):
    arr = data[:]                       # copy so the original is untouched
    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]   # swap
    return arr

print(bubble_sort([5, 2, 4]))           # [2, 4, 5]
```

Each outer pass locks the next-largest value into place at the end. It is easy to
understand, which is why it is taught first — but it is slow on large lists.

## 3. Insertion sort

**Insertion sort** builds the sorted list one item at a time, like sorting cards
in your hand: take the next card and slide it back until it sits in the right
spot.

```python
def insertion_sort(data):
    arr = data[:]
    for i in range(1, len(arr)):
        key = arr[i]                    # the card we are placing
        j = i - 1
        while j >= 0 and arr[j] > key:  # slide bigger values right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key                # drop the card into place
    return arr

print(insertion_sort([9, 1, 6]))        # [1, 6, 9]
```

## 4. Sort, then search

Because binary search needs sorted data, a common pattern is **sort first, then
search**. Reuse your Week 13 binary search on the sorted result:

```python
scores = [8, 3, 14, 11]
scores = insertion_sort(scores)         # [3, 8, 11, 14]
index = binary_search(scores, 11)       # 2
```

## 5. Tradeoffs (and the built-in sort)

Bubble and insertion sort are simple and great for learning, but they slow down
quickly as lists grow. For real work, Python's built-in tools are faster and
already tested:

```python
scores = [42, 17, 31]
scores.sort()                 # sorts the list in place -> [17, 31, 42]
ranked = sorted(scores)       # returns a new sorted list
```

The lesson: **simple sorts are easy to understand; built-in sorts are efficient.**
Knowing how sorting works under the hood helps you choose wisely.

## Common mistakes to avoid

- **Editing the original list by accident:** copy with `data[:]` if you must keep
  the original.
- **Botched swap:** `arr[i] = arr[i+1]` then `arr[i+1] = arr[i]` loses a value.
  Use the one-line tuple swap.
- **Insertion-sort loop bounds:** the `while` guard needs both `j >= 0` **and**
  `arr[j] > key`.
- **Searching before sorting:** binary search only works after the list is sorted.

## Official Python documentation

- Sorting HOW TO: <https://docs.python.org/3/howto/sorting.html>
- `sorted()`: <https://docs.python.org/3/library/functions.html#sorted>
- `list.sort()` and other list methods: <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

## How this connects to your homework

- **Problem 1 (`week14_p1_bubble_sort.py`)** — implement bubble sort; show before
  and after.
- **Problem 2 (`week14_p2_insertion_sort.py`)** — implement insertion sort.
- **Problem 3 (`week14_p3_leaderboard.py`)** — sort scores ascending.
- **Problem 4 (`week14_p4_sort_then_search.py`)** — sort, then reuse your Week 13
  binary search on the result.
- **Problem 5 (`week14_p5_reflection.txt`)** — reflect on the simplicity-vs-speed
  tradeoff.

## Quick reference

```python
a, b = b, a                # swap two values

# bubble: swap neighbors until sorted
if arr[i] > arr[i + 1]:
    arr[i], arr[i + 1] = arr[i + 1], arr[i]

# insertion: slide each item back into place
key = arr[i]
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]; j -= 1
arr[j + 1] = key

scores.sort()              # built-in, in place
sorted(scores)             # built-in, returns new list
```
