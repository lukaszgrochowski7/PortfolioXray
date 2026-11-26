Pull request layout
Use this template for every PR. In PR 1, save it as .github/pull_request_template.md in the repo and GitHub fills it in automatically for each new PR.
Title format: feat: add add and list commands (same style as commit messages; put the plan's PR number in the description).

Commit messages
A commit message says what changed and why, so you (and a recruiter) can read the history like a story.
Format: type: short summary
• Summary in the imperative ("add", not "added"), lowercase, no full stop, under 50 characters.
• Optional body after a blank line: why you made the change, not what the code does.
• One logical change per commit. Commit often, at least after every working step.

Type
Use for
feat new feature
fix bug fix
test adding or changing tests
docs README or comments
refactor restructuring without changing behavior
chore setup, dependencies, config

Good:
feat: add holdings table to SQLite schema
fix: handle unknown ticker in price fetch
test: cover P&L for a losing position
docs: add usage example for list command
chore: add pytest to requirements

Bad:
update
fixed stuff
work in progress
asdf

## What

## Why
## Changes

• Add

## How to test
## Checklist
[ ] Tests added or updated, pytest passes
[ ] README updated if usage changed
[ ] No secrets or API keys in the code
[ ] I read my own diff before merging
## Notes
