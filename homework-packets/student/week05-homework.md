# Week 5 Homework Packet

> **Story so far:** The party trains for the road ahead. Loops let heroes repeat
> drills — and let the Guild vault keep asking until the right code is entered,
> no matter how many times Timo guesses wrong.

**Quest branch:** Work on a branch named `quest/week05-training-loops`. When the
quest is done, open a merge request titled
`Week 05 - Firstname Lastname - Training Loops` and request review before
merging. New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Training-rep counter

**Setup:** The party runs training reps out loud.
Create `week05_p1_count.py` that prints numbers from 1 to N.

### Example stdout

```text
N: 5
1
2
3
4
5
```

## Problem 2 - Even-energy crystals

**Setup:** BranchQuest grants bonus energy on even-numbered levels.
Create `week05_p2_even.py` that prints even numbers from 2 to N.

### Example stdout

```text
N: 10
2
4
6
8
10
```

## Problem 3 - Lina's spellbook drills

**Setup:** Lina memorizes a times table to power her spells.
Create `week05_p3_table.py` for one chosen number (1-12).

### Example stdout

```text
Number: 3
3 x 1 = 3
3 x 2 = 6
...
3 x 12 = 36
```

## Problem 4 - Vault retry loop

**Setup:** To keep the Glitch out, the vault keeps asking until the correct passcode is entered.
Create `week05_p4_retry_password.py` that loops until correct password.

### Example stdout

```text
Password: cat
Try again
Password: dog
Try again
Password: lion
Access granted
```

## Problem 5 - Number-hunter puzzle

**Setup:** A BranchQuest puzzle hides a secret number for players to hunt.
Create `week05_p5_guess.py` with a fixed target number.

### Example stdout

```text
Guess: 7
Too low
Guess: 11
Correct
```

## Level up (optional)

- **Side-quest:** give Timo only three vault attempts using a counter, then lock him out.
- **Stuck?** a `while True:` loop needs a `break`; make sure the correct-answer branch breaks.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
