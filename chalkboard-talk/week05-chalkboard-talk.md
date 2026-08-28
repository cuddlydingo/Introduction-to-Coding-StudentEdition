# Week 5 — Loops: Repeating Work with `for` and `while`

> **Read this before you start the Week 5 homework.** Loops let heroes repeat
> drills and let the Guild vault keep asking until the right code is entered.
> This week you learn to repeat work without copying and pasting.
>
> Homework packet: [week05-homework.md](../homework-packets/student/week05-homework.md)

## What you'll learn this week

- How a `for` loop repeats a set number of times using `range()`.
- How `range(start, stop, step)` controls the numbers you get.
- How a `while` loop repeats *until* a condition changes.
- How to stop a loop with `break`.
- The counter/accumulator pattern.

## 1. The `for` loop with `range()`

A **`for` loop** repeats its indented block once for each item it is given.
`range()` produces a sequence of numbers to loop over.

```python
for i in range(1, 6):
    print(i)
```

```text
1
2
3
4
5
```

Read it as: *"let `i` be each number in the range, and run the block each time."*
Like `if`, a `for` line ends in a colon and its body is indented.

### How `range()` works

`range(start, stop, step)` counts from `start` **up to but not including** `stop`:

- `range(5)` gives `0, 1, 2, 3, 4` (starts at 0 by default).
- `range(1, 6)` gives `1, 2, 3, 4, 5`.
- `range(2, 11, 2)` gives `2, 4, 6, 8, 10` (step of 2 -> even numbers).

The "stop is not included" rule is why counting to `n` needs `range(1, n + 1)`:

```python
n = int(input("N: "))
for i in range(1, n + 1):
    print(i)
```

### Using the loop variable in a calculation

The loop variable changes each pass, so you can compute with it — perfect for a
times table:

```python
number = 3
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
```

## 2. The `while` loop

A **`while` loop** repeats **as long as** its condition stays `True`. Use it when
you do not know in advance how many times you need to repeat.

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1     # this MUST change, or the loop never ends
```

The line that moves you toward the exit (here `count = count + 1`) is essential.
Forget it and you get an **infinite loop**.

## 3. Stopping with `break`

`break` immediately exits the loop. A common pattern is "loop forever, and break
when the goal is met" — exactly how the vault keeps asking until the code is
right:

```python
secret = "lion"
while True:
    guess = input("Password: ")
    if guess == secret:
        print("Access granted")
        break
    print("Try again")
```

You can compare with `<`, `>`, and `==` inside the loop to give hints:

```python
target = 11
while True:
    guess = int(input("Guess: "))
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct")
        break
```

## 4. The counter / accumulator pattern

A very common loop job is to keep a running total or count. Start a variable
*before* the loop, then update it *inside*:

```python
total = 0
for i in range(1, 6):
    total = total + i     # add each number
print("Total:", total)    # Total: 15
```

You will reuse this pattern all semester (counting vowels, summing scores, and
more).

## Common mistakes to avoid

- **Off-by-one errors:** `range(1, n)` stops at `n - 1`. Use `range(1, n + 1)` to
  include `n`.
- **Infinite `while` loops:** always change the condition variable, or include a
  `break`.
- **Indentation:** everything that should repeat must be indented under the loop.
- **Resetting a total inside the loop:** put `total = 0` *before* the loop, not
  inside it.

## Official Python documentation

- `for` statements (tutorial): <https://docs.python.org/3/tutorial/controlflow.html#for-statements>
- The `range()` function: <https://docs.python.org/3/library/stdtypes.html#range>
- The `while` statement (reference): <https://docs.python.org/3/reference/compound_stmts.html#the-while-statement>
- `break`, `continue`, and loop `else`: <https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements>

## How this connects to your homework

- **Problem 1 (`week05_p1_count.py`)** — `for i in range(1, n + 1)` to print 1..N.
- **Problem 2 (`week05_p2_even.py`)** — `range(2, n + 1, 2)` for even numbers.
- **Problem 3 (`week05_p3_table.py`)** — loop `range(1, 13)` and print
  `number * i` each pass.
- **Problem 4 (`week05_p4_retry_password.py`)** — `while True` with `break` when
  the password matches.
- **Problem 5 (`week05_p5_guess.py`)** — loop and compare the guess with `<`, `>`,
  `==` against a fixed target.

## Quick reference

```python
for i in range(1, n + 1):   # count 1..n
    print(i)

for i in range(2, n + 1, 2):  # even numbers up to n
    ...

while condition:            # repeat while True
    ...

while True:                 # repeat until you break
    if done:
        break
```
