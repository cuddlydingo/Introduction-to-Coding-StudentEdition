# Week 15 Homework Packet

> **Story so far:** Players want to save their progress. You build BranchQuest's
> mission-log system, reading and writing the Guild's `missions.txt` records.

**Quest branch:** Work on a branch named `quest/week15-save-system`. When the
quest is done, open a merge request titled
`Week 15 - Firstname Lastname - Save System` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Read the mission log

**Setup:** BranchQuest writes mission status lines to a file.
Create `week15_p1_read_lines.py` counting non-empty lines in `missions.txt`.
Use the provided file from `course-materials/week15-file-inputs/missions.txt`.

### Example stdout

```text
Non-empty lines: 5
```

## Problem 2 - Completion counter

**Setup:** The Guild wants progress totals: complete vs incomplete missions.
Create `week15_p2_count_complete.py` counting `complete` entries.
Use the provided file from `course-materials/week15-file-inputs/missions.txt`.

### Example stdout

```text
Completed: 3
Incomplete: 2
```

## Problem 3 - Summary writer

**Setup:** Automate a mission summary report for the Guild.
Create `week15_p3_write_summary.py` writing totals to `summary.txt`.

### Example stdout

```text
Summary written to summary.txt
```

## Problem 4 - Full report pipeline

**Setup:** Build one script that reads the log, counts, prints, and saves.
Create `week15_p4_report.py` doing read + count + write.
Use the provided file from `course-materials/week15-file-inputs/missions.txt`.

### Example stdout

```text
Total missions: 5
Completed: 3
Incomplete: 2
```

## Problem 5 - Save-system reflection

**Setup:** Document what you learned about working with files.
Create `week15_p5_reflection.txt` with 5 lessons learned.

### Example output target

```text
Lesson 1: Always strip newline characters.
```

## Level up (optional)

- **Side-quest:** guard the read with `try`/`except FileNotFoundError` so a missing `missions.txt` prints a friendly message.
- **Stuck?** run your script from the folder that holds `missions.txt`, or open it with a full path; a bare filename looks in the current working directory.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
