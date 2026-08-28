# Week 6 Homework Packet

> **Story so far:** Ada teaches the maker's golden rule: build tools you can
> reuse, not one-off scripts. Today you forge the Guild's first shared
> functions.

**Quest branch:** Work on a branch named `quest/week06-reusable-tools`. When the
quest is done, open a merge request titled
`Week 06 - Firstname Lastname - Reusable Tools` and request review before
merging. New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Your first reusable tool

**Setup:** The Guild needs an add tool every maker can reuse.
Create `week06_p1_add_function.py` with `add(a, b)`.

### Example stdout

```text
add(3, 4) -> 7
```

## Problem 2 - Room-builder helper

**Setup:** BranchQuest's map needs its rooms measured.
Create `week06_p2_area.py` with `rectangle_area(length, width)`.

### Example stdout

```text
rectangle_area(5, 2) -> 10
```

## Problem 3 - Even-key utility

**Setup:** Some BranchQuest doors accept only even keys.
Create `week06_p3_is_even.py` with `is_even(n)`.

### Example stdout

```text
is_even(8) -> True
is_even(7) -> False
```

## Problem 4 - Greeting forge

**Setup:** Turn the game's greeter into a reusable function for any hero.
Create `week06_p4_greeting.py` with function parameter for name.

### Example stdout

```text
greet("Alex") -> Hello, Alex!
```

## Problem 5 - Maker's command center

**Setup:** Assemble your tools into one toolkit run from a `main()`.
Create `week06_p5_main_program.py` that calls at least 3 functions.

### Example stdout

```text
Sum: 9
Area: 12
Even check: True
```

## Level up (optional)

- **Side-quest:** add `assert add(2, 3) == 5` under your function to prove it works.
- **Stuck?** a function only gives back a value if it uses `return`; printing inside is not the same.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
