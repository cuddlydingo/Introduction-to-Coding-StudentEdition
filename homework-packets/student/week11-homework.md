# Week 11 Homework Packet

> **Story so far:** BranchQuest needs to know its heroes. You build the party
> roster as a dictionary — and a fifth apprentice, Nova the knight, officially
> joins the Guild.

**Quest branch:** Work on a branch named `quest/week11-party-roster`. When the
quest is done, open a merge request titled
`Week 11 - Firstname Lastname - Party Roster` and request review before merging.
New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Party database

**Setup:** Store the party in a dictionary of name/role pairs: Aria, Dax, Lina, Timo.
Create `week11_p1_dict_basics.py` with at least 4 key/value pairs.

### Example stdout

```text
{'aria': 'archer', 'dax': 'healer', 'lina': 'mage', 'timo': 'scout'}
```

## Problem 2 - Recruit Nova

**Setup:** A new knight, Nova, joins the party.
Create `week11_p2_update_dict.py` to add or update one entry.

### Example stdout

```text
Added: nova -> knight
```

## Problem 3 - Role lookup tool

**Setup:** Quickly check any hero's role before a mission.
Create `week11_p3_lookup.py` and handle missing key.

### Example stdout

```text
Lookup name: lina
Role: mage
```

## Problem 4 - Roster printout

**Setup:** Print the whole party for mission planning.
Create `week11_p4_iterate.py` printing all `name: role` lines.

### Example stdout

```text
aria: archer
dax: healer
```

## Problem 5 - Party book app

**Setup:** Build a menu app to manage the party book.
Create `week11_p5_character_book.py` with add + lookup + list options.

### Example stdout

```text
1) Add
2) Lookup
3) List
Choice: 3
aria: archer
```

## Level up (optional)

- **Side-quest:** add a "remove hero" option to the menu using `del` or `.pop()`.
- **Stuck?** check `if name in party:` before reading `party[name]` to avoid a KeyError.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
