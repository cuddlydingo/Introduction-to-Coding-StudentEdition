# Week 17 — Capstone Planning: Scope, Design, and QA

> **Read this before you start the Week 17 homework.** Your apprenticeship
> capstone has arrived: design and build **your own** BranchQuest-style game. Ada
> approves your scope and Grace runs QA, just like a real studio heading toward
> launch. This week is about **planning and testing** like an engineer — the
> skills that turn code into a finished project.
>
> Homework packet: [week17-homework.md](../homework-packets/student/week17-homework.md)
> · QA template: `course-materials/week04-test-cases-template/` · Bug triage: `course-materials/week17-bug-triage-sample/`

## What you'll learn this week

- How to **scope** a project: decide what is in and what is out.
- How to design a **function map** so your program is maintainable.
- How to write a **QA test checklist** that catches bugs.
- What a **release candidate** is and how to verify it.
- How to outline a clear showcase presentation.

## 1. Scope: decide what you will (and won't) build

**Scope** is the boundary of your project. With one week to launch, define a
small **goal**, a short list of **features** you will build, and — just as
important — the **non-features** you are deliberately leaving out. A tight scope
you can finish beats a huge scope you cannot.

```text
Goal: Build a playable text adventure with 3 endings.
In scope:   intro screen, 3 choices, inventory, 3 endings, replay
Out of scope: saving to a file, graphics, combat system
```

This is your **MVP** — the minimum version that is still fun and complete.

## 2. Function map: design before you build

A **function map** lists every function you plan to write, with its input, output,
and one-line purpose. It is the blueprint another maker could use to maintain your
game — and it keeps you organized while you build.

```text
show_intro():            displays game title and start prompt
play_turn(inventory):    asks a choice, updates inventory, returns item found
show_ending(inventory):  picks an ending based on what was collected
main():                  runs intro, loops turns, shows ending, offers replay
```

You already have the tools for each of these from Weeks 6-11 (functions, loops,
lists, dictionaries).

## 3. QA: a test checklist

**QA (quality assurance)** means checking your program behaves correctly *before*
showcase day. Good test cases cover three categories:

- **Happy path** — normal, expected input works.
- **Invalid input** — bad input gets a clear message, not a crash.
- **Boundaries** — edge values (empty input, the first/last choice, very large
  numbers).

```text
Test 1  (happy)    : choosing "left" adds the torch          -> pass
Test 2  (invalid)  : typing "banana" at the menu             -> shows "Invalid choice"
Test 3  (boundary) : pressing Enter with no input            -> no crash
Test 4  (happy)    : replay "yes" restarts the game          -> pass
Test 5  (invalid)  : letters where a number is expected      -> handled, no crash
```

Aim for at least ten test cases. Writing tests as a checklist means you can rerun
them every time you change the code.

## 4. Release candidate

A **release candidate** is a near-final build you believe is ready. Verify it by
running the program start to finish with no crashes, checking every menu path, and
confirming it meets your scope. Grace's rule: *"If a stranger can play it without
you standing next to them, it's ready."*

## 5. Showcase outline

Plan your demo before you present. A clear five-slide flow keeps you calm:

```text
Slide 1: The problem and your idea
Slide 2: Program structure (your function map)
Slide 3: Live demo of a key feature
Slide 4: A challenge you solved
Slide 5: What you learned / next steps
```

## Common mistakes to avoid

- **Scope creep:** adding features mid-week until nothing is finished. Lock your
  scope, then build.
- **Testing only the happy path:** most bugs hide in invalid and boundary input.
- **No function map:** unplanned code becomes tangled and hard to demo.
- **Skipping the full run-through:** always play the whole game before calling it
  a release candidate.

## Official documentation

- Errors and exceptions (the testing mindset): <https://docs.python.org/3/tutorial/errors.html>
- Defining functions (for your function map): <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>
- The Python tutorial (review any construct you need): <https://docs.python.org/3/tutorial/index.html>
- `unittest` — how professionals automate tests (enrichment): <https://docs.python.org/3/library/unittest.html>

## How this connects to your homework

- **Problem 1 (`week17_p1_scope.md`)** — goal, in-scope features, out-of-scope
  non-features.
- **Problem 2 (`week17_p2_functions.md`)** — a function map: name, purpose, input,
  output.
- **Problem 3 (`week17_p3_test_checklist.md`)** — at least ten test cases across
  happy, invalid, and boundary categories.
- **Problem 4 (`week17_p4_near_final/`)** — a release candidate that runs start to
  finish.
- **Problem 5 (`week17_p5_slides_outline.md`)** — a five-slide showcase structure.

## Quick reference

```text
Scope:        goal + in-scope features + out-of-scope non-features (your MVP)
Function map: name(input) -> output : one-line purpose
QA tests:     happy path · invalid input · boundaries (aim for 10+)
Release:      run end-to-end, no crashes, every path checked, meets scope
Showcase:     problem -> design -> demo -> challenge -> lesson
```
