# Introduction to Coding — Student Edition

A collaborative space for students to turn in homework assignments, receive commented updates from instructors, and learn how to code.

This course introduces students to the foundational concepts of computer programming and the algorithmic thinking that underlies all software development. Python 3 serves as the working language because of its human-readable syntax and operating system agnosticism, allowing students to focus on *how programs are constructed* rather than on language-specific punctuation. Short, structured comparisons with Lua, C++, and Java are used throughout the course to demonstrate that the underlying concepts — variables, control flow, data structures, functions, and algorithms — are largely language-independent.

By the end of the semester, students should be able to read, write, debug, and reason about small Python programs, and should recognize the same constructs when shown code in another language.

> This is the **Student Edition** of the course repository. It contains everything you need as a student — the syllabus, homework packets, provided files, templates, and course reference material. The full course specification lives in [Introduction_to_Coding.md](Introduction_to_Coding.md).

---

## Course at a glance

| | |
| --- | --- |
| **Duration** | One semester — two nine-week terms (18 weeks total) |
| **Format** | Weekly 1-hour in-person lesson + take-home coding practice |
| **Primary language** | Python 3 |
| **Supplemental languages (survey only)** | Lua, C++, Java |
| **Prerequisites** | None; basic computer literacy assumed |
| **Who it's for** | Absolute beginners with no prior coding experience |

---

## What you will learn

Upon successful completion of the course, you will be able to:

1. Explain what a program is and how source code is translated and executed by a computer.
2. Write, run, and debug Python programs using variables, expressions, conditionals, loops, functions, and basic data structures (lists, tuples, dictionaries, strings).
3. Decompose a problem into discrete steps and express a solution as an algorithm using pseudocode and a flowchart before writing code.
4. Implement and explain foundational algorithms, including linear search, binary search, and at least one elementary sort.
5. Read short code samples in Lua, C++, and Java and identify the equivalent constructs you already know from Python.
6. Use version-control basics (branches, commits, merge requests) and apply common debugging practices, including reading error messages and step-through inspection.
7. Demonstrate professional habits: writing readable code, naming things clearly, and commenting where intent is not obvious.

---

## The 18-week arc

The semester is divided into two nine-week terms. Term 1 establishes the fundamentals in Python; Term 2 extends them into algorithms, data structures, and a cross-language survey, ending with a small individual project.

### Term 1 — Foundations in Python (Weeks 1–9)

| Week | Topic | Key concepts |
| :--: | --- | --- |
| 1 | What is a program? | Hardware vs. software, source vs. machine code, interpreters vs. compilers, environment setup |
| 2 | Values, variables, and types | Integers, floats, strings, booleans; assignment; basic input/output |
| 3 | Expressions and operators | Arithmetic, comparison, and logical operators; operator precedence |
| 4 | Conditionals | `if` / `elif` / `else`; boolean logic; truthiness |
| 5 | Loops | `while` and `for`; iteration; `break` and `continue` |
| 6 | Functions, Part 1 | Definition, parameters, return values, scope |
| 7 | Strings and lists | Indexing, slicing, common methods, iteration over collections |
| 8 | Debugging and reading errors | Tracebacks, common error categories, `print` debugging, `try` / `except` |
| 9 | Term 1 checkpoint project | A small integrated program (the *Cave Quest* mini adventure) |

### Term 2 — Algorithms, data, and language comparison (Weeks 10–18)

| Week | Topic | Key concepts |
| :--: | --- | --- |
| 10 | Functions, Part 2 | Decomposition, reuse, introductory recursion |
| 11 | Dictionaries and structured data | Key/value storage, lookups, choosing the right collection |
| 12 | Algorithmic thinking | Pseudocode, flowcharts, decomposition, correctness |
| 13 | Searching | Linear search, binary search, why sorted input matters |
| 14 | Sorting | Bubble/insertion sort traced by hand and implemented in Python |
| 15 | Files and persistence | Reading and writing text files; basic data processing |
| 16 | Cross-language survey | One program in Python, Lua, C++, and Java; optional public API + JSON mini-lab with `requests` |
| 17 | Final project work | Student-chosen project: planning, implementation, iteration |
| 18 | Presentations and review | Demonstrations, peer review, semester wrap-up |

Detailed in-class plans and per-week homework are in [lesson-plans/weekly-lesson-plans.md](lesson-plans/weekly-lesson-plans.md).

---

## Major components

Grades are built from four connected strands of work plus professional habits:

- **Weekly coding homework (individual).** One assignment per week, following the *BranchQuest* story arc and submitted through GitHub. The weekly packets are in [homework-packets/student/](homework-packets/student/), with an all-in-one reference in [homework-packets/weekly-homework-problems-student-version.md](homework-packets/weekly-homework-problems-student-version.md).
- **Collaborative class game project.** A Python text-based "choose your adventure" game built in small teams — your team handbook is [course-materials/group-project-handbook.md](course-materials/group-project-handbook.md).
- **Final individual coding project.** A student-chosen program built and presented in the final weeks.
- **Research paper.** One paper of at least 1,024 words on a technology topic, scaffolded with milestone checkpoints across the semester — see [lesson-plans/research-paper-track.md](lesson-plans/research-paper-track.md).

---

## BranchQuest — the story that ties it together

The weekly homework follows one connected narrative, **BranchQuest: The Apprentice Maker's Chronicle**. You play a new apprentice at a game-maker's guild, building a class text adventure one skill at a time. Recurring characters (Ada the Guildmaster, Grace the Chief Bug-Hunter, and the adventuring party) and cumulative weekly beats keep practice feeling like one continuous project.

Each week is framed as a **quest branch**, submitted by **merge request** — giving you a gentle first taste of professional version-control habits. Read the story overview in [course-materials/branchquest-map.md](course-materials/branchquest-map.md) in Week 1.

---

## How work is submitted

You will practice authentic feature-branch and merge-request (pull request) workflows. At the start of term you **fork** the class master repository to your own GitHub account and do all your work in that fork. Each week's homework is then its own quest branch:

1. Update local `main`: `git checkout main` then `git pull`.
2. Create the quest branch: `git checkout -b quest/weekNN-topic`.
3. Complete the work in the assigned file names.
4. Commit using the required message format: `Week NN - Firstname Lastname - Homework`.
5. Push the branch and open a merge request into your own fork's `main`, titled `Week NN - Firstname Lastname - <Quest name>`.
6. Merge your own merge request into `main` before the next class.

You merge your own merge requests — no approval needed. Your instructor reviews your merged work afterward for correctness, readability, and commit history, then leaves feedback and a grade. Full details are in [lesson-plans/github-workflow-and-submission.md](lesson-plans/github-workflow-and-submission.md).

---

## Grading and academic integrity

| Component | Weight |
| --- | :--: |
| Weekly homework (individual) | 40% |
| Collaborative game project | 25% |
| Final individual project | 20% |
| Research paper | 10% |
| Participation / professional habits | 5% |

**AI-generated code and content are not allowed** for homework or projects. You must be able to explain everything you submit; commit history and short in-class code walkthroughs are used to verify authorship. Rubrics and the full AI-use policy are in [lesson-plans/grading-and-academic-integrity.md](lesson-plans/grading-and-academic-integrity.md). You will sign the [academic honor statement](syllabus/academic-honor-statement.md) in Week 1.

---

## Tools and environment

- **Runtime:** Python 3 (current stable release).
- **Editor:** Visual Studio Code with the official Python extension.
- **Version control:** Git and GitHub for submissions and feedback.
- **Supplemental languages:** demonstrated through instructor-led examples and online sandboxes; no local install of Lua, C++, or Java is required.
- **Tablet-friendly:** every assignment can be completed on a laptop, Chromebook, or tablet with a keyboard via a browser-based Python environment.

Assignments run on any standard personal computer. Full minimum and recommended hardware specifications are documented in [Introduction_to_Coding.md](Introduction_to_Coding.md#minimum-computer-requirements). Python dependencies used by course tooling and the optional API mini-lab are listed in [requirements.txt](requirements.txt).

---

## Repository map

| Path | Contents |
| --- | --- |
| [Introduction_to_Coding.md](Introduction_to_Coding.md) | Full course specification: objectives, structure, and computer requirements |
| [syllabus/](syllabus/) | Parent/student syllabus handout and the academic honor statement |
| [course-materials/](course-materials/) | Provided student files: quizzes, templates, buggy files, cross-language samples, API bonus, and the BranchQuest map |
| [chalkboard-talk/](chalkboard-talk/) | Weekly lesson readings to study before each homework (concepts, worked examples, and common mistakes) |
| [homework-packets/](homework-packets/) | Weekly homework packets (student versions) |
| [lesson-plans/](lesson-plans/) | Weekly plan, submission workflow, collaborative project, research track, and grading framework |
| [templates/](templates/) | Starter repository templates for individual and group work |
| [requirements.txt](requirements.txt) | Python dependencies for course tooling and the optional API mini-lab |

---

## Getting started

1. Read the [syllabus handout](syllabus/parent-student-syllabus-handout.md) and the [BranchQuest map](course-materials/branchquest-map.md).
2. Set up Python 3 and VS Code (or a browser-based environment), then pick your GitHub username in Week 1.
3. Fork the class master repository to your own GitHub account; see the [submission workflow guide](lesson-plans/github-workflow-and-submission.md) for the one-time fork-and-clone steps.
4. Each week, branch from `main`, complete your quest in [homework-packets/student/](homework-packets/student/), and open a merge request before the next class.

---

## License

Released under the [MIT License](LICENSE).
