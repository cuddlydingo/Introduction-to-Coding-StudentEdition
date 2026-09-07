# Intro to Coding - Student Repository Template

## Purpose

This repository stores one student's weekly coding assignments, final project, and research paper milestones. Each week's homework is a **quest** in the semester-long BranchQuest story, submitted on its own **quest branch** via a **merge request** (pull request).

## Structure

- `assignments/week01` ... `assignments/week18`: weekly work
- `final-project/`: final coding project
- `research-paper/`: topic proposal, drafts, and final paper
- `notes/`: optional personal notes
- `resources/`: optional screenshots/diagrams

## Weekly submission checklist

1. Start the week's quest branch from an up-to-date `main`:
   `git checkout main && git pull && git checkout -b quest/weekNN-topic`
   (the branch name is at the top of each homework packet).
2. Complete the assignment in the current week folder.
3. Verify the program runs.
4. Commit using the required message format.
5. Push the branch and open a **merge request** (pull request) into your fork's
   `main`, titled `Week NN - Firstname Lastname - <Quest name>`.
6. Merge your own merge request into `main` before the next in-person class — you
   own your fork, so no approval is needed.

See [../../lesson-plans/github-workflow-and-submission.md](../../lesson-plans/github-workflow-and-submission.md)
for the full command sequence.

## Commit message format

`Week NN - Firstname Lastname - Homework`

## Example

`Week 05 - Alex Kim - Homework`
