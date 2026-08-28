# GitHub Workflow and Submission Model

This model supports weekly timestamped submissions and progress tracking. It
also gives students authentic practice with **feature branches** and **merge
requests** (GitHub calls these *pull requests*), framed in the homework as
**quest branches** in the semester-long BranchQuest story. See
[branchquest-map.md](../course-materials/branchquest-map.md)
for the narrative context.

## Recommended structure

Option A (simplest): one classroom organization with one repo per student.

- `intro-coding-student-alex`
- `intro-coding-student-maya`
- etc.

Option B (single shared repo): one branch per student.

- `student/alex`
- `student/maya`
- etc.

**Recommendation:** Use **Option A** for beginners to reduce merge conflicts.
Even with one repo per student, each student still practices real branching by
opening a pull request from their weekly `quest/...` branch into their own
`main`.

## Setting up student repos without Classroom

Option A works without GitHub Classroom — you create the per-student repos
yourself and protect each one. Do this once per student at the start of term.

1. **Make the template reusable.** Open the
   [student repo template](../templates/student-repo-template/README.md) on
   GitHub, then **Settings → General → Template repository** (check the box).
   You can now generate a fresh copy from it at any time.
2. **Create one private repo per student.** Click **Use this template → Create a
   new repository** in the UI, or use the `gh` CLI:

   ```bash
   gh repo create <org>/intro-coding-student-alex \
     --template <org>/student-repo-template \
     --private
   ```

3. **Add the student with _Write_ access — not Admin.** In the new repo,
   **Settings → Collaborators and teams → Add people**, and choose the **Write**
   role. Write lets them branch, push, and open pull requests, but not change
   branch protection or bypass review — which is what makes the next step
   enforceable.

### Require your approval before any merge to `main`

Protect each student's `main` so they cannot merge their own homework until you
approve it. In the repo, go to **Settings → Branches → Add branch protection
rule**, set the branch name pattern to `main`, and enable:

- **Require a pull request before merging.**
- **Require approvals** → set to **1**.
- **Require review from Code Owners.**
- **Do not allow bypassing the above settings** (applies the rule to admins too).

Then commit a one-line `CODEOWNERS` file (repo root or `.github/`) naming you:

```text
*  @your-teacher-handle
```

Because **GitHub never lets anyone approve their own pull request**, and the
student has only _Write_ access, the one required approval can come only from
**you**. The student opens the merge request as usual, and it stays blocked
until your admin account reviews and approves it.

> **Configure it once, not per repo:** create an **organization ruleset**
> (**Org → Settings → Rulesets → New ruleset**) that targets repositories by
> name (for example `intro-coding-student-*`) with the same "require a pull
> request" and "require review from Code Owners" rules. It then applies to every
> current and future student repo automatically.

## Weekly submission protocol (students)

Each week's homework is a **quest branch**: you create a branch, do the work,
push it, and open a **merge request** (pull request) for review before it is
merged into `main`. This mirrors how professional teams ship code.

1. Update your local `main`: `git checkout main` then `git pull`.
2. Create this week's quest branch: `git checkout -b quest/weekNN-topic`
   (for example `quest/week03-score-systems`; the branch name is listed at the
   top of each homework packet).
3. Complete the weekly work in the assigned file names.
4. Commit with the required message format:
   - `Week NN - Firstname Lastname - Homework`
5. Push the branch: `git push -u origin quest/weekNN-topic`.
6. Open a **merge request / pull request** titled
   `Week NN - Firstname Lastname - <Quest name>`, then request review.
7. After feedback, merge the pull request into `main` before the next class.

Some weeks build on earlier work (for example, Week 10 refactors your Week 9
Cave Quest). For those, branch off your existing game rather than starting over.

## Instructor protocol

1. Open each weekly **pull request** and review commit history timestamps.
2. Check code readability and correctness.
3. Leave feedback in pull request comments or repo issues; approve and merge,
   or request changes.
4. Record grade and one actionable suggestion.

## Basic student command sequence

```bash
git clone <repo-url>
cd <repo-name>

# start this week's quest branch from an up-to-date main
git checkout main
git pull
git checkout -b quest/week03-score-systems

# edit files, then stage and commit
git add .
git commit -m "Week 03 - Alex Kim - Homework"

# publish the branch and open a merge request (pull request) on GitHub
git push -u origin quest/week03-score-systems
```

After pushing, open a pull request on GitHub titled
`Week 03 - Alex Kim - Score Systems`, request review, and merge it into `main`
once feedback is addressed.

## Quality gates for each weekly submission

- Program runs without crash for expected inputs.
- File naming follows assignment instructions.
- Student can explain logic in a 2-3 minute code walkthrough.

## Academic integrity checks (no AI assistance)

- In-class "explain your code" spot checks.
- Small in-class remix of homework (students make one modification live).
- Compare style consistency across student submissions over time.
- Require short design notes for larger assignments (what they tried, what failed, what changed).
