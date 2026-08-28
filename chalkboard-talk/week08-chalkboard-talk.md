# Week 8 — Debugging: Reading Errors and Fixing Bugs

> **Read this before you start the Week 8 homework.** The Glitch has swarmed
> BranchQuest and three scripts crash. Grace, the Guild's Chief Bug-Hunter,
> teaches you to hunt bugs one **traceback** at a time. This week is about
> reading error messages calmly and fixing them.
>
> Homework packet: [week08-homework.md](../homework-packets/student/week08-homework.md)
> · Buggy starter files: `course-materials/week08-buggy-files/`

## What you'll learn this week

- How to read a Python **traceback** (from the bottom up).
- Four common errors: `NameError`, `TypeError`, `IndexError`, `ValueError`.
- What causes each one and how to fix it.
- A repeatable debugging strategy.

## 1. Reading a traceback

When Python hits a problem it stops and prints a **traceback**. It looks scary,
but the two most useful parts are at the very **bottom**:

```text
Traceback (most recent call last):
  File "game.py", line 3, in <module>
    print(player)
NameError: name 'player' is not defined
```

- The **last line** names the error type and gives a short message
  (`NameError: name 'player' is not defined`).
- The line just above shows the **file and line number** where it happened
  (`line 3`).

**Grace's rule:** read the last line first, then jump to the line number it
points at. Ninety percent of debugging is reading the message carefully.

## 2. The four errors you will fix

### `NameError` — the missing name

Python does not recognize a name you used. Usual causes: a typo, or using a
variable before you created it (including capitalization — `Player` and `player`
are different names).

```python
# Broken
player_name = "Aria"
print(playerName)     # NameError: playerName was never defined

# Fixed — use the exact same name
player_name = "Aria"
print(player_name)
```

### `TypeError` — the wrong kind of value

You tried an operation on the wrong type, such as adding text to a number.
Remember `input()` returns a string.

```python
# Broken
a = input("Score: ")   # a is a string like "12"
b = input("Bonus: ")   # b is a string like "6"
print(a + b)           # "126", not 18!

# Fixed — convert to numbers first
a = int(input("Score: "))
b = int(input("Bonus: "))
print(a + b)           # 18
```

### `IndexError` — reaching past the end

You asked for a list position that does not exist. A list of 3 items has valid
indexes `0`, `1`, `2`.

```python
items = ["map", "torch", "rope"]

# Broken
print(items[3])        # IndexError: list index out of range

# Fixed — check the length before you reach in
if len(items) > 3:
    print(items[3])
else:
    print("No fourth item found.")
```

### `ValueError` — the right type, an impossible value

The type is fine but the value cannot be used that way — most often converting
non-numeric text to a number.

```python
# Broken
age = int("thirteen")  # ValueError: invalid literal for int()

# Fixed — only convert text that is actually numeric
text = input("Age: ")
if text.isdigit():
    age = int(text)
else:
    print("Please type a number.")
```

## 3. A repeatable debugging strategy

1. **Read the last line** of the traceback — what error, what message?
2. **Go to the line number** it names.
3. **Form a guess:** what type or name is wrong here?
4. **Make one small change**, save, and rerun.
5. **Repeat** until the output matches the target.

Keeping a short **bug log** (what broke, why, how you fixed it) — as Grace does —
makes you faster the next time you meet the same error.

## Common mistakes to avoid

- **Panicking at the wall of red text:** only the last line and the line number
  matter first.
- **Changing many lines at once:** change one thing, then rerun, so you know what
  fixed it.
- **Ignoring capitalization:** `player_name` and `Player_Name` are different.
- **Forgetting conversions:** most `TypeError`/`ValueError` bugs trace back to a
  string that should have been an `int`.

## Official Python documentation

- Errors and exceptions (tutorial): <https://docs.python.org/3/tutorial/errors.html>
- Built-in exceptions (the full list): <https://docs.python.org/3/library/exceptions.html>
- `NameError`: <https://docs.python.org/3/library/exceptions.html#NameError>
- `TypeError`: <https://docs.python.org/3/library/exceptions.html#TypeError>
- `IndexError`: <https://docs.python.org/3/library/exceptions.html#IndexError>
- `ValueError`: <https://docs.python.org/3/library/exceptions.html#ValueError>

## How this connects to your homework

- **Problem 1 (`week08_p1_name_error.py`)** — fix a `NameError` by matching the
  variable name exactly.
- **Problem 2 (`week08_p2_type_error.py`)** — fix a `TypeError` by converting
  input to numbers before math.
- **Problem 3 (`week08_p3_index_error.py`)** — fix an `IndexError` with a length
  check before indexing.
- **Problem 4 (`week08_p4_debug_log.txt`)** — write a bug log: name each bug, its
  cause, and your fix.
- **Problem 5 (`week08_p5_reflection.txt`)** — reflect on reading tracebacks and
  the fix-and-rerun cycle.

## Quick reference

| Error        | Typical cause                    | Typical fix                         |
| ------------ | -------------------------------- | ----------------------------------- |
| `NameError`  | typo / undefined variable        | use the exact defined name          |
| `TypeError`  | mixing text and numbers          | `int(...)` / `float(...)` first     |
| `IndexError` | index past the end of a list     | check `len()` before indexing       |
| `ValueError` | converting non-numeric text      | validate with `.isdigit()` first    |

Read the traceback **bottom-up**: error type -> message -> line number.
