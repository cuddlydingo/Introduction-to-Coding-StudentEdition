# Collaborative Semester Project

# Project title

**BranchQuest: A Choice-Driven Python Adventure**

## Project goal

Students collaboratively build a text-based "choose your adventure" game that grows each week as new coding concepts are learned.

> **Shared world with the weekly homework.** The individual homework arc,
> *BranchQuest: The Apprentice Maker's Chronicle*, uses the same name, setting,
> and cast (Ada, Grace, and the party Aria/Dax/Lina/Timo/Nova). Teams may borrow
> that world so individual practice and team work feel like one project. See
> [../course-materials/branchquest-map.md](../course-materials/branchquest-map.md).

> **Student handbook.** The student-facing version of this plan is
> [../course-materials/group-project-handbook.md](../course-materials/group-project-handbook.md) —
> give each team a copy when the project begins.

## Delivery model

- One shared class project repository.
- Small teams (3-4 students each).
- Each team owns one story region/chapter.
- Teams submit via pull requests to a shared `main` branch.

## Core technical constraints

- Python 3 only.
- Terminal-based input/output.
- No external packages required for baseline completion.
- Optional enrichment track: `requests` may be used for API-powered features.
- Code must be modular by end of term (functions and files).

## Suggested repository layout

```text
branchquest/
  main.py
  engine.py
  scenes/
    intro.py
    forest.py
    city.py
    mountain.py
  data/
    choices.json
  tests/
    smoke_test_checklist.md
  README.md
```

> **Teacher note on `choices.json`.** The layout shows a JSON/dictionary data
> file, but dictionaries are not formally taught until Week 11. Early teams can
> start with simple `if/elif` branching and in-code lists, then migrate choices
> into `choices.json` around Weeks 10-12 when dictionaries and structured data
> are introduced.

## Milestones by week

## Weeks 1-3: Setup and narrative design

- Define game theme and tone.
- Create story map (nodes and branches).
- Build first playable intro (one choice point).

**Deliverable**

- `README.md` with story overview.
- Flowchart image of choice branches.

## Weeks 4-6: Conditionals, loops, and functions

- Add at least 8 meaningful decision points.
- Add replay loop (play again).
- Move repeated logic into helper functions.

**Deliverable**

- Playable v0.2 with multiple endings.

## Weeks 7-9: Lists, debugging, and checkpoint release

- Track inventory or points with lists.
- Add basic state tracking (health, score, clues).
- Run class debugging day and fix major bugs.

**Deliverable**

- v0.5 checkpoint demo in Week 9.

## Weeks 10-12: Better architecture and data structures

- Use dictionaries to map choices to outcomes.
- Separate scene logic from engine/navigation logic.
- Document pseudocode for one complex branch.

**Deliverable**

- v0.7 with cleaner structure and clearer scene modules.

## Weeks 13-15: Algorithm integration and save/report feature

- Add at least one algorithmic feature:
  - search inventory,
  - sort scoreboard,
  - branch lookup table.
- Add file read/write for saving run summary.

**Deliverable**

- v0.9 with persistence feature.

## Weeks 16-18: Final polish and showcase

- Add intro credits and player instructions.
- Playtest with another team and collect feedback.
- Optional API side quest: integrate one safe public endpoint for dynamic flavor text,
  weather events, or character data.
- Final presentation and live playthrough.

**Deliverable**

- v1.0 final playable game and team retrospective.

## Team roles (rotate every 2-3 weeks)

- Story Lead: narrative and branching quality.
- Logic Lead: conditions, loops, and function integration.
- QA Lead: testing, bug log, and release checklist.
- Repo Lead: pull requests, merge hygiene, release tags.

## Team assessment rubric (suggested)

- 35% Code quality and correctness.
- 25% Collaboration process (PR quality, participation, communication).
- 20% Scope completion by milestones.
- 10% Creativity and user experience.
- 10% Demo clarity and ability to explain technical decisions.

## Instructor checkpoints

- Week 3: Story architecture approval.
- Week 6: Function and control-flow quality review.
- Week 9: Midpoint playable demo.
- Week 12: Structure/refactor review.
- Week 15: Persistence feature check.
- Week 18: Final demo and retrospective.
