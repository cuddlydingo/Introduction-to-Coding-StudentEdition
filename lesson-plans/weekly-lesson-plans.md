# Weekly Lesson Plans (18 Weeks)

Course alignment source:
[Introduction_to_Coding.md](../Introduction_to_Coding.md).

The individual homework follows a semester-long story, **BranchQuest: The
Apprentice Maker's Chronicle**, in which students play a new apprentice at a
game-maker's guild building a class text adventure. Recurring characters, the
cumulative game they build, and the per-week story beats are introduced in
[../course-materials/branchquest-map.md](../course-materials/branchquest-map.md).
Each week is framed as a **quest branch** submitted by **merge request**; see
[github-workflow-and-submission.md](./github-workflow-and-submission.md).

## Week-by-week plan

## Week 1 - Course launch and coding environment

### In-class focus

- Course expectations and academic integrity policy.
- What a program is: source code, interpreter, execution.
- Python + editor setup check.
- GitHub submission flow demo (instructor-led).

**In-class practice**

- Students run first script: `print("Hello, world")`.
- Students make one personal intro script with `print()`.

**Homework (individual)** — see [week01-homework.md](../homework-packets/student/week01-homework.md)

1. **Hello, future maker** — `week01_p1_hello.py`: print a course welcome message.
2. **Apprentice badge** — `week01_p2_intro.py`: print your name and grade.
3. **Apprentice's goals** — `week01_p3_goals.py`: print 3 coding goals for the semester.
4. **Field notes** — `week01_p4_comments.py`: include at least two comments and one print statement.
5. **Guild launch checklist** — `week01_p5_checklist.txt`: write 5 bullet points for how to run a Python script.

---

## Week 2 - Values, variables, and data types

### In-class focus

- Integers, floats, strings, booleans.
- Variables and assignment.
- Basic `input()` and `print()` formatting.
- Cross-language peek (variables): `score = 10` (Python) vs `int score = 10;` (Java/C++) — same idea, different syntax; previews Week 16.

**In-class practice**

- "Mad Lib" mini script using three user inputs.

**Homework (individual)** — see [week02-homework.md](../homework-packets/student/week02-homework.md)

1. **Party greeter bot** — `week02_p1_name_card.py`: ask name and print greeting.
2. **Type detective with Lina** — `week02_p2_types.py`: define int, float, string, bool variables and print each type with `type()`.
3. **Time-scroll age checker** — `week02_p3_age_next_year.py`: ask age and print age + 1.
4. **Party favorites wall** — `week02_p4_favorites.py`: ask 3 favorites and print a summary.
5. **Hero profile card** — `week02_p5_profile_card.py`: ask name, age, hobby and print formatted profile.

---

## Week 3 - Expressions and operators

**In-class focus**

- Arithmetic, comparison, and logical operators.
- Operator precedence.
- Common expression mistakes.

**In-class practice**

- Build a "tip and total" calculator.

**Homework (individual)** — see [week03-homework.md](../homework-packets/student/week03-homework.md)

1. **Quest score math** — `week03_p1_math.py`: ask two numbers, print sum and product.
2. **Sparring-match comparison** — `week03_p2_compare.py`: ask two numbers, print whether first is greater.
3. **Gate permission logic** — `week03_p3_logic.py`: ask age and permission, print if the gate opens.
4. **Provisioning planner** — `week03_p4_snacks.py`: multiply heroes × rations each.
5. **Climate converter** — `week03_p5_temp.py`: convert Fahrenheit to Celsius.

Note: logic quiz prompts are in `course-materials/week03-expression-quiz/week03_logic_quiz_prompts.txt`.

---

## Week 4 - Conditionals

**In-class focus**

- `if`, `elif`, `else`.
- Boolean logic and truthiness.
- Input validation basics.
- Cross-language peek (conditionals): Python `if x > 10:` (indentation) vs Java/C++ `if (x > 10) { ... }` (braces).

**In-class practice**

- Grade classifier (`A/B/C/...`) based on numeric score.

**Homework (individual)** — see [week04-homework.md](../homework-packets/student/week04-homework.md)

1. **Apprentice trial checker** — `week04_p1_pass_fail.py`: score ≥ 70 = pass, else fail.
2. **Gatekeeper classifier** — `week04_p2_ticket.py`: classify child/teen/adult by age.
3. **Traveler's advisor** — `week04_p3_weather.py`: clothing advice based on temperature and rain input.
4. **Level gate** — `week04_p4_level_gate.py`: 3 branches based on player level.
5. **Guild vault passcode** — `week04_p5_password_check.py`: compare input to a stored passcode.

Note: test case template is in `course-materials/week04-test-cases-template/week04_test_cases_template.txt`.

---

## Week 5 - Loops

**In-class focus**

- `while` and `for` loops.
- Counter patterns and iteration over ranges.
- `break` and `continue`.
- Cross-language peek (loops): Python `for i in range(1, 6):` vs C++ `for (int i = 1; i <= 5; i++)` — same count loop, different syntax.

**In-class practice**

- Number guessing game (simple version).

**Homework (individual)** — see [week05-homework.md](../homework-packets/student/week05-homework.md)

1. **Training-rep counter** — `week05_p1_count.py`: print numbers from 1 to N using a loop.
2. **Even-energy crystals** — `week05_p2_even.py`: print even numbers from 2 to N.
3. **Lina's spellbook drills** — `week05_p3_table.py`: print full multiplication table for a chosen number.
4. **Vault retry loop** — `week05_p4_retry_password.py`: loop until correct passcode entered.
5. **Number-hunter puzzle** — `week05_p5_guess.py`: guessing game with too-high/too-low feedback.

---

## Week 6 - Functions, Part 1

**In-class focus**

- Defining and calling functions.
- Parameters and return values.
- Variable scope basics.
- Cross-language peek (functions): Python `def add(a, b): return a + b` vs Java `int add(int a, int b) { return a + b; }`.
- Self-check with `assert`: demo `assert add(2, 3) == 5` as a fast "did my function work?" test (foreshadows Week 17 testing).

**In-class practice**

- Refactor a long script into 3-4 small functions.

**Homework (individual)** — see [week06-homework.md](../homework-packets/student/week06-homework.md)

1. **Your first reusable tool** — `week06_p1_add_function.py`: write `add(a, b)` and call it.
2. **Room-builder helper** — `week06_p2_area.py`: write `rectangle_area(length, width)`.
3. **Even-key utility** — `week06_p3_is_even.py`: write `is_even(n)` returning True/False.
4. **Greeting forge** — `week06_p4_greeting.py`: write `greet(name)` returning personalized string.
5. **Maker's command center** — `week06_p5_main_program.py`: call at least 3 functions from a `main()`.

---

## Week 7 - Strings and lists

**In-class focus**

- Indexing and slicing strings/lists.
- Common methods (`append`, `split`, `join`, etc.).
- Looping over collections.

**In-class practice**

- Word-frequency-lite counter from a sentence.

**Homework (individual)** — see [week07-homework.md](../homework-packets/student/week07-homework.md)

1. **Decode the scrambled message** — `week07_p1_reverse.py`: reverse input text.
2. **Rune counter** — `week07_p2_vowels.py`: count vowels (a,e,i,o,u) in a series of words; bonus includes `y`.
3. **Provision pack** — `week07_p3_shopping.py`: collect 5 items in a list and print numbered.
4. **Top-score finder** — `week07_p4_largest.py`: find the largest value in a fixed list.
5. **Inventory screen** — `week07_p5_numbered_list.py`: print a numbered list using `enumerate`.

---

## Week 8 - Debugging and error handling habits

**In-class focus**

- Reading tracebacks.
- Common error types (`NameError`, `TypeError`, `ValueError`, `IndexError`).
- Print debugging and "rubber duck" explanation.
- Handling errors with `try`/`except`: catch a bad `int(input())` and show a friendly message instead of crashing.

**In-class practice**

- Students fix 5 intentionally broken scripts.

**Homework (individual)** — see [week08-homework.md](../homework-packets/student/week08-homework.md)

Buggy starter files for problems 1–3 are in `course-materials/week08-buggy-files/`.

1. **Bug hunt: the missing hero (NameError)** — fix `week08_p1_name_error.py` so it prints the hero name correctly.
2. **Bug hunt: broken score math (TypeError)** — fix `week08_p2_type_error.py` so numeric addition works on string input.
3. **Bug hunt: inventory crash (IndexError)** — fix `week08_p3_index_error.py` to safely handle a short list.
4. **Bug-hunter's report** — `week08_p4_debug_log.txt`: document at least 3 bugs: original error, cause, fix.
5. **Debrief with Grace** — `week08_p5_reflection.txt`: 8–10 sentences on your debugging process and lessons learned.

---

## Week 9 - Term 1 checkpoint project

**In-class focus**

- Review game-like scripting patterns.
- Planning before coding.
- Term 1 checkpoint coding session.

**Homework (individual checkpoint project)** — see [week09-homework.md](../homework-packets/student/week09-homework.md)

Build all five parts of the Cave Quest mini adventure:

1. **Cave Quest intro scene** — `week09_p1_intro_function.py`: write `show_intro()` that prints the game title.
2. **First major choice** — `week09_p2_choice.py`: two-branch choice with different item outcomes.
3. **Inventory tracker** — `week09_p3_inventory.py`: add found items to a list and print it.
4. **Replay mode** — `week09_p4_replay.py`: loop until the user declines to play again.
5. **Playable Cave Quest** — `week09_p5_checkpoint_game.py`: combine all four parts into one playable script.

---

## Week 10 - Functions, Part 2 and decomposition

**In-class focus**

- Breaking larger problems into smaller functions.
- Reuse and modular design.
- Intro to simple recursion (concept only).

**In-class practice**

- Decompose a menu-driven utility into modules.

**Homework (individual)** — see [week10-homework.md](../homework-packets/student/week10-homework.md)

Refactor the Week 9 Cave Quest game:

1. **Refactor the intro module** — move intro logic into a standalone `show_intro()` function.
2. **Refactor turn logic** — move choice logic into `play_turn()` that returns the item found.
3. **Refactor the ending system** — move ending logic into `show_ending(inventory)`.
4. **Document with docstrings** — add a one-line docstring to every function in the refactored script.
5. **Engineering change notes** — `week10_p5_refactor_notes.txt`: list at least 5 concrete improvements made.

---

## Week 11 - Dictionaries and structured data

**In-class focus**

- Dictionary keys/values.
- Dictionary iteration patterns.
- Choosing list vs dictionary.

**In-class practice**

- Contact book mini app.

**Homework (individual)** — see [week11-homework.md](../homework-packets/student/week11-homework.md)

1. **Party database** — `week11_p1_dict_basics.py`: create a dictionary of at least 4 hero name/role pairs.
2. **Recruit Nova** — `week11_p2_update_dict.py`: add or update one dictionary entry.
3. **Role lookup tool** — `week11_p3_lookup.py`: ask for a name and print the role, handling missing keys.
4. **Roster printout** — `week11_p4_iterate.py`: iterate and print all name: role pairs.
5. **Party book app** — `week11_p5_character_book.py`: menu-driven app with add, lookup, and list options.

---

## Week 12 - Algorithmic thinking

**In-class focus**

- Pseudocode and flowcharts.
- Correctness: does algorithm always work?
- Step-by-step problem decomposition.

**In-class practice**

- Turn pseudocode into Python code.

**Homework (individual)** — see [week12-homework.md](../homework-packets/student/week12-homework.md)

1. **Quest-select pseudocode** — `week12_p1_pseudocode.txt`: write pseudocode for a 3-choice quest selector (starter template in `course-materials/week12-flowchart-template/`).
2. **Quest-select flowchart** — `week12_p2_flowchart.png`: draw a flowchart of the decision logic.
3. **Build the quest selector** — `week12_p3_quest_selector.py`: convert pseudocode to working Python.
4. **Guard against bad input** — `week12_p4_validated_selector.py`: handle invalid choices gracefully.
5. **Prove it is correct** — `week12_p5_algorithm_explain.txt`: explain why your algorithm works for all valid inputs.

---

## Week 13 - Searching algorithms

**In-class focus**

- Linear search implementation.
- Binary search concept and sorted data requirement.
- Informal efficiency comparison.

**In-class practice**

- Unplugged warm-up: play "guess my number 1-100" to feel linear vs binary search, then find a name in a shuffled vs sorted stack of index cards.
- Trace search steps by hand, then code.

**Homework (individual)** — see [week13-homework.md](../homework-packets/student/week13-homework.md)

1. **Linear search tool** — `week13_p1_linear_search.py`: implement `linear_search(items, target)` returning index or -1.
2. **Binary search tool** — `week13_p2_binary_search.py`: implement `binary_search(sorted_items, target)`.
3. **Search race** — `week13_p3_compare_steps.py`: count and compare steps taken by each algorithm.
4. **Item finder app** — `week13_p4_search_app.py`: ask user for a target item and report result.
5. **Search strategy write-up** — `week13_p5_analysis.txt`: explain when to use linear vs binary search.

---

## Week 14 - Sorting algorithms

**In-class focus**

- Bubble sort or insertion sort.
- Tracing swaps and passes.
- Time-cost intuition (non-math heavy).

**In-class practice**

- Unplugged warm-up: sort students by birthday month using only pairwise swaps (bubble sort) to feel passes and comparisons.
- Sort list manually, then code.

**Homework (individual)** — see [week14-homework.md](../homework-packets/student/week14-homework.md)

1. **Bubble sort engine** — `week14_p1_bubble_sort.py`: implement bubble sort; print list before and after.
2. **Insertion sort practice** — `week14_p2_insertion_sort.py`: implement insertion sort; print before and after.
3. **Leaderboard sorter** — `week14_p3_leaderboard.py`: sort a set of game scores in ascending order.
4. **Sort, then search** — `week14_p4_sort_then_search.py`: sort a list, then use binary search to find a target.
5. **Sorting tradeoffs reflection** — `week14_p5_reflection.txt`: describe sorting tradeoffs for future students.

---

## Week 15 - Files and persistence

**In-class focus**

- Reading/writing text files.
- File paths and safe write habits.
- Lightweight data processing.
- Working directory and file paths: run from the folder that holds the file, or build a path with `pathlib`/`__file__`; explain why a bare `open("missions.txt")` can fail.
- Guard file reads with `try`/`except FileNotFoundError` for a friendly message (reinforces Week 8).

**In-class practice**

- Read names file (`course-materials/week15-file-inputs/names.txt`), output formatted roster.

**Homework (individual)** — see [week15-homework.md](../homework-packets/student/week15-homework.md)

Input file: `course-materials/week15-file-inputs/missions.txt`

1. **Read the mission log** — `week15_p1_read_lines.py`: count non-empty lines in `missions.txt`.
2. **Completion counter** — `week15_p2_count_complete.py`: count complete vs incomplete entries.
3. **Summary writer** — `week15_p3_write_summary.py`: write totals to `summary.txt`.
4. **Full report pipeline** — `week15_p4_report.py`: read, count, print, and write in one script.
5. **Save-system reflection** — `week15_p5_reflection.txt`: 5 lessons learned about working with files.

---

## Week 16 - Cross-language survey

**In-class focus**

- One small program in Python, Lua, C++, Java.
- Same concepts, different syntax.
- How to read unknown language code effectively.
- Callback to Week 1 (Objective 1): Python and Lua are interpreted while C++ and Java are compiled first — connect syntax differences to how each language is translated and run.

**In-class practice**

- Identify variable, loop, function sections in each sample from `course-materials/week16-cross-language-samples/`.
- Optional bonus mini-lab: consume one public JSON endpoint with Python `requests` using `course-materials/week16-api-bonus/`.

**Homework (individual)** — see [week16-homework.md](../homework-packets/student/week16-homework.md)

Reference samples: `course-materials/week16-cross-language-samples/`

1. **Dialect pattern finder** — `week16_p1_constructs.txt`: map equivalent variable/loop/function syntax in Python vs Java.
2. **Translate the logic** — `week16_p2_translation.txt`: show the same loop in pseudocode, Python, and C++.
3. **Dialect difference chart** — `week16_p3_differences.txt`: list at least 5 concrete syntax differences across languages.
4. **Why concepts travel** — `week16_p4_shared_concepts.txt`: 8–10 sentences on why concepts transfer across languages.
5. **Cross-dialect takeaway** — `week16_p5_summary.txt`: 3 similarities, 3 differences, and 1 personal takeaway.

### Bonus extension - Public APIs with Python requests (optional)

- Goal: connect classroom Python skills to real-world JSON APIs.
- Use guide and starters in `course-materials/week16-api-bonus/`.
- Suggested class format (20-30 minutes):
  - 5 min: `requests.get()`, status codes, `.json()`
  - 10 min: run `pokemon_requests_example.py`
  - 10-15 min: students adapt to another endpoint from the curated list
- Reinforce safety habits: API keys in environment variables, no secrets in commits, add timeouts, handle non-200 responses.
- Candidate APIs for student choice:
  - NASA Open APIs (key; `DEMO_KEY` for exploration)
  - SpaceX API (community-maintained, no key)
  - PokeAPI (no key)
  - TMDB (key)
  - Rick and Morty API (no key)
  - OpenWeatherMap (key)
  - REST Countries (check current tier/docs before class)

---

## Week 17 - Final individual project work

**In-class focus**

- Project planning checkpoints.
- Debugging support and design review.
- Optional enrichment coaching: integrate one public API endpoint safely with
  `requests` and error handling.
- Presentation readiness.

**Homework (individual final project)** — see [week17-homework.md](../homework-packets/student/week17-homework.md)

Also due this week (research track): your final research paper `.pdf` and source list; see [research-paper-track.md](./research-paper-track.md).

1. **Scope your spin-off** — `week17_p1_scope.md`: define goal, in-scope features, and out-of-scope items.
2. **Function map** — `week17_p2_functions.md`: list every function by name with a one-line description.
3. **Grace's QA checklist** — `week17_p3_test_checklist.md`: at least 10 test cases covering happy path, invalid input, and edge cases.
4. **Release candidate** — `week17_p4_near_final/`: runnable near-complete code with a short run-instructions note.
5. **Showcase outline** — `week17_p5_slides_outline.md`: 5-slide structure (problem, design, demo, challenge, lesson).

---

## Week 18 - Final presentations and reflection

**In-class focus**

- Final demos (short timed format).
- Peer questions and feedback.
- Semester reflection and next steps in coding.

**Homework/final submissions due** — see [week18-homework.md](../homework-packets/student/week18-homework.md)

1. **Ship the final build** — `week18_p1_final_code/`: complete, runnable final project.
2. **Note to a future maker** — `week18_p2_reflection.txt`: answer three prompts (strongest skill, biggest challenge, next goal).
3. **Research paper talk** — `week18_p3_paper_talk.md`: 3-minute paper presentation notes (the written paper is submitted in Week 17).
4. **Showcase speaking script** — `week18_p4_demo_script.md`: 2–3 minute speaking notes for live presentation.
5. **Maker's portfolio** — `week18_p5_portfolio_readme.md`: link and describe your 5 best semester artifacts.

---

## Ongoing expectation each week

- At least one GitHub push before the next class.
- Students should be ready to explain their own code in class.
- Late work policy and resubmission windows should be enforced consistently.
