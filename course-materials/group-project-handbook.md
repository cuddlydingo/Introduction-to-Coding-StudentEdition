# BranchQuest Group Project — Student Handbook

> **Story so far:** The Maker's Guild has one big job that lasts all semester —
> building **BranchQuest**, the Guild's flagship choose-your-path adventure. You
> and your team are the makers. Keep this handbook open all term so you always
> know what to build, how to turn it in, and how you're graded.

This is your guide for the **collaborative game project** — the team game your
whole class builds together. It is different from your **weekly homework
quests**, which you build alone in your own repository. Here, your team works
together in **one shared class repository**.

---

## 1. What your class is building

Your class is building **BranchQuest: A Choice-Driven Python Adventure** — a
text-based "choose your adventure" game that runs in the terminal and grows
every few weeks as you learn new coding skills. It lives in the same world as
your weekly quests, with the same cast (Ada, Grace, and the party
Aria/Dax/Lina/Timo/Nova), so your solo practice and your team's game feel like
one story.

## 2. Group project vs. weekly homework — the quick version

|  | Weekly homework (solo) | Group project (team) |
| --- | --- | --- |
| Where you work | **Your own** repository | **One shared** class repository |
| Who commits | Just you | Your whole team (3–4 people) |
| You branch, then merge into | **Your own** `main` | The **shared** `main` |
| Who reviews your pull request | Your teacher | A **teammate** (plus your teacher at checkpoints) |
| What you own | Everything | **One region** of the game |

The skills are the same each week — you just use them in two places: once alone
in your homework, and once with your team here.

## 3. Your team and your region

- Teams are **3–4 students**.
- Each team **owns one region/chapter** of the game (for example the **Forest**,
  **City**, or **Mountain**). Your region is yours to design and build.
- You'll coordinate with the other teams so all the regions connect into one
  game.

## 4. Team roles (rotate every 2–3 weeks)

Everyone codes. Roles just say who "owns" each area for a couple of weeks so
nothing falls through the cracks. **Rotate roles every 2–3 weeks** so everyone
gets to try each job.

| Role | You take care of… |
| --- | --- |
| **Story Lead** | Narrative, tone, and branching quality of your region. |
| **Logic Lead** | Conditions, loops, and how the functions fit together. |
| **QA Lead** | Testing, the bug log, and the release checklist. |
| **Repo Lead** | Pull requests, clean merges, and release tags. |

## 5. The rules of the build

- **Python 3 only.**
- **Terminal input/output** — text in, text out, no graphics.
- **No extra packages** are needed to finish the baseline game.
- **Optional:** the `requests` package is allowed only for the optional API side
  quest late in the term.
- **Be modular by the end:** organize your code into **functions and files**,
  not one giant script.

## 6. Your project folder

Your team's starter repository is set up like this:

```text
src/
  main.py        # game entry point — run this to play
  engine.py      # shared helpers: the game loop and routing
  scenes/        # one file per scene in your region
  data/          # game data (plain text now, JSON later)
tests/           # your test notes and checklists
docs/            # design docs and meeting notes
README.md        # your game's story overview
CONTRIBUTING.md  # the team rules in short form
```

Run the game at any time with:

```bash
python src/main.py
```

> **About `data/`:** You'll store choices in a `choices.json` file **later**.
> Dictionaries aren't taught until **Week 11**, so for now start with simple
> `if/elif` choices and lists, then move your choices into `choices.json` around
> **Weeks 10–12** when you learn dictionaries and structured data.

## 7. How your team turns in work (the git flow)

Every change joins the shared game through a **pull request** that a teammate
reviews first. Small changes are easier to review, so keep each pull request
focused on one thing.

1. Start from an up-to-date shared `main`: `git checkout main` then `git pull`.
2. Make a branch for your task:
   - `feature/<short-description>` for new work (e.g. `feature/forest-trap-scene`)
   - `fix/<short-description>` for a bug fix
3. Do **one scoped change**, then commit.
4. Push your branch and open a **pull request into the shared `main`**.
5. Title it with your milestone and region, e.g.
   `Milestone 2 - Forest team - Add trap scene`.
6. In the description, say **what changed and why**, and add your **test notes**.
7. A **teammate reviews** it. Fix any comments they leave.
8. Once at least **one teammate approves** and all comments are resolved, merge
   it into `main`.

### Pull request checklist (copy into your PR description)

- [ ] The change is small and focused on one thing.
- [ ] The code runs locally without crashing.
- [ ] I updated the matching scene/test checklist.
- [ ] The description explains what changed and why.

> **How this differs from homework:** in your solo homework, no teammate reviews
> your work and you merge into *your own* `main`. Here, a teammate must review
> first, and you merge into the *shared* `main` the whole class builds on.

## 8. Milestone roadmap (what to build, and when)

The game grows in six milestones. Each one lines up with skills you're learning
in class and ends with a version number so you can watch it grow.

| Milestone | Weeks | What your team adds | Deliverable |
| --- | --- | --- | --- |
| **1 — Setup & story** | 1–3 | Choose your game's theme and tone, map your region's choices (nodes and branches), and build a first playable intro with one choice. | `README.md` story overview + a **flowchart** of your choice branches. |
| **2 — Choices & endings** | 4–6 | Add **at least 8 meaningful choices**, a **play-again** loop, and move repeated code into **helper functions**. | Playable **v0.2** with multiple endings. |
| **3 — Items & first demo** | 7–9 | Track **inventory or points with lists**, add basic **state** (health, score, clues), and squash major bugs on class debugging day. | **v0.5** checkpoint demo in Week 9. |
| **4 — Cleaner structure** | 10–12 | Use **dictionaries** to map choices to outcomes, split **scene logic** from the **engine**, and write **pseudocode** for one tricky branch. | **v0.7** with clear scene modules. |
| **5 — Smart features & saving** | 13–15 | Add one **algorithm** (search inventory, sort a scoreboard, or a branch lookup) and **save a run summary to a file**. | **v0.9** with a save feature. |
| **6 — Polish & showcase** | 16–18 | Add **credits and player instructions**, **playtest** with another team, add an optional **API side quest**, then present a live playthrough. | **v1.0** final game + team retrospective. |

### Teacher checkpoints

Your teacher reviews the whole game at these points, so aim to have that
milestone's deliverable ready:

- **Week 3:** story/architecture check
- **Week 6:** functions & control-flow check
- **Week 9:** midpoint playable demo
- **Week 12:** structure/refactor check
- **Week 15:** save-feature check
- **Week 18:** final demo & retrospective

## 9. How your team is graded

| Weight | What it measures |
| --- | --- |
| **35%** | Code quality and correctness. |
| **25%** | Collaboration — pull-request quality, participation, communication. |
| **20%** | Scope completed by each milestone. |
| **10%** | Creativity and player experience. |
| **10%** | Demo clarity and explaining your technical choices. |

Notice that **a quarter of your grade is teamwork** — how you review each other's
pull requests, communicate, and share the work counts as much as the code.

## 10. Teamwork and honesty

- **Everyone commits.** Your own commits and pull requests are the record of what
  you contributed — make sure your name is on real work.
- **Review kindly and clearly.** Say what's good, ask questions, and suggest
  fixes; don't just click approve.
- **Keep it your own.** The course's no-AI-generated-code rule applies to the
  group project too — you must be able to **explain any code your team submits**.
  Ask teammates, your teacher, and approved resources for help, but the work is
  yours. (See your [Academic Honor Statement](../syllabus/academic-honor-statement.md).)

## Quick reference

- **Repo:** the one **shared** class repository (not your homework repo).
- **Branches:** `feature/<desc>` or `fix/<desc>`.
- **Pull request title:** `Milestone N - <team/region> - <what changed>`.
- **Before merge:** one teammate approves and all comments are resolved.
- **Run the game:** `python src/main.py`.
- **Roles rotate** every 2–3 weeks: Story, Logic, QA, Repo.

Welcome to the build, maker — ship something your whole team is proud of.
