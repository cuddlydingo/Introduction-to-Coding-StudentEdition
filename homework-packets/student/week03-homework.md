# Week 3 Homework Packet

> **Story so far:** BranchQuest needs math it can trust. Grace, the Guild's
> Chief Bug-Hunter, warns that sloppy arithmetic is exactly the kind of crack
> the Glitch slips through — so every calculation must be exact.

**Quest branch:** Work on a branch named `quest/week03-score-systems`. When the
quest is done, open a merge request titled
`Week 03 - Firstname Lastname - Score Systems` and request review before
merging. New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Quest score math

**Setup:** Two heroes finish a quest with points to combine.
Create `week03_p1_math.py` that asks two numbers and prints sum and product.

### Example stdout

```text
First number: 4
Second number: 6
Sum: 10
Product: 24
```

## Problem 2 - Sparring-match comparison

**Setup:** Aria and Timo spar to see who scored higher.
Create `week03_p2_compare.py` that asks two numbers and prints whether first is greater.

### Example stdout

```text
First number: 9
Second number: 5
First > Second: True
```

## Problem 3 - Gate permission logic

**Setup:** A guarded gate opens only if a hero is old enough AND has a permission token.
Create `week03_p3_logic.py` that asks age and permission (`yes/no`) and prints if allowed.

### Example stdout

```text
Age: 14
Permission (yes/no): yes
Allowed: True
```

## Problem 4 - Provisioning planner

**Setup:** Dax packs rations before a long quest.
Create `week03_p4_snacks.py` (players * snacks each).

### Example stdout

```text
Players: 6
Snacks each: 3
Total snacks: 18
```

## Problem 5 - Climate converter

**Setup:** Heroes travel between the hot and cold regions of BranchQuest.
Create `week03_p5_temp.py` for Fahrenheit to Celsius.

### Example stdout

```text
Fahrenheit: 68
Celsius: 20.0
```

## Level up (optional)

- **Side-quest:** also print integer division `//` and remainder `%`, each with a label.
- **Stuck?** convert inputs with `int(...)` or `float(...)` before doing math, or you will add text.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
