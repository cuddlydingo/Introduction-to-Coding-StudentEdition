# Week 10 — Refactoring and Docstrings: Making Code Clean

> **Read this before you start the Week 10 homework.** Ada reviews Cave Quest:
> *"Good — now make it clean before we expand it."* Real studios **refactor**
> (improve the structure without changing behavior) before adding features. This
> week you tidy the code the whole party will build on next.
>
> Homework packet: [week10-homework.md](../homework-packets/student/week10-homework.md)

## What you'll learn this week

- What refactoring is and why makers do it.
- How to remove duplicated code by extracting functions.
- How to have functions **return** results instead of printing everything.
- How to document functions with **docstrings**.
- How clearer names and structure improve a program.

## 1. What refactoring means

**Refactoring** is improving *how* code is written without changing *what* it
does. Same output, cleaner insides. You refactor to make code easier to read,
easier to fix, and easier to extend. The output before and after should be
identical.

> Grace's test: *"If the game still behaves the same but is easier to read, the
> refactor worked."*

## 2. Remove duplication by extracting a function

If you find yourself copy-pasting the same lines, pull them into one function and
call it. Before:

```python
# Two nearly identical blocks -- hard to maintain
print("=== Cave Quest ===")
# ... later ...
print("=== Cave Quest ===")
```

After:

```python
def show_intro():
    print("=== Cave Quest ===")

show_intro()
# ... later ...
show_intro()
```

Now the title lives in **one** place. Change it once and every call updates.

## 3. Return results instead of printing everything

A function that **returns** a value is more reusable than one that only prints,
because the caller decides what to do with the result (print it, store it,
compare it). Move logic into a helper that returns:

```python
def play_turn():
    choice = input("Choose left or right: ").strip().lower()
    if choice == "left":
        return "torch"
    return "map"

item = play_turn()          # caller decides what to do
print("You found:", item)
```

The same idea applies to endings that depend on game state — pass the state in
and return the result:

```python
def show_ending(inventory):
    if "map" in inventory:
        return "Explorer rank achieved."
    return "You made it out."

print("Ending:", show_ending(["map"]))
```

## 4. Docstrings: built-in documentation

A **docstring** is a string in triple quotes on the first line inside a function.
It explains what the function does. Unlike a `#` comment, a docstring is attached
to the function and can be read by tools and by `help()`.

```python
def play_turn():
    """Play one turn and return the item the player discovered."""
    choice = input("Choose left or right: ").strip().lower()
    if choice == "left":
        return "torch"
    return "map"
```

Good docstrings are short and say *what* the function does and *what it returns*,
not every line inside it. The whole party can now read your code without
guessing.

## 5. Clearer names and structure

Part of refactoring is renaming for clarity: `play_turn` beats `pt`;
`inventory` beats `x`. Group related steps into functions, and let `main()` call
them in order. When you are done, write down what improved — smaller functions,
no duplication, clearer names — so reviewers can see the value.

## Common mistakes to avoid

- **Changing behavior while refactoring:** the output should match before and
  after. Refactor *or* add features — not both at once.
- **`#` comment vs docstring:** the docstring must be the **first line inside**
  the function, in triple quotes.
- **Over-documenting:** one clear sentence beats a paragraph restating each line.
- **Extracting too aggressively:** pull out repeated or clearly separate logic,
  not every single line.

## Official Python documentation

- Documentation strings (tutorial): <https://docs.python.org/3/tutorial/controlflow.html#documentation-strings>
- Defining functions: <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
- PEP 257 — Docstring conventions: <https://peps.python.org/pep-0257/>

## How this connects to your homework

- **Problem 1** — move your Week 9 intro logic into its own `show_intro()`.
- **Problem 2** — extract choice logic into `play_turn()` that **returns** the
  item found.
- **Problem 3** — move ending logic into `show_ending(inventory)` that picks the
  ending from game state.
- **Problem 4** — add a one-line **docstring** to every function.
- **Problem 5 (`week10_p5_refactor_notes.txt`)** — list at least five concrete
  improvements (duplication removed, clearer names, functions return values, etc.).

## Quick reference

```python
def do_thing(state):
    """One-line summary of what this returns."""   # docstring
    ...
    return result           # prefer returning over only printing

# refactor checklist:
# - no copy-pasted blocks (extract a function)
# - functions return values the caller can use
# - clear names, each function does one job
# - same output as before the refactor
```
