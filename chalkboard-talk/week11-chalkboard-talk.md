# Week 11 — Dictionaries: Storing Pairs of Data

> **Read this before you start the Week 11 homework.** BranchQuest needs to know
> its heroes. This week you build the party roster as a **dictionary** — and a
> fifth apprentice, Nova the knight, joins the Guild.
>
> Homework packet: [week11-homework.md](../homework-packets/student/week11-homework.md)

## What you'll learn this week

- What a dictionary is and how it differs from a list.
- How to create a dictionary of **key/value** pairs.
- How to add and update entries.
- How to look up a value safely, including missing keys.
- How to loop over all pairs with `.items()`.

## 1. What is a dictionary?

A **dictionary** stores **key -> value** pairs. Where a list finds items by
*position* (`items[0]`), a dictionary finds them by a meaningful *key*
(`roster["aria"]`). Think of a real dictionary: you look up a **word** (key) to
get its **definition** (value).

```python
roster = {"aria": "archer", "dax": "healer", "lina": "mage", "timo": "scout"}
print(roster)
```

- Curly braces `{}` wrap the dictionary.
- Each pair is `key: value`.
- Pairs are separated by commas.

## 2. Look up a value by key

Use square brackets with the key to read a value:

```python
print(roster["lina"])     # mage
```

But asking for a key that does not exist raises a `KeyError`. The safe way is
`.get()`, which returns a default instead of crashing:

```python
print(roster.get("nova", "not found"))   # not found
```

You can also test membership with `in`:

```python
name = input("Lookup name: ").strip().lower()
if name in roster:
    print("Role:", roster[name])
else:
    print("Role: not found")
```

## 3. Add or update an entry

Assigning to a key adds it if new, or updates it if it already exists:

```python
roster["nova"] = "knight"     # Nova joins the party
roster["timo"] = "ranger"     # Timo changes role (same key -> updated)
print("Added: nova ->", roster["nova"])
```

There is only ever **one** value per key, so assigning to an existing key
replaces the old value.

## 4. Loop over every pair with `.items()`

`.items()` gives you both the key and the value on each pass, perfect for
printing a full roster:

```python
for name, role in roster.items():
    print(f"{name}: {role}")
```

```text
aria: archer
dax: healer
lina: mage
timo: scout
```

(Related helpers: `.keys()` loops over just the keys, `.values()` over just the
values.)

## 5. Building a menu app

Combine a dictionary with the Week 5 loop and Week 4 branching to make a small
menu program — the shape of the party-book app:

```python
roster = {}
while True:
    print("1) Add  2) Lookup  3) List  4) Quit")
    choice = input("Choice: ").strip()
    if choice == "1":
        name = input("Name: ").strip().lower()
        role = input("Role: ").strip().lower()
        roster[name] = role
    elif choice == "2":
        name = input("Name: ").strip().lower()
        print(roster.get(name, "not found"))
    elif choice == "3":
        for name, role in roster.items():
            print(f"{name}: {role}")
    else:
        break
```

## Common mistakes to avoid

- **`KeyError` on a missing key:** use `.get(key, default)` or check `key in dict`
  first.
- **Expecting duplicate keys:** each key is unique; a second assignment overwrites
  the first.
- **Mixing up keys and values:** you look things up *by key*, and each key points
  to one value.
- **Looping wrong:** `for x in roster` gives you the **keys**; use
  `for k, v in roster.items()` to get both.

## Official Python documentation

- Dictionaries (tutorial): <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>
- Mapping type `dict`: <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>
- `dict.get()`: <https://docs.python.org/3/library/stdtypes.html#dict.get>
- `dict.items()`: <https://docs.python.org/3/library/stdtypes.html#dict.items>

## How this connects to your homework

- **Problem 1 (`week11_p1_dict_basics.py`)** — create a dictionary with at least
  four name/role pairs.
- **Problem 2 (`week11_p2_update_dict.py`)** — add or update one entry (recruit
  Nova).
- **Problem 3 (`week11_p3_lookup.py`)** — look up a role and handle a missing key
  with `.get()` or `in`.
- **Problem 4 (`week11_p4_iterate.py`)** — print every `name: role` line with
  `.items()`.
- **Problem 5 (`week11_p5_character_book.py`)** — a menu app with add, lookup, and
  list options.

## Quick reference

```python
d = {"key": "value"}     # create
d["key"]                 # read (KeyError if missing)
d.get("key", "default")  # safe read
d["new"] = "value"       # add or update
"key" in d               # membership test
for k, v in d.items():   # loop over pairs
    print(k, v)
```
