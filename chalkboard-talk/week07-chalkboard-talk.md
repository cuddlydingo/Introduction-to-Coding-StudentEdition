# Week 7 — Strings and Lists

> **Read this before you start the Week 7 homework.** Every adventure needs an
> inventory and readable messages. This week you work with **strings** (text) and
> **lists** (collections), the two workhorses behind BranchQuest's items and
> messages.
>
> Homework packet: [week07-homework.md](../homework-packets/student/week07-homework.md)

## What you'll learn this week

- How to index and slice a string, including reversing it.
- How to loop over the characters in a string and test membership with `in`.
- How to create a **list** and add to it with `.append()`.
- How to build a list inside a loop.
- Useful built-ins: `max()` and `enumerate()`.

## 1. Strings are sequences of characters

A string is an ordered sequence of characters. Each character has an **index**,
starting at `0`:

```python
word = "code"
print(word[0])    # c
print(word[1])    # o
```

### Slicing and reversing

A **slice** `word[start:stop:step]` grabs part of a string. A step of `-1` walks
backward, which reverses the whole string:

```python
word = "code"
print(word[::-1])   # edoc
```

`[::-1]` means "from start to end, stepping backward by one." This is the classic
trick for the decode-the-scrambled-message task.

### Looping over characters and the `in` test

You can loop through a string one character at a time, and `in` checks whether a
character appears in another string — perfect for counting vowels:

```python
word = "banana"
count = 0
for ch in word:
    if ch in "aeiou":     # is this character a vowel?
        count += 1
print(count)              # 3
```

`count += 1` is shorthand for `count = count + 1` (the accumulator pattern from
Week 5). To include `y` as a vowel, test against `"aeiouy"`.

## 2. Lists: ordered collections

A **list** holds many values in order, inside square brackets:

```python
inventory = ["map", "torch", "rope"]
print(inventory[0])       # map
print(len(inventory))     # 3
```

Lists are indexed just like strings, starting at `0`, and `len()` tells you how
many items there are.

### Building a list with `.append()`

`.append(x)` adds `x` to the end of a list. Start with an empty list `[]` and
fill it in a loop:

```python
items = []
for i in range(1, 6):
    item = input(f"Item {i}: ")
    items.append(item)
print("Final list:", items)
```

## 3. Handy built-ins for lists

### `max()` (and `min()`)

`max()` returns the largest value in a list; `min()` returns the smallest:

```python
numbers = [3, 9, 2, 14, 7]
print("Largest:", max(numbers))   # 14
```

### `enumerate()` for numbered lists

When you want both the **position** and the **item**, `enumerate()` gives you
both. Use `start=1` so numbering begins at 1 instead of 0:

```python
items = ["map", "torch", "rope"]
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

```text
1. map
2. torch
3. rope
```

## Common mistakes to avoid

- **Index out of range:** the last index of a length-3 list is `2`, not `3`.
  Reaching `items[3]` raises an `IndexError` (you will study this in Week 8).
- **Forgetting `.append()` returns nothing:** write `items.append(x)`, not
  `items = items.append(x)` (that would make `items` become `None`).
- **Resetting the list inside the loop:** put `items = []` *before* the loop.
- **Off-by-one numbering:** `enumerate()` starts at 0 unless you pass `start=1`.

## Official Python documentation

- Strings (tutorial): <https://docs.python.org/3/tutorial/introduction.html#text>
- String methods and the `str` type: <https://docs.python.org/3/library/stdtypes.html#string-methods>
- Lists and other data structures (tutorial): <https://docs.python.org/3/tutorial/datastructures.html>
- `enumerate()`: <https://docs.python.org/3/library/functions.html#enumerate>
- `max()`: <https://docs.python.org/3/library/functions.html#max>

## How this connects to your homework

- **Problem 1 (`week07_p1_reverse.py`)** — reverse the input with `text[::-1]`.
- **Problem 2 (`week07_p2_vowels.py`)** — loop each character and count those
  `in "aeiou"`; the bonus adds `y`.
- **Problem 3 (`week07_p3_shopping.py`)** — start an empty list and `.append()`
  five inputs.
- **Problem 4 (`week07_p4_largest.py`)** — use `max()` on a fixed list.
- **Problem 5 (`week07_p5_numbered_list.py`)** — print a numbered list with
  `enumerate(items, start=1)`.

## Quick reference

```python
text[0]          # first character
text[::-1]       # reversed string
ch in "aeiou"    # membership test -> True/False
items = []       # empty list
items.append(x)  # add to the end
len(items)       # how many items
max(nums)        # largest value
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```
