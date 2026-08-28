# Week 4 — Making Decisions with `if`, `elif`, and `else`

> **Read this before you start the Week 4 homework.** Ada says branching is the
> heart of BranchQuest — the choices that make every player's path different.
> This week you build those branches with `if` statements.
>
> Homework packet: [week04-homework.md](../homework-packets/student/week04-homework.md)

## What you'll learn this week

- How an `if` statement runs code only when a condition is `True`.
- Why **indentation** and the **colon** matter.
- How to add `else` and `elif` for multiple paths.
- How to order your branches correctly.
- How to combine conditions and compare strings safely.

## 1. The `if` statement

An `if` statement runs a block of code **only when** its condition is `True`.
The condition is any expression that evaluates to a boolean (see Week 3).

```python
score = 82
if score >= 70:
    print("Result: Pass")
```

Two rules you must follow:

1. The line ends with a **colon** `:`.
2. The code that belongs to the `if` is **indented** (four spaces is standard).
   Indentation is how Python knows which lines are "inside" the `if`.

```python
if score >= 70:
    print("You passed!")     # inside the if
    print("Well done.")      # also inside the if
print("This always runs.")   # not indented -> always runs
```

## 2. `else`: the other path

`else` gives you a second block that runs when the condition is `False`. Exactly
one of the two blocks runs.

```python
score = 55
if score >= 70:
    print("Result: Pass")
else:
    print("Result: Fail")
```

## 3. `elif`: more than two paths

For three or more choices, add one or more `elif` (short for "else if") branches.
Python checks them **top to bottom** and runs the **first** one that is `True`,
then skips the rest.

```python
age = 15
if age < 13:
    print("Ticket type: Child")
elif age < 18:
    print("Ticket type: Teen")
else:
    print("Ticket type: Adult")
```

### Order matters

Because Python stops at the first match, put the most specific or smallest
ranges first. If you wrote `if age < 18` before `if age < 13`, a 10-year-old
would wrongly match the teen branch first. Read your branches out loud in order
to check them.

## 4. Combining conditions

Use the Week 3 logic operators to require more than one thing:

```python
temp = 55
rain = input("Raining? (yes/no): ").strip().lower()
if temp < 60 and rain == "yes":
    print("Advice: Wear a jacket and bring an umbrella.")
elif temp < 60:
    print("Advice: Wear a jacket.")
else:
    print("Advice: Light clothing is okay.")
```

## 5. Comparing strings safely

When you branch on typed text, compare against clean values and normalize the
input first, just like in Week 3:

```python
entered = input("Enter password: ")
if entered == "tiger123":
    print("Access granted")
else:
    print("Access denied")
```

### Bonus: the one-line conditional

For a simple two-way choice you may see this compact form (a *conditional
expression*). It is optional, but handy:

```python
print("Result: Pass" if score >= 70 else "Result: Fail")
```

## Common mistakes to avoid

- **Missing colon:** `if score >= 70` without the `:` is a `SyntaxError`.
- **Wrong indentation:** mixing spaces inconsistently causes an
  `IndentationError`. Pick four spaces and stay consistent.
- **Using `=` instead of `==`:** `if x = 5:` is an error; comparison needs `==`.
- **Overlapping ranges in the wrong order:** check specific cases before general
  ones.
- **Repeating `if` when you meant `elif`:** separate `if`s can both run; `elif`
  makes them exclusive.

## Official Python documentation

- `if` statements (tutorial): <https://docs.python.org/3/tutorial/controlflow.html#if-statements>
- The `if` statement (reference): <https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>
- Comparisons: <https://docs.python.org/3/library/stdtypes.html#comparisons>
- Boolean operations: <https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not>

## How this connects to your homework

- **Problem 1 (`week04_p1_pass_fail.py`)** — one `if/else` on `score >= 70`.
- **Problem 2 (`week04_p2_ticket.py`)** — three-way `if/elif/else` by age; order
  the ranges from youngest to oldest.
- **Problem 3 (`week04_p3_weather.py`)** — combine a temperature test and a rain
  test with `and`.
- **Problem 4 (`week04_p4_level_gate.py`)** — three branches for a locked /
  almost / open gate.
- **Problem 5 (`week04_p5_password_check.py`)** — compare typed input to a stored
  password with `==`.

## Quick reference

```python
if condition:
    # runs when condition is True
elif other_condition:
    # runs when the first was False and this is True
else:
    # runs when nothing above matched

# one-line form
result = "yes" if condition else "no"
```
