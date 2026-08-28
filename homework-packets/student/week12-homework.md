# Week 12 Homework Packet

> **Story so far:** Ada's rule holds: plan before you build. You design
> BranchQuest's quest-select screen with pseudocode and a flowchart before
> writing a single line of code.

**Quest branch:** Work on a branch named `quest/week12-quest-design`. When the
quest is done, open a merge request titled
`Week 12 - Firstname Lastname - Quest Design` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Quest-select pseudocode

**Setup:** Ada approves logic before coding starts.
Write `week12_p1_pseudocode.txt` for a 3-choice quest selector.

### Example output target

```text
START
SHOW 3 quests
GET choice
IF choice valid THEN show result
END
```

## Problem 2 - Quest-select flowchart

**Setup:** Draw the decision logic so the whole party can see the branches.
Create `week12_p2_flowchart.png` for that logic.

### Example output target

```text
Flowchart has Start -> Choice -> Branches -> End
```

## Problem 3 - Build the quest selector

**Setup:** Turn your approved plan into working Python for three quests.
Create `week12_p3_quest_selector.py` from pseudocode.

### Example stdout

```text
1) Forest Watch
2) River Run
3) Sky Tower
Choose: 2
River Run selected.
```

## Problem 4 - Guard against bad input

**Setup:** The Glitch loves unexpected input, so handle invalid choices safely.
Create `week12_p4_validated_selector.py` with invalid-choice handling.

### Example stdout

```text
Choose: 9
Invalid choice.
```

## Problem 5 - Prove it is correct

**Setup:** Explain to Ada why your selector gives exactly one result per valid choice.
Create `week12_p5_algorithm_explain.txt` describing correctness.

### Example output target

```text
The algorithm is correct because each valid input maps to exactly one output...
```

## Level up (optional)

- **Side-quest:** add a fourth quest and update both the pseudocode and the flowchart to match.
- **Stuck?** every path through your flowchart should reach exactly one printed result, including the invalid case.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
