# Weekly Homework Problems (Student Version)

These assignments are designed for GitHub submission and build skills step-by-step across the semester. They follow one connected story, **BranchQuest: The Apprentice Maker's Chronicle** — you are a new apprentice at a game-maker's guild helping build a class text adventure, and by the final weeks you ship a game of your own. Each week you check out a **quest branch**, complete the work, and open a **merge request** for review. See [../lesson-plans/github-workflow-and-submission.md](../lesson-plans/github-workflow-and-submission.md) for the branch and merge-request steps. Each weekly packet also ends with an optional **Level up** — a side-quest stretch, a hint if you get stuck, and a self-check to run before you submit.

## Week 1

> **Story so far:** Welcome to the Maker's Guild! Guildmaster Ada hands you an
> apprentice's bench and your first work orders. Today you set up your maker's
> tools and record who you are. Your **apprentice name is the GitHub username you
> choose this week** — you will carry it through every quest all semester.

### Problem 1 - Hello, future maker

**Setup:** Ada asks every new apprentice to write the Guild's welcome banner —
the first screen players see when they open BranchQuest.
Create `week01_p1_hello.py` that prints a course welcome message.

#### Example stdout

```text
Welcome to Introduction to Coding!
```

### Problem 2 - Apprentice badge

**Setup:** Every maker gets a badge for the Guild roster. Use your apprentice
name (your GitHub username) on the badge.
Create `week01_p2_intro.py` that prints your name and grade.

#### Example stdout

```text
Name: Alex Student
Grade: 8
```

### Problem 3 - Apprentice's goals

**Setup:** Ada wants to know what you hope to build during your apprenticeship.
Create `week01_p3_goals.py` that prints 3 coding goals.

#### Example stdout

```text
Goal 1: Learn Python basics
Goal 2: Build a text game
Goal 3: Improve debugging skills
```

### Problem 4 - Field notes

**Setup:** Makers leave notes for their future selves. Add comments so you
remember why each line matters.
Create `week01_p4_comments.py` with at least two comments and one print statement.

#### Example stdout

```text
This script practices comments.
```

### Problem 5 - Guild launch checklist

**Setup:** A brand-new apprentice asks, "How do I run my first script?" Write the
Guild's quick-start checklist.
Create `week01_p5_checklist.txt` with 5 bullet points for how to run a Python script.

#### Example output target

```text
- Open terminal
- Navigate to folder
- Run python filename.py
- Read output
- Fix errors and rerun
```

## Week 2

> **Story so far:** Ada introduces your apprentice party — Aria, Dax, Lina, and
> Timo — the heroes you will bring to life in BranchQuest. Lina, who loves data,
> shows you how the game stores information.

### Problem 1 - Party greeter bot

**Setup:** BranchQuest greets each hero by name. Build the greeter that asks for
a name and welcomes the player.
Create `week02_p1_name_card.py` that asks name and prints greeting.

#### Example stdout

```text
Enter your name: Alex
Hello, Alex!
```

### Problem 2 - Type detective with Lina

**Setup:** Lina explains that the game tracks different kinds of data. Play data
detective and label each value's type.
Create `week02_p2_types.py` with int, float, string, bool variables and print each type.

#### Example stdout

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### Problem 3 - Time-scroll age checker

**Setup:** A time-scroll artifact shows a hero one year older.
Create `week02_p3_age_next_year.py` that asks age and prints age+1.

#### Example stdout

```text
Enter your age: 13
Next year you will be 14
```

### Problem 4 - Party favorites wall

**Setup:** Get to know your party. Collect three favorites and print a summary
card for the Guild wall.
Create `week02_p4_favorites.py` that asks 3 favorites and prints a summary.

#### Example stdout

```text
Favorite color: blue
Favorite game: chess
Favorite snack: popcorn
Summary: blue, chess, popcorn
```

### Problem 5 - Hero profile card

**Setup:** Every hero in BranchQuest needs a character sheet. Print a formatted
profile with name, age, and hobby.
Create `week02_p5_profile_card.py` with name, age, hobby and formatted output.

#### Example stdout

```text
Name: Alex
Age: 13
Hobby: Soccer
```

## Week 3

> **Story so far:** BranchQuest needs math it can trust. Grace, the Guild's
> Chief Bug-Hunter, warns that sloppy arithmetic is exactly the kind of crack
> the Glitch slips through — so every calculation must be exact.

### Problem 1 - Quest score math

**Setup:** Two heroes finish a quest with points to combine.
Create `week03_p1_math.py` that asks two numbers and prints sum and product.

#### Example stdout

```text
First number: 4
Second number: 6
Sum: 10
Product: 24
```

### Problem 2 - Sparring-match comparison

**Setup:** Aria and Timo spar to see who scored higher.
Create `week03_p2_compare.py` that asks two numbers and prints whether first is greater.

#### Example stdout

```text
First number: 9
Second number: 5
First > Second: True
```

### Problem 3 - Gate permission logic

**Setup:** A guarded gate opens only if a hero is old enough AND has a permission token.
Create `week03_p3_logic.py` that asks age and permission (`yes/no`) and prints if allowed.

#### Example stdout

```text
Age: 14
Permission (yes/no): yes
Allowed: True
```

### Problem 4 - Provisioning planner

**Setup:** Dax packs rations before a long quest.
Create `week03_p4_snacks.py` (players * snacks each).

#### Example stdout

```text
Players: 6
Snacks each: 3
Total snacks: 18
```

### Problem 5 - Climate converter

**Setup:** Heroes travel between the hot and cold regions of BranchQuest.
Create `week03_p5_temp.py` for Fahrenheit to Celsius.

#### Example stdout

```text
Fahrenheit: 68
Celsius: 20.0
```

## Week 4

> **Story so far:** Ada reveals the heart of BranchQuest: choices. Today you
> build the branching gates that make every player's path different — the very
> branches the game is named for.

### Problem 1 - Apprentice trial checker

**Setup:** New apprentices must pass a trial: score 70 or higher passes.
Create `week04_p1_pass_fail.py`: score >= 70 => pass else fail.

#### Example stdout

```text
Score: 82
Result: Pass
```

### Problem 2 - Gatekeeper classifier

**Setup:** A gatekeeper sorts travelers into entry tiers by age.
Create `week04_p2_ticket.py`: child (<13), teen (13-17), adult (18+).

#### Example stdout

```text
Age: 15
Ticket type: Teen
```

### Problem 3 - Traveler's advisor

**Setup:** Before crossing a region, heroes need advice on what to wear.
Create `week04_p3_weather.py` using temp and rain input.

#### Example stdout

```text
Temperature: 55
Raining? (yes/no): yes
Advice: Wear a jacket and bring an umbrella.
```

### Problem 4 - Level gate

**Setup:** A hero reaches a locked gate deep inside BranchQuest.
Create `week04_p4_level_gate.py` with 3 branches.

#### Example stdout

```text
Level: 4
Gate status: Locked
```

### Problem 5 - Guild vault passcode

**Setup:** The Guild vault opens only with the correct passcode.
Create `week04_p5_password_check.py` that compares input to a stored password.

#### Example stdout

```text
Enter password: tiger123
Access granted
```

## Week 5

> **Story so far:** The party trains for the road ahead. Loops let heroes repeat
> drills — and let the Guild vault keep asking until the right code is entered,
> no matter how many times Timo guesses wrong.

### Problem 1 - Training-rep counter

**Setup:** The party runs training reps out loud.
Create `week05_p1_count.py` that prints numbers from 1 to N.

#### Example stdout

```text
N: 5
1
2
3
4
5
```

### Problem 2 - Even-energy crystals

**Setup:** BranchQuest grants bonus energy on even-numbered levels.
Create `week05_p2_even.py` that prints even numbers from 2 to N.

#### Example stdout

```text
N: 10
2
4
6
8
10
```

### Problem 3 - Lina's spellbook drills

**Setup:** Lina memorizes a times table to power her spells.
Create `week05_p3_table.py` for one chosen number (1-12).

#### Example stdout

```text
Number: 3
3 x 1 = 3
3 x 2 = 6
...
3 x 12 = 36
```

### Problem 4 - Vault retry loop

**Setup:** To keep the Glitch out, the vault keeps asking until the correct passcode is entered.
Create `week05_p4_retry_password.py` that loops until correct password.

#### Example stdout

```text
Password: cat
Try again
Password: dog
Try again
Password: lion
Access granted
```

### Problem 5 - Number-hunter puzzle

**Setup:** A BranchQuest puzzle hides a secret number for players to hunt.
Create `week05_p5_guess.py` with a fixed target number.

#### Example stdout

```text
Guess: 7
Too low
Guess: 11
Correct
```

## Week 6

> **Story so far:** Ada teaches the maker's golden rule: build tools you can
> reuse, not one-off scripts. Today you forge the Guild's first shared
> functions.

### Problem 1 - Your first reusable tool

**Setup:** The Guild needs an add tool every maker can reuse.
Create `week06_p1_add_function.py` with `add(a, b)`.

#### Example stdout

```text
add(3, 4) -> 7
```

### Problem 2 - Room-builder helper

**Setup:** BranchQuest's map needs its rooms measured.
Create `week06_p2_area.py` with `rectangle_area(length, width)`.

#### Example stdout

```text
rectangle_area(5, 2) -> 10
```

### Problem 3 - Even-key utility

**Setup:** Some BranchQuest doors accept only even keys.
Create `week06_p3_is_even.py` with `is_even(n)`.

#### Example stdout

```text
is_even(8) -> True
is_even(7) -> False
```

### Problem 4 - Greeting forge

**Setup:** Turn the game's greeter into a reusable function for any hero.
Create `week06_p4_greeting.py` with function parameter for name.

#### Example stdout

```text
greet("Alex") -> Hello, Alex!
```

### Problem 5 - Maker's command center

**Setup:** Assemble your tools into one toolkit run from a `main()`.
Create `week06_p5_main_program.py` that calls at least 3 functions.

#### Example stdout

```text
Sum: 9
Area: 12
Even check: True
```

## Week 7

> **Story so far:** Every adventure needs an inventory and readable messages.
> You build the systems that let heroes carry items — and decode a note the
> Glitch scrambled backwards.

### Problem 1 - Decode the scrambled message

**Setup:** The Glitch left a message backwards. Reverse the text to read it.
Create `week07_p1_reverse.py` to reverse input text.

#### Example stdout

```text
Text: code
Reversed: edoc
```

### Problem 2 - Rune counter

**Setup:** Lina counts the vowel-runes hidden in words of power.
Create `week07_p2_vowels.py` that counts vowels (a,e,i,o,u) in:
`banana`, `octopus`, `gerbil`, `horse`, `onomatopoeia`.
For a bonus, show how to include `y` as a vowel.

#### Example stdout

```text
banana -> 3
octopus -> 3
gerbil -> 2
horse -> 2
onomatopoeia -> 8
Bonus (including y): mystery -> 2
```

### Problem 3 - Provision pack

**Setup:** Dax loads the party's pack before setting out.
Create `week07_p3_shopping.py` to collect 5 items in list.

#### Example stdout

```text
Item 1: milk
Item 2: bread
Item 3: eggs
Item 4: apples
Item 5: rice
Final list: ['milk', 'bread', 'eggs', 'apples', 'rice']
```

### Problem 4 - Top-score finder

**Setup:** Peek at the BranchQuest leaderboard and find the highest score.
Create `week07_p4_largest.py` from a fixed list.

#### Example stdout

```text
Numbers: [3, 9, 2, 14, 7]
Largest: 14
```

### Problem 5 - Inventory screen

**Setup:** Number the backpack so teammates can call out items fast.
Create `week07_p5_numbered_list.py` using `enumerate`.

#### Example stdout

```text
1. map
2. torch
3. rope
```

## Week 8

> **Story so far:** Disaster! The night before the first demo, the Glitch swarms
> BranchQuest and three scripts crash. Grace — the Guild's Chief Bug-Hunter, who
> gave the "bug" its name long ago — teaches you to hunt them down one traceback
> at a time.

### Problem 1 - Bug hunt: the missing hero (NameError)

**Setup:** A teammate's script crashes before launch — a hero's name will not print.
Fix `week08_p1_name_error.py` (provided buggy file).
Buggy starter files are provided in `course-materials/week08-buggy-files/`.

#### Example stdout

```text
Player: Alex
```

### Problem 2 - Bug hunt: broken score math (TypeError)

**Setup:** The score calculator treats numbers as text and refuses to add.
Fix `week08_p2_type_error.py` so numeric math works.
Use the provided buggy file from `course-materials/week08-buggy-files/`.

#### Example stdout

```text
Total: 18
```

### Problem 3 - Bug hunt: inventory crash (IndexError)

**Setup:** The inventory display reaches for an item that is not there.
Fix `week08_p3_index_error.py` with safe list access.
Use the provided buggy file from `course-materials/week08-buggy-files/`.

#### Example stdout

```text
No fourth item found.
```

### Problem 4 - Bug-hunter's report

**Setup:** Grace keeps an incident log for every Glitch attack.
Create `week08_p4_debug_log.txt` describing at least 3 fixes.

#### Example output target

```text
Bug 1: NameError because variable name mismatch
Fix: changed playerName to player_name
```

### Problem 5 - Debrief with Grace

**Setup:** Grace asks every apprentice to reflect after a bug hunt.
Create `week08_p5_reflection.txt` (8-10 sentences).

#### Example output target

```text
I learned to read the traceback from top to bottom...
```

## Week 9

> **Story so far:** The Glitch is beaten back, and it is time to ship the first
> playable chapter of BranchQuest: **Cave Quest**. Build it end to end and demo
> it for Ada and the party.

### Problem 1 - Cave Quest intro scene

**Setup:** Chapter 1 of BranchQuest opens in the Cave and needs a strong opening.
Create `week09_p1_intro_function.py` with `show_intro()`.

#### Example stdout

```text
Welcome to Cave Quest!
```

### Problem 2 - First major choice

**Setup:** Give players a branch that changes what they find in the Cave.
Create `week09_p2_choice.py` with two choices and outcomes.

#### Example stdout

```text
Choose left or right: left
You found a torch.
```

### Problem 3 - Inventory tracker

**Setup:** Track what players collect as they explore the Cave.
Create `week09_p3_inventory.py` adding found items to list.

#### Example stdout

```text
Inventory: ['torch', 'coin']
```

### Problem 4 - Replay mode

**Setup:** Let players try different paths through the Cave until they stop.
Create `week09_p4_replay.py` to replay until user says no.

#### Example stdout

```text
Play again? yes
Play again? no
Thanks for playing.
```

### Problem 5 - Playable Cave Quest

**Setup:** Combine intro, choice, inventory, and replay into one playable chapter to demo.
Create `week09_p5_checkpoint_game.py` combining all above.

#### Example stdout

```text
Welcome to Cave Quest!
Choose path: right
You found a map.
Play again? no
Final inventory: ['map']
```

## Week 10

> **Story so far:** Ada reviews Cave Quest and nods: "Good — now make it clean
> before we expand it." Real studios refactor before adding features, so you
> tidy the code the whole party will build on next.

### Problem 1 - Refactor the intro module

**Setup:** Cave Quest is growing; move the intro logic into its own function.
Refactor Week 9 intro code into its own function.

#### Example stdout

```text
=== Cave Quest ===
```

### Problem 2 - Refactor turn logic

**Setup:** Duplicated choice code is slowing the party down.
Move choice logic into `play_turn()` returning item found.

#### Example stdout

```text
You found: rope
```

### Problem 3 - Refactor the ending system

**Setup:** Endings should depend on what the hero collected.
Move ending logic into `show_ending(inventory)`.

#### Example stdout

```text
Ending: Explorer rank achieved.
```

### Problem 4 - Document with docstrings

**Setup:** The whole party will build on this code, so make it easy to read.
Add docstrings to all functions.

#### Example output target

```text
"""Plays one turn and returns discovered item."""
```

### Problem 5 - Engineering change notes

**Setup:** Ada asks what improved after the refactor.
Write `week10_p5_refactor_notes.txt` with at least 5 improvements.

#### Example output target

```text
Improvement 1: Removed duplicated choice code.
```

## Week 11

> **Story so far:** BranchQuest needs to know its heroes. You build the party
> roster as a dictionary — and a fifth apprentice, Nova the knight, officially
> joins the Guild.

### Problem 1 - Party database

**Setup:** Store the party in a dictionary of name/role pairs: Aria, Dax, Lina, Timo.
Create `week11_p1_dict_basics.py` with at least 4 key/value pairs.

#### Example stdout

```text
{'aria': 'archer', 'dax': 'healer', 'lina': 'mage', 'timo': 'scout'}
```

### Problem 2 - Recruit Nova

**Setup:** A new knight, Nova, joins the party.
Create `week11_p2_update_dict.py` to add or update one entry.

#### Example stdout

```text
Added: nova -> knight
```

### Problem 3 - Role lookup tool

**Setup:** Quickly check any hero's role before a mission.
Create `week11_p3_lookup.py` and handle missing key.

#### Example stdout

```text
Lookup name: lina
Role: mage
```

### Problem 4 - Roster printout

**Setup:** Print the whole party for mission planning.
Create `week11_p4_iterate.py` printing all `name: role` lines.

#### Example stdout

```text
aria: archer
dax: healer
```

### Problem 5 - Party book app

**Setup:** Build a menu app to manage the party book.
Create `week11_p5_character_book.py` with add + lookup + list options.

#### Example stdout

```text
1) Add
2) Lookup
3) List
Choice: 3
aria: archer
```

## Week 12

> **Story so far:** Ada's rule holds: plan before you build. You design
> BranchQuest's quest-select screen with pseudocode and a flowchart before
> writing a single line of code.

### Problem 1 - Quest-select pseudocode

**Setup:** Ada approves logic before coding starts.
Write `week12_p1_pseudocode.txt` for a 3-choice quest selector.

#### Example output target

```text
START
SHOW 3 quests
GET choice
IF choice valid THEN show result
END
```

### Problem 2 - Quest-select flowchart

**Setup:** Draw the decision logic so the whole party can see the branches.
Create `week12_p2_flowchart.png` for that logic.

#### Example output target

```text
Flowchart has Start -> Choice -> Branches -> End
```

### Problem 3 - Build the quest selector

**Setup:** Turn your approved plan into working Python for three quests.
Create `week12_p3_quest_selector.py` from pseudocode.

#### Example stdout

```text
1) Forest Watch
2) River Run
3) Sky Tower
Choose: 2
River Run selected.
```

### Problem 4 - Guard against bad input

**Setup:** The Glitch loves unexpected input, so handle invalid choices safely.
Create `week12_p4_validated_selector.py` with invalid-choice handling.

#### Example stdout

```text
Choose: 9
Invalid choice.
```

### Problem 5 - Prove it is correct

**Setup:** Explain to Ada why your selector gives exactly one result per valid choice.
Create `week12_p5_algorithm_explain.txt` describing correctness.

#### Example output target

```text
The algorithm is correct because each valid input maps to exactly one output...
```

## Week 13

> **Story so far:** The party's inventory has grown huge. You build search so
> heroes can find an item instantly — and race linear against binary search to
> see which is faster.

### Problem 1 - Linear search tool

**Setup:** Search an unsorted backpack for an item.
Create `week13_p1_linear_search.py` returning index or -1.

#### Example stdout

```text
linear_search(['map', 'rope', 'key'], 'rope') -> 1
```

### Problem 2 - Binary search tool

**Setup:** Search a sorted artifact vault quickly.
Create `week13_p2_binary_search.py` for sorted lists.

#### Example stdout

```text
binary_search(['coin', 'key', 'map', 'rope'], 'map') -> 2
```

### Problem 3 - Search race

**Setup:** Race the two searches and count how many checks each one needs.
Create `week13_p3_compare_steps.py` counting steps used by each search.

#### Example stdout

```text
Linear steps: 5
Binary steps: 3
```

### Problem 4 - Item finder app

**Setup:** Build a command-line finder for BranchQuest items.
Create `week13_p4_search_app.py` asking user target item.

#### Example stdout

```text
Enter target: key
Found at index 2
```

### Problem 5 - Search strategy write-up

**Setup:** Grace asks when each search type should be used.
Create `week13_p5_analysis.txt` comparing when to use each search.

#### Example output target

```text
Use linear search when data is small or unsorted...
```

## Week 14

> **Story so far:** The Guild wants a BranchQuest leaderboard. You build sorting
> to rank scores — then combine it with last week's search to find any rank
> fast.

### Problem 1 - Bubble sort engine

**Setup:** Sort quest times from slowest to fastest.
Create `week14_p1_bubble_sort.py`.

#### Example stdout

```text
Before: [5, 2, 4]
After: [2, 4, 5]
```

### Problem 2 - Insertion sort practice

**Setup:** Keep the leaderboard ordered as new scores arrive.
Create `week14_p2_insertion_sort.py`.

#### Example stdout

```text
Before: [9, 1, 6]
After: [1, 6, 9]
```

### Problem 3 - Leaderboard sorter

**Setup:** The Guild wants BranchQuest scores ranked each week.
Create `week14_p3_leaderboard.py` sorting scores ascending.

#### Example stdout

```text
Scores before: [42, 17, 31]
Scores after: [17, 31, 42]
```

### Problem 4 - Sort, then search

**Setup:** Reuse your Week 13 binary search: sort the scores, then find a target.
Create `week14_p4_sort_then_search.py` and search in sorted output.

#### Example stdout

```text
Sorted: [3, 8, 11, 14]
Target 11 found at index 2
```

### Problem 5 - Sorting tradeoffs reflection

**Setup:** Share what you learned about sorting tradeoffs with next semester's apprentices.
Create `week14_p5_reflection.txt` on sorting tradeoffs.

#### Example output target

```text
Bubble sort is easy to understand but can be slow for large lists...
```

## Week 15

> **Story so far:** Players want to save their progress. You build BranchQuest's
> mission-log system, reading and writing the Guild's `missions.txt` records.

### Problem 1 - Read the mission log

**Setup:** BranchQuest writes mission status lines to a file.
Create `week15_p1_read_lines.py` counting non-empty lines in `missions.txt`.
Use the provided file from `course-materials/week15-file-inputs/missions.txt`.

#### Example stdout

```text
Non-empty lines: 5
```

### Problem 2 - Completion counter

**Setup:** The Guild wants progress totals: complete vs incomplete missions.
Create `week15_p2_count_complete.py` counting `complete` entries.
Use the provided file from `course-materials/week15-file-inputs/missions.txt`.

#### Example stdout

```text
Completed: 3
Incomplete: 2
```

### Problem 3 - Summary writer

**Setup:** Automate a mission summary report for the Guild.
Create `week15_p3_write_summary.py` writing totals to `summary.txt`.

#### Example stdout

```text
Summary written to summary.txt
```

### Problem 4 - Full report pipeline

**Setup:** Build one script that reads the log, counts, prints, and saves.
Create `week15_p4_report.py` doing read + count + write.
Use the provided file from `course-materials/week15-file-inputs/missions.txt`.

#### Example stdout

```text
Total missions: 5
Completed: 3
Incomplete: 2
```

### Problem 5 - Save-system reflection

**Setup:** Document what you learned about working with files.
Create `week15_p5_reflection.txt` with 5 lessons learned.

#### Example output target

```text
Lesson 1: Always strip newline characters.
```

## Week 16

> **Story so far:** A neighboring guild speaks other "dialects" — Lua, C++, and
> Java. Ada sends you to learn how BranchQuest could be ported so you can read
> code in any language you meet.

### Problem 1 - Dialect pattern finder

**Setup:** Compare how the same idea looks in two dialects.
Create `week16_p1_constructs.txt` listing variables/loops/functions in Python vs Java.
Use the provided examples in `course-materials/week16-cross-language-samples/`.

#### Example output target

```text
Python variable: score = 10
Java variable: int score = 10;
```

### Problem 2 - Translate the logic

**Setup:** Show the party that logic transfers across syntax.
Create `week16_p2_translation.txt` showing pseudocode for a loop in both Python and C++ style.

#### Example output target

```text
FOR i from 1 to 5
Python: for i in range(1, 6)
C++: for (int i = 1; i <= 5; i++)
```

### Problem 3 - Dialect difference chart

**Setup:** Build a quick-reference chart for makers learning a new dialect.
Create `week16_p3_differences.txt` with at least 5 syntax differences.

#### Example output target

```text
Difference: Java uses braces {}, Python uses indentation.
```

### Problem 4 - Why concepts travel

**Setup:** Explain to a friend why learning one dialect helps with all the others.
Create `week16_p4_shared_concepts.txt` (8-10 sentences).

#### Example output target

```text
Even though syntax differs, conditionals and loops solve the same decision/repetition problems...
```

### Problem 5 - Cross-dialect takeaway

**Setup:** Give Ada your final insights on reading other dialects.
Create `week16_p5_summary.txt` with 3 similarities, 3 differences, and 1 takeaway.

#### Example output target

```text
Takeaway: Learn concepts first; syntax can be learned later.
```

### Bonus challenge (optional) - Public API explorer with Python requests

**Setup:** Ada offers a side-quest: pull live data into BranchQuest for dynamic
flavor — a creature codex, weather events, or character data.
Use starter files in `course-materials/week16-api-bonus/` and build one script that fetches live data.

Choose one API source from the curated list in `course-materials/week16-api-bonus/README.md`.

Create `week16_bonus_api_explorer.py` that:

1. Accepts one user input (for example Pokemon name, city, or character id).
2. Sends a `GET` request with `requests.get(..., timeout=10)`.
3. Handles status codes with at least `200` and one non-200 case.
4. Parses JSON and prints 3-5 useful fields.

#### Example stdout target (PokeAPI)

```text
Pokemon name: ditto
Name: Ditto
ID: 132
Weight: 40
Primary Type: normal
```

## Week 17

> **Story so far:** Your apprenticeship capstone has arrived: design and build
> **your own** BranchQuest-style game. Ada approves your scope and Grace runs
> QA, just like a real studio heading toward launch.

### Problem 1 - Scope your spin-off

**Setup:** One week to launch. Ada asks you to define what is realistic.
Create `week17_p1_scope.md` with project goal, features, and non-features.

#### Example output target

```text
Goal: Build a playable text adventure with 3 endings.
```

### Problem 2 - Function map

**Setup:** Make a function map so another maker could maintain your game.
Create `week17_p2_functions.md` listing all functions and their purpose.

#### Example output target

```text
show_intro(): displays game title and start prompt
```

### Problem 3 - Grace's QA checklist

**Setup:** Step into Grace's role and catch bugs before showcase day.
Create `week17_p3_test_checklist.md` with at least 10 test cases.

#### Example output target

```text
Test 1: Invalid menu choice -> error message appears
```

### Problem 4 - Release candidate

**Setup:** Prepare a near-final build the Guild could play.
Submit near-final code in `week17_p4_near_final/`.

#### Example stdout target

```text
=== Adventure Builder ===
1) Start
2) Instructions
3) Exit
```

### Problem 5 - Showcase outline

**Setup:** Plan your 5-slide demo flow before the Guild Showcase.
Create `week17_p5_slides_outline.md` with 5-slide structure.

#### Example output target

```text
Slide 1: Problem and idea
Slide 2: Program structure
```

## Week 18

> **Story so far:** Graduation day at the Maker's Guild. You ship your final
> game, present it at the Guild Showcase, and become a full maker.

### Problem 1 - Ship the final build

**Setup:** Release your final version like a real launch.
Submit final code in `week18_p1_final_code/`.

#### Example stdout target

```text
Program runs from start to finish with no crashes.
```

### Problem 2 - Note to a future maker

**Setup:** Write a note to your future self as a coder.
Create `week18_p2_reflection.txt` answering 3 prompts.

#### Example output target

```text
Strongest skill: Functions
Biggest challenge: Debugging
Next goal: Build larger projects
```

### Problem 3 - Research paper talk

**Setup:** Your written paper was submitted in Week 17; today prepare your 3-minute paper talk for the Showcase.
Create `week18_p3_paper_talk.md` with speaking notes for your research-paper presentation.

#### Example output target

```text
Hook -> thesis -> 2 key findings -> why it matters -> one source you trust
```

### Problem 4 - Showcase speaking script

**Setup:** Build calm, clear speaking notes for your live Showcase demo.
Create `week18_p4_demo_script.md` (2-3 minute speaking notes).

#### Example output target

```text
Intro -> Key feature demo -> Challenge -> Lesson learned
```

### Problem 5 - Maker's portfolio

**Setup:** Curate your best work into a maker's portfolio.
Create `week18_p5_portfolio_readme.md` linking best 5 semester artifacts.

#### Example output target

```text
Artifact 1: Week 9 checkpoint game
Artifact 2: Week 13 search comparison
```
