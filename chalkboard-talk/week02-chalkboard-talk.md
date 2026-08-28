# Week 2 — Input, Variables, and Data Types

> **Read this before you start the Week 2 homework.** This week your programs
> start *listening*. You will ask the player questions with `input()`, store
> answers in **variables**, learn the four basic **data types**, and format neat
> output with **f-strings**.
>
> Homework packet: [week02-homework.md](../homework-packets/student/week02-homework.md)

## What you'll learn this week

- How to store values in **variables**.
- How to read keyboard input with `input()`.
- The four core **data types**: `int`, `float`, `str`, `bool`.
- How to check a value's type with `type()`.
- How to convert text into numbers with `int()` and `float()`.
- How to build clean output with **f-strings**.

## 1. Variables: labeled boxes for values

A **variable** is a name that holds a value so you can use it later. You create
one with `=` (the assignment operator):

```python
hero = "Aria"
level = 3
```

Read `hero = "Aria"` as *"put the string Aria into the box named hero,"* not as
math equality. Naming rules: use letters, numbers, and underscores; start with a
letter; and prefer clear `snake_case` names like `player_name`.

## 2. Reading input with `input()`

`input()` pauses the program, shows a prompt, waits for the player to type
something and press Enter, then hands back what they typed.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

```text
Enter your name: Aria
Hello, Aria!
```

**The most important rule of Week 2:** `input()` *always* gives you a **string**,
even if the player types digits. `"13"` is text, not the number 13. We will fix
that in Section 5.

## 3. The four core data types

Every value in Python has a **type**. This week you use four:

| Type    | Name           | Example        | Used for                     |
| ------- | -------------- | -------------- | ---------------------------- |
| `int`   | integer        | `7`, `-2`      | whole numbers                |
| `float` | floating point | `3.5`, `20.0`  | numbers with a decimal point |
| `str`   | string         | `"torch"`      | text                         |
| `bool`  | boolean        | `True`, `False`| yes/no, on/off values        |

```python
health = 100        # int
speed = 4.5         # float
weapon = "sword"    # str
is_ready = True     # bool
```

Note that `True` and `False` are capitalized and have no quotes.

## 4. Checking a type with `type()`

The `type()` function tells you what kind of value you have. It is a great
debugging tool.

```python
print(type(100))      # <class 'int'>
print(type(4.5))      # <class 'float'>
print(type("sword"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```

If you want each result on its own line from a single `print()`, use the
`sep="\n"` trick from Week 1:

```python
print(type(1), type(1.5), type("x"), type(True), sep="\n")
```

## 5. Converting text into numbers

Because `input()` returns a string, you must **convert** it before doing math:

- `int("13")` becomes the integer `13`.
- `float("68")` becomes `68.0`.
- `str(14)` becomes the text `"14"`.

```python
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
```

```text
Enter your age: 13
Next year you will be 14
```

Without `int()`, `age + 1` would crash, because you cannot add a number to text.

## 6. F-strings: clean, formatted output

An **f-string** lets you drop variables straight into a string. Put an `f` right
before the opening quote, then wrap any variable in `{curly braces}`.

```python
name = "Aria"
age = 13
print(f"Name: {name}")
print(f"{name} is {age} years old.")
```

```text
Name: Aria
Aria is 13 years old.
```

F-strings are cleaner than gluing pieces together with `+`, and they handle
numbers without extra conversions. You can also make one f-string span multiple
output lines with `\n`:

```python
print(f"Name: {name}\nAge: {age}")
```

## Common mistakes to avoid

- **Doing math on input directly:** `age = input(...)` then `age + 1` fails.
  Wrap it: `age = int(input(...))`.
- **Forgetting the `f`:** `print("Hello {name}")` prints the braces literally.
  You need `print(f"Hello {name}")`.
- **Quoting `True`/`False`:** `"True"` is a string, not a boolean.
- **Converting words to numbers:** `int("hello")` raises a `ValueError`. Only
  convert text that actually looks like a number.

## Official Python documentation

- `input()` function: <https://docs.python.org/3/library/functions.html#input>
- `type()` function: <https://docs.python.org/3/library/functions.html#type>
- `int()`: <https://docs.python.org/3/library/functions.html#int> · `float()`: <https://docs.python.org/3/library/functions.html#float>
- Numeric, text, and boolean types: <https://docs.python.org/3/library/stdtypes.html>
- Formatted string literals (f-strings) tutorial: <https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals>

## How this connects to your homework

- **Problem 1 (`week02_p1_name_card.py`)** — `input()` for a name, then an
  f-string greeting.
- **Problem 2 (`week02_p2_types.py`)** — make one `int`, `float`, `str`, and
  `bool` variable, then `print(type(...))` for each.
- **Problem 3 (`week02_p3_age_next_year.py`)** — `int(input(...))` so you can add
  1 to the age.
- **Problem 4 (`week02_p4_favorites.py`)** — three `input()` calls, then one
  f-string summary line.
- **Problem 5 (`week02_p5_profile_card.py`)** — collect name, age, hobby and
  print a formatted card (f-strings with `\n` work well).

## Quick reference

```python
answer = input("Prompt: ")   # always returns a string
number = int(answer)         # convert text -> whole number
price  = float(answer)       # convert text -> decimal number
type(x)                      # show the type of x
name = "Aria"
print(f"Hi {name}, level {3}")  # f-string with variables
```
