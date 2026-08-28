# Week 9 Homework Packet

> **Story so far:** The Glitch is beaten back, and it is time to ship the first
> playable chapter of BranchQuest: **Cave Quest**. Build it end to end and demo
> it for Ada and the party.

**Quest branch:** Work on a branch named `quest/week09-cave-quest`. When the
quest is done, open a merge request titled
`Week 09 - Firstname Lastname - Cave Quest` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Cave Quest intro scene

**Setup:** Chapter 1 of BranchQuest opens in the Cave and needs a strong opening.
Create `week09_p1_intro_function.py` with `show_intro()`.

### Example stdout

```text
Welcome to Cave Quest!
```

## Problem 2 - First major choice

**Setup:** Give players a branch that changes what they find in the Cave.
Create `week09_p2_choice.py` with two choices and outcomes.

### Example stdout

```text
Choose left or right: left
You found a torch.
```

## Problem 3 - Inventory tracker

**Setup:** Track what players collect as they explore the Cave.
Create `week09_p3_inventory.py` adding found items to list.

### Example stdout

```text
Inventory: ['torch', 'coin']
```

## Problem 4 - Replay mode

**Setup:** Let players try different paths through the Cave until they stop.
Create `week09_p4_replay.py` to replay until user says no.

### Example stdout

```text
Play again? yes
Play again? no
Thanks for playing.
```

## Problem 5 - Playable Cave Quest

**Setup:** Combine intro, choice, inventory, and replay into one playable chapter to demo.
Create `week09_p5_checkpoint_game.py` combining all above.

### Example stdout

```text
Welcome to Cave Quest!
Choose path: right
You found a map.
Play again? no
Final inventory: ['map']
```

## Level up (optional)

- **Side-quest:** add a second choice point so the Cave has at least two branches and two endings.
- **Stuck?** build one piece at a time (intro, choice, inventory) and test each before combining.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
