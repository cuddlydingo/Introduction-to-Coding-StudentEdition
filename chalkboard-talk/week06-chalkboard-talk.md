# Week 6 — Functions: Building Reusable Tools

> **Read this before you start the Week 6 homework.** Ada's maker's rule: build
> tools you can reuse, not one-off scripts. This week you forge your first
> **functions** — named, reusable blocks of code.
>
> Homework packet: [week06-homework.md](../homework-packets/student/week06-homework.md)

## What you'll learn this week

- How to define a function with `def`.
- How **parameters** pass information into a function.
- How `return` sends a value back out.
- The difference between `return` and `print`.
- How a `main()` function organizes a program.

## 1. Defining a function

A **function** is a named recipe you can run whenever you want. You define it
once with `def`, then **call** it as many times as you like.

```python
def greet():
    print("Hello, apprentice!")

greet()    # call it
greet()    # call it again
```

```text
Hello, apprentice!
Hello, apprentice!
```

The `def` line ends with a colon, and the function body is indented — the same
shape as `if` and `for`.

## 2. Parameters: passing information in

A **parameter** is a variable listed in the parentheses of the `def` line. When
you call the function, you pass an **argument** that fills it in.

```python
def greet(name):            # name is a parameter
    print(f"Hello, {name}!")

greet("Aria")               # "Aria" is the argument
greet("Dax")
```

```text
Hello, Aria!
Hello, Dax!
```

Functions can take several parameters, separated by commas:

```python
def rectangle_area(length, width):
    print(length * width)
```

## 3. `return`: sending a value back

`return` hands a value back to whoever called the function, so you can use the
result later. A function that returns a value is like a calculator: you feed it
inputs and it gives you an answer.

```python
def add(a, b):
    return a + b

result = add(3, 4)          # result is now 7
print("add(3, 4) ->", result)
```

Once Python hits `return`, the function ends immediately. You can use the
returned value in more math, store it, or print it.

### `return` vs `print` — a key distinction

- `print` **shows** a value on screen and gives nothing back to your code.
- `return` **hands a value back** so your program can keep using it.

```python
def double_print(n):
    print(n * 2)            # shows it, but you cannot reuse it

def double_return(n):
    return n * 2            # gives it back, so you can

x = double_return(5)        # x is 10
print(x + 1)                # 11  -- only works because we returned
```

Returning booleans is common for yes/no helpers:

```python
def is_even(n):
    return n % 2 == 0       # True when n is even

print(is_even(8))           # True
print(is_even(7))           # False
```

## 4. Organizing with `main()`

As programs grow, makers gather the top-level steps into a `main()` function and
call it once at the bottom. This keeps the "what happens first" logic in one
clear place.

```python
def add(a, b):
    return a + b

def area(length, width):
    return length * width

def main():
    print("Sum:", add(4, 5))
    print("Area:", area(3, 4))
    print("Even check:", is_even(10))

main()
```

Building small functions and calling them from `main()` is exactly how you will
assemble your Cave Quest game in Week 9.

## Common mistakes to avoid

- **Defining but never calling:** `def greet(): ...` does nothing until you write
  `greet()`.
- **Confusing `return` and `print`:** if you need the value later, `return` it.
- **Forgetting arguments:** calling `greet()` when the function needs
  `greet(name)` raises a `TypeError`.
- **Code after `return` in the same block:** it never runs, because `return`
  exits the function.
- **Indentation:** the function body must be indented under the `def` line.

## Official Python documentation

- Defining functions (tutorial): <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
- More on defining functions (parameters, arguments): <https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions>
- Function definitions (reference): <https://docs.python.org/3/reference/compound_stmts.html#function-definitions>
- The `return` statement: <https://docs.python.org/3/reference/simple_stmts.html#the-return-statement>

## How this connects to your homework

- **Problem 1 (`week06_p1_add_function.py`)** — define `add(a, b)` that returns
  `a + b`.
- **Problem 2 (`week06_p2_area.py`)** — define `rectangle_area(length, width)`.
- **Problem 3 (`week06_p3_is_even.py`)** — define `is_even(n)` returning
  `n % 2 == 0`.
- **Problem 4 (`week06_p4_greeting.py`)** — a `greet(name)` function that uses its
  parameter.
- **Problem 5 (`week06_p5_main_program.py`)** — a `main()` that calls at least
  three of your functions.

## Quick reference

```python
def name(param1, param2):   # define
    return param1 + param2  # send a value back

value = name(3, 4)          # call and capture the result

def main():                 # organize top-level steps
    print(name(1, 2))
main()                      # run the program
```
