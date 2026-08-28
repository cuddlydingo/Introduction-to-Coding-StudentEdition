# Week 3 — Math, Comparisons, and Boolean Logic

> **Read this before you start the Week 3 homework.** Grace the Bug-Hunter warns
> that sloppy arithmetic is exactly the crack the Glitch slips through, so this
> week is about calculations Python can trust: math operators, comparisons, and
> combining conditions with `and`/`or`.
>
> Homework packet: [week03-homework.md](../homework-packets/student/week03-homework.md)

## What you'll learn this week

- The arithmetic operators and the order Python applies them.
- The difference between `/`, `//`, and `%`.
- How comparison operators produce `True` or `False`.
- How to combine conditions with `and`, `or`, and `not`.
- How to convert input and apply a formula (Fahrenheit to Celsius).

## 1. Arithmetic operators

Python does math with these operators:

| Operator | Meaning          | Example  | Result |
| -------- | ---------------- | -------- | ------ |
| `+`      | add              | `4 + 6`  | `10`   |
| `-`      | subtract         | `9 - 5`  | `4`    |
| `*`      | multiply         | `6 * 3`  | `18`   |
| `/`      | divide           | `7 / 2`  | `3.5`  |
| `//`     | floor divide     | `7 // 2` | `3`    |
| `%`      | remainder (mod)  | `7 % 2`  | `1`    |
| `**`     | power (exponent) | `2 ** 3` | `8`    |

```python
a = 4
b = 6
print("Sum:", a + b)
print("Product:", a * b)
```

```text
Sum: 10
Product: 24
```

### `/` vs `//` vs `%`

- `/` always gives a **float**: `10 / 2` is `5.0`, not `5`.
- `//` throws away the fractional part: `10 // 3` is `3`.
- `%` gives what is *left over*: `10 % 3` is `1`. This is how you test for even
  numbers later (`n % 2 == 0`).

### Order of operations

Python follows normal math order: parentheses first, then `**`, then `*` `/`
`//` `%`, then `+` `-`. Use parentheses to make your intent clear:

```python
celsius = (f - 32) * 5 / 9   # subtraction happens first because of the ()
```

## 2. Do the math on numbers, not strings

Remember from Week 2: `input()` returns a string. Convert before you calculate,
or `+` will glue text together instead of adding.

```python
players = int(input("Players: "))
snacks = int(input("Snacks each: "))
print("Total snacks:", players * snacks)
```

## 3. Comparison operators

A **comparison** asks a yes/no question and answers with a boolean (`True` or
`False`).

| Operator | Meaning                  | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | equal to                 | `5 == 5` | `True`  |
| `!=`     | not equal to             | `5 != 4` | `True`  |
| `>`      | greater than             | `9 > 5`  | `True`  |
| `<`      | less than                | `9 < 5`  | `False` |
| `>=`     | greater than or equal to | `5 >= 5` | `True`  |
| `<=`     | less than or equal to    | `4 <= 5` | `True`  |

**Watch out:** `=` assigns a value, but `==` *compares* two values. Mixing them
up is one of the most common beginner bugs.

```python
a = 9
b = 5
print("First > Second:", a > b)   # First > Second: True
```

## 4. Boolean logic: `and`, `or`, `not`

You can combine yes/no questions:

- `and` is `True` only when **both** sides are `True`.
- `or` is `True` when **at least one** side is `True`.
- `not` flips a boolean.

```python
age = 14
permission = "yes"
allowed = age >= 13 and permission == "yes"
print("Allowed:", allowed)   # Allowed: True
```

A quick truth summary:

| A       | B       | `A and B` | `A or B` |
| ------- | ------- | --------- | -------- |
| `True`  | `True`  | `True`    | `True`   |
| `True`  | `False` | `False`   | `True`   |
| `False` | `True`  | `False`   | `True`   |
| `False` | `False` | `False`   | `False`  |

### Cleaning up text before comparing

Players type messily. `"Yes"`, `" yes "`, and `"yes"` look different to Python.
Tidy input first:

```python
permission = input("Permission (yes/no): ").strip().lower()
```

`.strip()` removes spaces at the ends; `.lower()` makes it all lowercase, so
`" YES "` becomes `"yes"`.

## Common mistakes to avoid

- **Using `=` instead of `==`** inside a comparison.
- **Comparing a string to a number:** `"5" == 5` is `False`. Convert first.
- **Expecting `/` to give a whole number:** it returns a float; use `//` if you
  want the whole part.
- **Chaining `or` wrong:** `permission == "yes" or "y"` is always `True`. Write
  `permission == "yes" or permission == "y"`.

## Official Python documentation

- Numeric types and operators: <https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex>
- Comparisons: <https://docs.python.org/3/library/stdtypes.html#comparisons>
- Boolean operations `and`, `or`, `not`: <https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not>
- Numbers in the tutorial: <https://docs.python.org/3/tutorial/introduction.html#numbers>

## How this connects to your homework

- **Problem 1 (`week03_p1_math.py`)** — convert two inputs to `int`, then print
  their sum and product.
- **Problem 2 (`week03_p2_compare.py`)** — print the result of `a > b`.
- **Problem 3 (`week03_p3_logic.py`)** — combine `age >= 13` **and** a permission
  check with `and`; clean the input with `.strip().lower()`.
- **Problem 4 (`week03_p4_snacks.py`)** — multiply players by snacks each.
- **Problem 5 (`week03_p5_temp.py`)** — use `float(input(...))` and the formula
  `(f - 32) * 5 / 9`; mind the parentheses.

## Quick reference

```python
7 // 2      # 3   (floor division)
7 % 2       # 1   (remainder -> even test: n % 2 == 0)
2 ** 3      # 8   (power)
a == b      # equal?   a != b   not equal?
a >= b      # at least?
x and y     # both true?
x or y      # either true?
text.strip().lower()   # tidy user input before comparing
```
