# GitHub Workflow and Submission Guide

This is how you turn in your homework every week. Along the way you get real
practice with **branches** and **merge requests** (GitHub calls these *pull
requests*) — the same tools professional software teams use every day. In our
homework, each week's branch is a **quest branch** in the semester-long
BranchQuest story. See [branchquest-map.md](../course-materials/branchquest-map.md)
for the story so far.

Never used git or GitHub before? That is exactly who this guide is written for.
Follow the steps in order and you will be fine.

## The big picture: your own fork

You will make your **own copy** of the class repository, called a **fork**, and
do all your work there.

- The class has one **master repository**:
  `cuddlydingo/Introduction-to-Coding-StudentEdition`. Think of it as the shared
  classroom bookshelf.
- You click **Fork** once, and GitHub gives you a personal copy under your own
  account, for example `alex-kim/Introduction-to-Coding-StudentEdition`. **You
  own your fork** — it is yours to build in all semester.
- Each week you make a **branch** in your fork, do the homework, and open a
  **merge request** to fold that work into your fork's `main` branch.

```text
cuddlydingo/Introduction-to-Coding-StudentEdition   (class master)
        │  you click "Fork"  (one time)
        ▼
alex-kim/Introduction-to-Coding-StudentEdition       (your fork — you own it)
        │  each week: make a quest/weekNN-topic branch, do the work
        ▼
   open a merge request  ->  merge into your own main
```

**You merge your own merge requests — you do not have to wait for approval.**
Your teacher reviews your work afterward and leaves feedback and a grade, so
still do your best work before you merge. GitHub automatically records the time
of every commit and merge, which is how your teacher sees what you turned in and
when.

## One-time setup (do this in Week 1)

### Step A — Fork the class repository (Web UI)

1. Sign in to GitHub (create a free account first if you need one).
2. Go to `github.com/cuddlydingo/Introduction-to-Coding-StudentEdition`.
3. Click **Fork** (top right) → **Create fork**. You now have your own copy at
   `github.com/<your-username>/Introduction-to-Coding-StudentEdition`.

### Step B — Get the files onto your computer (optional, for command-line work)

If you plan to use the command line, copy your fork to your computer with
`git clone`. If you plan to work entirely in the web browser, you can skip this.

```bash
# clone YOUR fork — use your own username, not cuddlydingo
git clone https://github.com/<your-username>/Introduction-to-Coding-StudentEdition.git
cd Introduction-to-Coding-StudentEdition

# (recommended) link the class master as "upstream" so you can pull new materials later
git remote add upstream https://github.com/cuddlydingo/Introduction-to-Coding-StudentEdition.git
```

## Every week: two ways to do it

Here is the full weekly workflow shown **two ways** — pick whichever you like.
**Option 1** stays entirely in the web browser. **Option 2** uses the command
line. The example below is for a student named **Alex Kim** doing Week 3, whose
quest branch is `quest/week03-score-systems` (the exact branch name is printed at
the top of each week's homework packet).

### Option 1 — In the web browser (Web UI)

**Step 1: Create this week's branch**

1. Open your fork on GitHub.
2. Click the **branch button** (it says `main`, just above the list of files).
3. Type the branch name from your homework packet, e.g.
   `quest/week03-score-systems`.
4. Click **Create branch: quest/week03-score-systems from main**.
5. Check that the branch button now shows **your new branch**, not `main`.

**Step 2: Add or change your files**

- To add a new file: click **Add file → Create new file**. Type the file name
  exactly as the homework packet lists it (for example `week03_p1_math.py`), then
  type your code.
- To change a file that already exists: open it and click the **pencil (Edit
  this file)** icon.
- Scroll down to the **Commit changes** box. In the message, write
  `Week 03 - Alex Kim - Homework`. Make sure the option **Commit directly to the
  `quest/week03-score-systems` branch** is selected (**not** `main`). Click
  **Commit changes**. Do this for each file you add or change.

**Step 3: Open your merge request (pull request)**

1. On your fork, click the **Pull requests** tab, then **New pull request**.
2. **This is the step to slow down on.** Because you are working in a fork,
   GitHub tries to send your merge request to the *class master* by default. You
   want it to go to **your own fork** instead:
   - Set **base repository** to
     `<your-username>/Introduction-to-Coding-StudentEdition` (**your** fork — not
     `cuddlydingo/...`).
   - Set **base** to `main`.
   - Set **compare** to `quest/week03-score-systems`.
3. Click **Create pull request**. Give it the title
   `Week 03 - Alex Kim - Score Systems`, write a one-sentence description, and
   click **Create pull request** again.

**Step 4: Merge it**

1. On the merge request page, click **Merge pull request → Confirm merge**.
2. You can click **Delete branch** afterward to stay tidy. That's it — your work
   is on `main`, on time.

### Option 2 — On the command line

```bash
# 1. start from an up-to-date main
git checkout main
git pull                       # updates your fork's main

# 2. create this week's quest branch
git checkout -b quest/week03-score-systems

# 3. do the homework in the assigned files, then save (stage) and commit
git add .
git commit -m "Week 03 - Alex Kim - Homework"

# 4. send the branch up to YOUR fork on GitHub
git push -u origin quest/week03-score-systems
```

Now open the merge request. The easiest way is in the browser: open your fork,
click the **Compare & pull request** banner that appears after you push, and
follow **Step 3** and **Step 4** from Option 1 (double-check the **base
repository** is your own fork).

If you have installed the GitHub CLI (`gh`), you can do it from the terminal
instead. The `--repo` flag makes sure the request goes to **your own fork**:

```bash
# open a pull request into YOUR OWN fork's main
gh pr create \
  --repo <your-username>/Introduction-to-Coding-StudentEdition \
  --base main \
  --head quest/week03-score-systems \
  --title "Week 03 - Alex Kim - Score Systems" \
  --body "Completed the Week 03 quest."

# when it looks good, merge it yourself
gh pr merge --repo <your-username>/Introduction-to-Coding-StudentEdition --merge --delete-branch
```

## Weekly checklist

1. Update `main`: `git checkout main` then `git pull`.
2. Make the quest branch: `git checkout -b quest/weekNN-topic` (name is at the
   top of the homework packet).
3. Do the work in the file names the packet asks for.
4. Commit with this exact message format:
   `Week NN - Firstname Lastname - Homework`.
5. Push your branch and open a **merge request** into your own `main`, titled
   `Week NN - Firstname Lastname - <Quest name>`.
6. **Merge your own merge request** into `main` before the next class.

Some weeks build on earlier work (for example, Week 10 improves your Week 9 Cave
Quest game). For those, start your new branch from your existing game instead of
from scratch.

## Getting new class materials during the term

Sometimes your teacher adds new weeks, or fixes files, in the class master
**after** you have already forked. Those changes do **not** appear in your fork
by themselves — you pull them in yourself. A good habit is to do this at the
**start of each week, before you create that week's quest branch**, so you always
build on the latest materials. Your own homework is kept; this just adds your
teacher's changes on top.

### Option 1 — Web browser (easiest)

You do **not** need the `upstream` link from Option 2 for this. Because you
forked the repository, GitHub already knows your class master, and the **Sync
fork** button pulls from it automatically.

1. Open your fork on GitHub
   (`github.com/<your-username>/Introduction-to-Coding-StudentEdition`).
2. Just above the file list, click **Sync fork**, then **Update branch**. GitHub
   copies your teacher's new commits into your fork's `main`.
3. **Warning — never click "Discard N commits."** That button deletes *your*
   homework. If GitHub says it cannot update automatically, stop and use the
   command line below, or ask your teacher — do not discard anything.
4. If you also work on your computer, bring the update down afterward:
   `git checkout main` then `git pull`.

### Option 2 — Command line

This uses the `upstream` link to the class master. You only add it **once** (you
may already have done this during setup):

```bash
# one time only — skip if you already added upstream
git remote add upstream https://github.com/cuddlydingo/Introduction-to-Coding-StudentEdition.git
```

Then, any time you want the latest materials:

```bash
git checkout main            # be on your own main branch
git pull upstream main       # pull the teacher's updates into your main
git push origin main         # save them back to your fork on GitHub
```

If git reports a **conflict** — uncommon, and only if you changed the same file
your teacher changed — ask your teacher to help you resolve it. Do not delete your
work to make the message go away.

## Before you submit each week

- Your program **runs without crashing** on the example inputs.
- Your files are **named exactly** as the homework packet asks.
- You can **explain your own code** out loud in 2–3 minutes — you may be asked to
  in class.
- The work is **your own**. AI-generated code is not allowed; you sign the
  [academic honor statement](../syllabus/academic-honor-statement.md) in Week 1.
