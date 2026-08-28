# Week 2 Homework Packet

> **Story so far:** Ada introduces your apprentice party — Aria, Dax, Lina, and
> Timo — the heroes you will bring to life in BranchQuest. Lina, who loves data,
> shows you how the game stores information.

**Quest branch:** Work on a branch named `quest/week02-party-profiles`. When the
quest is done, open a merge request titled
`Week 02 - Firstname Lastname - Party Profiles` and request review before
merging. New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Party greeter bot

**Setup:** BranchQuest greets each hero by name. Build the greeter that asks for
a name and welcomes the player.
Create `week02_p1_name_card.py` that asks name and prints greeting.

### Example stdout

```text
Enter your name: Alex
Hello, Alex!
```

## Problem 2 - Type detective with Lina

**Setup:** Lina explains that the game tracks different kinds of data. Play data
detective and label each value's type.
Create `week02_p2_types.py` with int, float, string, bool variables and print each type.

### Example stdout

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Problem 3 - Time-scroll age checker

**Setup:** A time-scroll artifact shows a hero one year older.
Create `week02_p3_age_next_year.py` that asks age and prints age+1.

### Example stdout

```text
Enter your age: 13
Next year you will be 14
```

## Problem 4 - Party favorites wall

**Setup:** Get to know your party. Collect three favorites and print a summary
card for the Guild wall.
Create `week02_p4_favorites.py` that asks 3 favorites and prints a summary.

### Example stdout

```text
Favorite color: blue
Favorite game: chess
Favorite snack: popcorn
Summary: blue, chess, popcorn
```

## Problem 5 - Hero profile card

**Setup:** Every hero in BranchQuest needs a character sheet. Print a formatted
profile with name, age, and hobby.
Create `week02_p5_profile_card.py` with name, age, hobby and formatted output.

### Example stdout

```text
Name: Alex
Age: 13
Hobby: Soccer
```

## Level up (optional)

- **Side-quest:** add a fourth input (favorite number) and print its `type()` too.
- **Stuck?** `input()` always returns a string; wrap it in `int(...)` only when you need a number.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
