# Week 16 — Concepts Across Languages (and a Live-Data Bonus)

> **Read this before you start the Week 16 homework.** A neighboring guild speaks
> other "dialects" — Lua, C++, and Java. Ada sends you to learn how BranchQuest
> could be ported, so you can read code in any language you meet. The same *ideas*
> you already know show up everywhere; only the **syntax** changes.
>
> Homework packet: [week16-homework.md](../homework-packets/student/week16-homework.md)
> · Samples: `course-materials/week16-cross-language-samples/`
> · Optional API bonus: `course-materials/week16-api-bonus/`

## What you'll learn this week

- Why programming **concepts** transfer across languages.
- How variables, loops, conditionals, and functions look in Python vs Java/C++.
- The most common **syntax differences** between languages.
- (Bonus) How to pull **live data** from a web API with `requests`.

## 1. Concepts are shared; syntax differs

Every language you will meet has the same building blocks you already learned:
**variables**, **conditionals** (`if`), **loops**, and **functions**. A `for`
loop in Java solves the same "repeat this" problem as a `for` loop in Python —
the punctuation just looks different. Learn the concept once and you can read any
dialect.

## 2. The same idea in different dialects

**A variable:**

```python
score = 10          # Python: no type keyword
```

```java
int score = 10;     // Java: declare the type, end with a semicolon
```

**A loop from 1 to 5:**

```text
Idea (pseudocode): FOR i from 1 to 5

Python:  for i in range(1, 6):
C++:     for (int i = 1; i <= 5; i++) { ... }
```

**A function:**

```python
def add(a, b):          # Python
    return a + b
```

```java
int add(int a, int b) { // Java: declare return type and parameter types
    return a + b;
}
```

Notice the logic is identical — only the wrapping changes.

## 3. Common syntax differences

| Difference          | Python                 | Java / C++                            |
| ------------------- | ---------------------- | ------------------------------------- |
| Blocks              | indentation            | curly braces `{ }`                    |
| End of a statement  | end of line            | semicolon `;`                         |
| Variable types      | inferred automatically | you declare the type                  |
| Printing            | `print(...)`           | `System.out.println(...)` / `cout <<` |
| Program entry point | top-level code         | a `main` method/function              |
| Comments            | `#`                    | `//` or `/* ... */`                   |

Being able to list five or more of these differences is a Week 16 goal.

## 4. Why this matters

Because concepts travel, learning your **second** language is far faster than the
first — you are really just learning new syntax for ideas you already own. That is
why makers say: *learn concepts first; syntax can be picked up later.*

## 5. Bonus challenge — live data with `requests`

The optional bonus pulls real data into BranchQuest from a public web **API** (a
service you send a request to and get data back from, usually as **JSON**). This
uses the third-party `requests` library.

```python
import requests

name = input("Pokemon name: ").strip().lower()
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=10)

if response.status_code == 200:          # 200 means success
    data = response.json()               # parse JSON into a Python dict
    print("Name:", data["name"].title())
    print("ID:", data["id"])
    print("Weight:", data["weight"])
else:
    print("Could not find that Pokemon. Status:", response.status_code)
```

Key ideas:

- `requests.get(url, timeout=10)` sends the request and waits at most 10 seconds.
- `response.status_code` reports the result — handle `200` **and** at least one
  non-200 case (like `404 Not Found`).
- `response.json()` turns the reply into a dictionary you can read with keys
  (Week 11!).

Choose an API from the curated list in
`course-materials/week16-api-bonus/README.md` and print 3-5 useful fields.

## Common mistakes to avoid

- **Thinking languages are unrelated:** they share the same core concepts.
- **Comparing syntax instead of ideas:** focus on what each construct *does*.
- **(Bonus) Assuming the request succeeds:** always check `status_code` before
  reading `.json()`.
- **(Bonus) No timeout:** always pass `timeout=` so a slow server cannot hang your
  program.

## Official documentation

- Python control flow (for comparing constructs): <https://docs.python.org/3/tutorial/controlflow.html>
- Python `json` module (parsing JSON): <https://docs.python.org/3/library/json.html>
- `requests` library (third-party, used in the bonus): <https://requests.readthedocs.io/en/latest/>
- Python's list of other implementations/languages context: <https://docs.python.org/3/>

## How this connects to your homework

- **Problem 1 (`week16_p1_constructs.txt`)** — pair equivalent constructs
  (variable, loop, function) in Python vs Java.
- **Problem 2 (`week16_p2_translation.txt`)** — show one loop as pseudocode, then
  Python and C++ style.
- **Problem 3 (`week16_p3_differences.txt`)** — list at least five concrete syntax
  differences.
- **Problem 4 (`week16_p4_shared_concepts.txt`)** — explain why learning one
  language helps with the others.
- **Problem 5 (`week16_p5_summary.txt`)** — three similarities, three differences,
  one takeaway.
- **Bonus (`week16_bonus_api_explorer.py`)** — fetch live data, handle status
  codes, parse JSON, print 3-5 fields.

## Quick reference

```text
Shared concepts: variables · conditionals · loops · functions
Syntax varies:   braces vs indentation · semicolons · type declarations · main()

# Bonus API pattern
import requests
r = requests.get(url, timeout=10)
if r.status_code == 200:
    data = r.json()      # -> dict, read with data["key"]
else:
    ...                  # handle the non-200 case
```
