# Week 1 — Printing, Comments, and Running Your First Script

> **Read this before you start the Week 1 homework.** By the end you will know
> what a program is, how to show text on the screen with `print()`, how to leave
> notes in your code with comments, and how to actually run a Python file. That
> is everything you need for your first quest at the Maker's Guild.
>
> Homework packet: [week01-homework.md](../homework-packets/student/week01-homework.md)

## What you'll learn this week

- What a *program*, *source code*, and the *interpreter* are.
- How the `print()` function displays text.
- How to control lines and spacing in your output.
- How to write comments with `#`.
- How to run a `.py` script and how a `.txt` file is different.

## 1. The big idea: what is a program?

A **program** is a recipe: a list of exact steps, in order, for the computer to
follow. The words you type are called **source code**. Python cannot read your
mind — it does exactly what you wrote, in the exact order you wrote it.

The **interpreter** is the translator named `python` that reads your code line by
line and carries out each instruction. When you "run" a file, you are asking the
interpreter to follow your recipe from top to bottom.

> Guildmaster Ada's rule: *"The computer never guesses. Precision is the whole
> job."* A misplaced quote or comma is not failure — it is a normal part of
> coding called a **bug**, and fixing it is called **debugging**.

## 2. The `print()` function

`print()` is a built-in tool that displays text on the screen. You put the text
you want to show inside quotes, inside the parentheses.

```python
print("Welcome to the Maker's Guild!")
```

Output:

```text
Welcome to the Maker's Guild!
```

Some things to notice:

- The text inside quotes is called a **string**. You can use double quotes
  `"like this"` or single quotes `'like this'` — just be consistent on each line.
- The parentheses `()` are how you *call* (use) the function. `print` without
  parentheses does nothing.

### Each `print()` starts a new line

Every `print()` call moves to a fresh line when it finishes. To show three
lines, use three `print()` calls:

```python
print("Aria the archer")
print("Dax the healer")
print("Lina the mage")
```

Output:

```text
Aria the archer
Dax the healer
Lina the mage
```

### Printing more than one value at once

You can hand `print()` several values separated by commas. It puts a single
space between them:

```python
print("Party size:", 4)
```

Output:

```text
Party size: 4
```

Notice that `4` has no quotes — it is a number, not a string, and `print()` can
show both. Two optional settings let you change the spacing:

- `sep=` sets what goes *between* the values (default is a space).
- `end=` sets what goes at the *end* (default is a new line).

```python
print("torch", "rope", "map", sep="\n")
```

Output:

```text
torch
rope
map
```

`\n` is a special "newline" character. You will use `sep="\n"` again in later
weeks, so it is worth remembering.

## 3. Comments: notes to your future self

A **comment** is a note for humans. Python ignores everything after a `#` on that
line, so comments never change what your program does.

```python
# This line greets the player.
print("Hello, apprentice!")  # a comment can also sit after code
```

Comments explain *why* you did something. Good comments make your code easy to
come back to next week.

## 4. Running your script

Coding is a cycle: **WRITE → SAVE → RUN → READ OUTPUT → FIX → run again.**

1. Write your code in a file that ends in `.py`, for example `week01_p1_hello.py`.
2. Save the file.
3. Open a terminal and go to the folder that holds the file.
4. Run it with the interpreter:

   ```text
   python week01_p1_hello.py
   ```

5. Read the output. If there is an error, read the message, fix the line it
   points to, and run it again.

> On some computers the command is `python3` instead of `python`. Both ask the
> same interpreter to run your file.

## 5. Plain text files (`.txt`)

Not every file is a program. A **`.txt`** file is just plain text — a checklist,
notes, or a list. You do **not** run it with `python`; you simply type your text
and save. One of your Week 1 tasks asks for a `.txt` checklist, so create it like
any other document.

## Common mistakes to avoid

- **Forgetting the quotes:** `print(Hello)` fails because Python thinks `Hello`
  is a variable name. Write `print("Hello")`.
- **Forgetting the parentheses:** `print "Hello"` is not valid in Python 3.
- **Mismatched quotes:** `print("Hello')` mixes `"` and `'`. Match them.
- **Expecting one `print()` to make several lines:** it makes one line unless you
  use `\n` or more `print()` calls.

## Official Python documentation

- `print()` function: <https://docs.python.org/3/library/functions.html#print>
- All built-in functions: <https://docs.python.org/3/library/functions.html>
- Comments and your first steps (tutorial): <https://docs.python.org/3/tutorial/introduction.html>
- Input and output, including newlines (tutorial): <https://docs.python.org/3/tutorial/inputoutput.html>

## How this connects to your homework

- **Problem 1 (`week01_p1_hello.py`)** — one `print()` with a welcome string.
- **Problem 2 (`week01_p2_intro.py`)** — two `print()` calls, one for the name
  line and one for the grade line.
- **Problem 3 (`week01_p3_goals.py`)** — three `print()` calls, one per goal.
- **Problem 4 (`week01_p4_comments.py`)** — at least two `#` comments plus one
  `print()`. The comments explain the code; only the `print()` shows output.
- **Problem 5 (`week01_p5_checklist.txt`)** — a plain `.txt` file listing the run
  steps from Section 4 (open terminal, navigate, run, read output, fix and rerun).

## Quick reference

```python
print("text")                 # show a string on its own line
print("A", "B")               # show values separated by a space -> A B
print("A", "B", sep="\n")     # separate with a newline instead
print("no newline", end=" ")  # do not move to a new line at the end
# this is a comment; Python ignores it
```

Run a file: `python filename.py`
