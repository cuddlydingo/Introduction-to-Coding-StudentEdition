# Week 15 — Working with Files: Reading and Writing

> **Read this before you start the Week 15 homework.** Players want to save their
> progress. This week you build BranchQuest's mission-log system, **reading** and
> **writing** the Guild's `missions.txt` records.
>
> Homework packet: [week15-homework.md](../homework-packets/student/week15-homework.md)
> · Provided data: `course-materials/week15-file-inputs/missions.txt`

## What you'll learn this week

- How to open a file with `open()` and the `with` statement.
- File **modes**: read (`"r"`) and write (`"w"`).
- How to read a file line by line.
- Why you need `.strip()` to remove newline characters.
- How to write results back to a file.

## 1. Opening a file the safe way

`open()` connects your program to a file. The best practice is to use it with a
`with` block, which **automatically closes** the file when you are done — even if
something goes wrong:

```python
with open("missions.txt", "r", encoding="utf-8") as f:
    contents = f.read()
print(contents)
```

- `"missions.txt"` is the file name.
- `"r"` is the **mode** (read).
- `encoding="utf-8"` tells Python how the text is stored (a safe default).
- `as f` names the open file `f` so you can use it inside the block.

## 2. File modes

| Mode  | Meaning | Notes                             |
| ----- | ------- | --------------------------------- |
| `"r"` | read    | Error if the file does not exist. |
| `"w"` | write   | Creates the file, or erases it.   |
| `"a"` | append  | Adds to the end without erasing.  |

Use `"r"` to read the mission log and `"w"` to save a summary.

## 3. Reading line by line

Looping over an open file gives you one line at a time. Each line includes a
hidden newline character (`\n`) at the end, so use `.strip()` to remove
surrounding whitespace:

```python
with open("missions.txt", "r", encoding="utf-8") as f:
    for line in f:
        clean = line.strip()      # remove the trailing newline and spaces
        print(clean)
```

### Counting non-empty lines

A common task is counting only the lines that have content. Skip blank lines by
testing the stripped text:

```python
with open("missions.txt", "r", encoding="utf-8") as f:
    lines = [line for line in f if line.strip()]
print("Non-empty lines:", len(lines))
```

### Counting entries by content

If each line looks like `Rescue,complete`, you can count how many end with
`complete`:

```python
with open("missions.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
complete = sum(1 for line in lines if line.endswith("complete"))
print("Completed:", complete)
print("Incomplete:", len(lines) - complete)
```

## 4. Writing to a file

Open in write mode and use `.write()`. Note that `.write()` does **not** add a
newline for you — include `\n` yourself:

```python
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write("Total missions: 5\n")
    f.write("Completed: 3\n")
print("Summary written to summary.txt")
```

A full report pipeline **reads** the log, **counts** the entries, **prints** the
totals, and **writes** them to a new file — combining everything above.

## Common mistakes to avoid

- **Forgetting `.strip()`:** leftover `\n` characters cause mismatched
  comparisons and messy output.
- **Using `"w"` when you meant `"r"`:** write mode **erases** the file first — you
  could wipe your data.
- **Not closing the file:** the `with` block handles this for you; prefer it over
  a bare `open()`.
- **Wrong working folder:** run your script from the folder that contains
  `missions.txt`, or the file will not be found.

## Official Python documentation

- Reading and writing files (tutorial): <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>
- The `open()` function: <https://docs.python.org/3/library/functions.html#open>
- The `with` statement (reference): <https://docs.python.org/3/reference/compound_stmts.html#the-with-statement>
- `str.strip()` and other string methods: <https://docs.python.org/3/library/stdtypes.html#str.strip>

## How this connects to your homework

- **Problem 1 (`week15_p1_read_lines.py`)** — count non-empty lines in
  `missions.txt`.
- **Problem 2 (`week15_p2_count_complete.py`)** — count complete vs incomplete
  entries.
- **Problem 3 (`week15_p3_write_summary.py`)** — write totals to `summary.txt`.
- **Problem 4 (`week15_p4_report.py`)** — one script that reads, counts, prints,
  and writes.
- **Problem 5 (`week15_p5_reflection.txt`)** — five lessons learned (modes,
  stripping newlines, error handling, etc.).

## Quick reference

```python
with open("file.txt", "r", encoding="utf-8") as f:   # read
    for line in f:
        clean = line.strip()

with open("out.txt", "w", encoding="utf-8") as f:     # write (erases first!)
    f.write("text\n")

len([l for l in lines if l.strip()])   # count non-empty lines
line.endswith("complete")              # test how a line ends
```
