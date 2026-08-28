# Week 7 Homework Packet

> **Story so far:** Every adventure needs an inventory and readable messages.
> You build the systems that let heroes carry items — and decode a note the
> Glitch scrambled backwards.

**Quest branch:** Work on a branch named `quest/week07-inventory-text`. When the
quest is done, open a merge request titled
`Week 07 - Firstname Lastname - Inventory and Text` and request review before
merging. New to branches? See
[github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md).

## Problem 1 - Decode the scrambled message

**Setup:** The Glitch left a message backwards. Reverse the text to read it.
Create `week07_p1_reverse.py` to reverse input text.

### Example stdout

```text
Text: code
Reversed: edoc
```

## Problem 2 - Rune counter

**Setup:** Lina counts the vowel-runes hidden in words of power.
Create `week07_p2_vowels.py` that counts vowels (a,e,i,o,u) in:
`banana`, `octopus`, `gerbil`, `horse`, `onomatopoeia`.
For a bonus, show how to include `y` as a vowel.

### Example stdout

```text
banana -> 3
octopus -> 3
gerbil -> 2
horse -> 2
onomatopoeia -> 8
Bonus (including y): mystery -> 2
```

## Problem 3 - Provision pack

**Setup:** Dax loads the party's pack before setting out.
Create `week07_p3_shopping.py` to collect 5 items in list.

### Example stdout

```text
Item 1: milk
Item 2: bread
Item 3: eggs
Item 4: apples
Item 5: rice
Final list: ['milk', 'bread', 'eggs', 'apples', 'rice']
```

## Problem 4 - Top-score finder

**Setup:** Peek at the BranchQuest leaderboard and find the highest score.
Create `week07_p4_largest.py` from a fixed list.

### Example stdout

```text
Numbers: [3, 9, 2, 14, 7]
Largest: 14
```

## Problem 5 - Inventory screen

**Setup:** Number the backpack so teammates can call out items fast.
Create `week07_p5_numbered_list.py` using `enumerate`.

### Example stdout

```text
1. map
2. torch
3. rope
```

## Level up (optional)

- **Side-quest:** also print your inventory in reverse using slicing `[::-1]`.
- **Stuck?** list indexes start at 0, so `items[0]` is the first item.
- **Self-check:** before opening your merge request, run your code and compare it to the Example output above; for a written piece, reread the prompt and confirm you covered every part.
