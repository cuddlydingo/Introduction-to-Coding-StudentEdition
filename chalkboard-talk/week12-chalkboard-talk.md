# Week 12 — Planning First: Pseudocode, Flowcharts, and Validation

> **Read this before you start the Week 12 homework.** Ada's rule holds: plan
> before you build. This week you design BranchQuest's quest-select screen with
> **pseudocode** and a **flowchart** before writing a single line of Python — and
> you learn to guard against bad input.
>
> Homework packet: [week12-homework.md](../homework-packets/student/week12-homework.md)
> · Flowchart template: `course-materials/week12-flowchart-template/`

## What you'll learn this week

- What an **algorithm** is.
- How to write **pseudocode** — plain-language steps before code.
- How to draw a **flowchart** of your logic.
- How to **validate** input so bad choices do not break your program.
- How to reason about whether an algorithm is correct.

## 1. What is an algorithm?

An **algorithm** is a step-by-step plan to solve a problem — like a recipe. Good
makers design the algorithm first, then translate it into Python. Planning
catches mistakes while they are still cheap to fix.

## 2. Pseudocode: plan in plain language

**Pseudocode** describes your steps in structured English, ignoring exact Python
syntax so you can focus on the logic. Common keywords: `START`, `GET`, `SHOW`,
`IF ... THEN`, `ELSE`, `END`.

```text
START
SHOW 3 quests
GET choice from user
IF choice is 1, 2, or 3 THEN
    SHOW the matching quest name
ELSE
    SHOW "Invalid choice"
END
```

Every pseudocode plan should have a clear **start**, take **input**, make a
**decision**, produce **output**, and reach an **end**.

## 3. Flowcharts: draw the logic

A **flowchart** is a picture of your algorithm. The standard shapes:

| Shape                | Meaning                        |
| -------------------- | ------------------------------ |
| Rounded box (oval)   | Start or End                   |
| Rectangle            | A process step / action        |
| Diamond              | A decision (a yes/no question) |
| Arrow                | The direction of flow          |

A decision diamond has **two arrows out** (one per answer). Your quest-select
flowchart should flow: **Start -> show quests -> get choice -> decision (valid?)
-> branches -> End**, including the branch for invalid input.

```text
        ┌─────────┐
        │  Start  │
        └────┬────┘
             ▼
     ┌───────────────┐
     │ Show 3 quests │
     └───────┬───────┘
             ▼
     ┌───────────────┐
     │  Get choice   │
     └───────┬───────┘
             ▼
        ◇ valid? ◇──No──► Show "Invalid choice" ─┐
             │Yes                                 │
             ▼                                     │
   Show matching quest ────────────────────────►──┤
                                                   ▼
                                              ┌─────────┐
                                              │   End   │
                                              └─────────┘
```

## 4. Translate the plan into Python

Once the plan is approved, the code follows it closely. A dictionary maps each
valid choice to its quest, and `.get()` supplies the invalid-choice message:

```python
quests = {"1": "Forest Watch", "2": "River Run", "3": "Sky Tower"}
print("1) Forest Watch\n2) River Run\n3) Sky Tower")
choice = input("Choose: ").strip()
print(quests.get(choice, "Invalid choice."))
```

## 5. Validate the input

**Validation** means checking input before you trust it — the Glitch loves
unexpected input. Always give the user a clear message for bad choices instead of
crashing:

```python
if choice in quests:
    print(quests[choice], "selected.")
else:
    print("Invalid choice.")
```

### Reasoning about correctness

To argue your algorithm is correct, show that **every valid input maps to exactly
one output**, and **every invalid input is handled safely**. That is the heart of
the Week 12 write-up: each of choices 1/2/3 gives one quest, and anything else
gives one clear "invalid" message.

## Common mistakes to avoid

- **Coding before planning:** write the pseudocode first; it is faster to fix an
  English step than tangled code.
- **Forgetting the invalid branch:** a decision has *two* outcomes — plan both.
- **Comparing the wrong types:** `input()` returns a string, so compare against
  `"1"`, not `1`.
- **A flowchart with no end:** every path must reach `End`.

## Official Python documentation

- More control flow tools (`if`, loops, structure): <https://docs.python.org/3/tutorial/controlflow.html>
- `dict.get()` for safe lookups: <https://docs.python.org/3/library/stdtypes.html#dict.get>
- The `if` statement (reference): <https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>

## How this connects to your homework

- **Problem 1 (`week12_p1_pseudocode.txt`)** — pseudocode for a 3-choice quest
  selector with `START`, input, branch, output, `END`.
- **Problem 2 (`week12_p2_flowchart.png`)** — a flowchart of that logic, including
  the invalid-input branch.
- **Problem 3 (`week12_p3_quest_selector.py`)** — turn the plan into working code
  for three quests.
- **Problem 4 (`week12_p4_validated_selector.py`)** — add explicit invalid-choice
  handling with a visible message.
- **Problem 5 (`week12_p5_algorithm_explain.txt`)** — explain why each valid input
  maps to exactly one output.

## Quick reference

```text
Pseudocode keywords: START  GET  SHOW  IF ... THEN  ELSE  END
Flowchart shapes:    oval = start/end   rectangle = action   diamond = decision
Validation:          check input is expected; give a clear message if not
Correctness:         one output per valid input + a safe branch for the rest
```
