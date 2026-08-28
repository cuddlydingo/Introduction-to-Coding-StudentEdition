# Week 4 Homework Packet

> **Story so far:** Ada reveals the heart of BranchQuest: choices. Today you
> build the branching gates that make every player's path different — the very
> branches the game is named for.

**Quest branch:** Work on a branch named `quest/week04-decision-gates`. When the
quest is done, open a merge request titled
`Week 04 - Firstname Lastname - Decision Gates` and request review before
merging. New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Apprentice trial checker

**Setup:** New apprentices must pass a trial: score 70 or higher passes.
Create `week04_p1_pass_fail.py`: score >= 70 => pass else fail.

### Example stdout

```text
Score: 82
Result: Pass
```

## Problem 2 - Gatekeeper classifier

**Setup:** A gatekeeper sorts travelers into entry tiers by age.
Create `week04_p2_ticket.py`: child (<13), teen (13-17), adult (18+).

### Example stdout

```text
Age: 15
Ticket type: Teen
```

## Problem 3 - Traveler's advisor

**Setup:** Before crossing a region, heroes need advice on what to wear.
Create `week04_p3_weather.py` using temp and rain input.

### Example stdout

```text
Temperature: 55
Raining? (yes/no): yes
Advice: Wear a jacket and bring an umbrella.
```

## Problem 4 - Level gate

**Setup:** A hero reaches a locked gate deep inside BranchQuest.
Create `week04_p4_level_gate.py` with 3 branches.

### Example stdout

```text
Level: 4
Gate status: Locked
```

## Problem 5 - Guild vault passcode

**Setup:** The Guild vault opens only with the correct passcode.
Create `week04_p5_password_check.py` that compares input to a stored password.

### Example stdout

```text
Enter password: tiger123
Access granted
```

## Level up (optional)

- **Side-quest:** block a Glitch by rejecting impossible input (like a negative age) with a friendly message before the branches.
- **Stuck?** only the first true branch runs; order `if/elif` from most specific to least.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
