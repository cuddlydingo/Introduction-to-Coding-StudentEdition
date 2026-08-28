# Week 9 — Putting It Together: Build a Playable Text Adventure

> **Read this before you start the Week 9 homework.** The Glitch is beaten back
> and it is time to ship the first playable chapter of BranchQuest: **Cave
> Quest**. This week you do not learn one new idea — you *combine* everything
> from Weeks 1-8 into a real, playable program.
>
> Homework packet: [week09-homework.md](../homework-packets/student/week09-homework.md)

## What you'll learn this week

- How to combine functions, input, `if/else`, loops, and lists into one program.
- How to structure a small game: intro, choices, inventory, replay.
- How to keep game state (the inventory) as the player plays.

This is an **integration** week. Skim the earlier chalkboard talks if any tool
below feels rusty:
[functions (Week 6)](week06-chalkboard-talk.md),
[loops (Week 5)](week05-chalkboard-talk.md),
[decisions (Week 4)](week04-chalkboard-talk.md),
[lists (Week 7)](week07-chalkboard-talk.md).

## 1. An intro scene as a function

Wrap your opening in a function so `main()` can call it. Functions keep each part
of the game named and separate:

```python
def show_intro():
    print("Welcome to Cave Quest!")

show_intro()
```

## 2. A choice that branches the story

Use `input()` plus `if/else` to let the player's choice change what happens. Tidy
the input with `.strip().lower()` so `"Left"` and `" left "` still work:

```python
choice = input("Choose left or right: ").strip().lower()
if choice == "left":
    print("You found a torch.")
else:
    print("You found a map.")
```

## 3. An inventory with a list

Track what the player collects in a list, adding to it with `.append()`:

```python
inventory = []
inventory.append("torch")
inventory.append("coin")
print("Inventory:", inventory)     # Inventory: ['torch', 'coin']
```

The inventory is your game's **state** — information that changes as the player
plays. Create it once, then update it as they explore.

## 4. A replay loop

Let players try different paths with a `while` loop that repeats until they say
no (the `while True` + `break` pattern from Week 5):

```python
while True:
    again = input("Play again? ").strip().lower()
    if again == "no":
        print("Thanks for playing.")
        break
```

## 5. Assembling the whole chapter

A playable chapter combines all four pieces. Here is the *shape* of a program
that uses functions, branching, a loop, and a list together — fill in your own
scenes and items:

```python
def show_intro():
    print("Welcome to Cave Quest!")

def play_once():
    inventory = []
    path = input("Choose path: ").strip().lower()
    if path == "right":
        inventory.append("map")
    else:
        inventory.append("torch")
    print("Final inventory:", inventory)

def main():
    show_intro()
    while True:
        play_once()
        again = input("Play again? ").strip().lower()
        if again == "no":
            print("Thanks for playing.")
            break

main()
```

Notice how each Week 1-8 skill has a job: `print()` for messages, `input()` for
choices, `if/else` for branching, a list for the inventory, a `while` loop for
replay, and functions to keep it organized.

## Common mistakes to avoid

- **One giant block of code:** break the game into small functions with clear
  names; it is far easier to debug.
- **Losing the inventory:** create `inventory = []` once, in the right place —
  not inside a loop that would reset it every turn.
- **Replay never ends (or ends instantly):** make sure your `break` condition
  matches exactly what you tell the player to type.
- **Unhandled choices:** decide what happens when a player types something
  unexpected (an `else` branch is a safe default).

## Official Python documentation

- More control flow tools (functions, `if`, loops): <https://docs.python.org/3/tutorial/controlflow.html>
- Data structures (lists): <https://docs.python.org/3/tutorial/datastructures.html>
- Input and output: <https://docs.python.org/3/tutorial/inputoutput.html>

## How this connects to your homework

- **Problem 1 (`week09_p1_intro_function.py`)** — a `show_intro()` function.
- **Problem 2 (`week09_p2_choice.py`)** — one branch with two outcomes.
- **Problem 3 (`week09_p3_inventory.py`)** — a list you `.append()` items to.
- **Problem 4 (`week09_p4_replay.py`)** — a `while` loop that replays until the
  player says no.
- **Problem 5 (`week09_p5_checkpoint_game.py`)** — combine intro, choice,
  inventory, and replay into one runnable chapter to demo.

## Quick reference

```python
def show_intro():           # scene as a function
    print("Welcome!")

choice = input("...").strip().lower()   # tidy input
if choice == "left":        # branch the story
    ...

inventory = []              # game state
inventory.append("torch")   # collect items

while True:                 # replay loop
    ...
    if again == "no":
        break
```
