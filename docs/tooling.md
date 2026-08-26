# Tooling Decisions

## Development Environment

The project is being developed locally on Windows.

A local development setup is sufficient for the current phase and avoids introducing unnecessary cloud tooling before it is needed.

## Git

Git is used for local version control.

It provides:

- change tracking

- staging and commits

- project history

- synchronization with GitHub

The project currently uses a simple `main` branch workflow because it is a solo portfolio project.

## GitHub

GitHub is used as the remote repository and portfolio-facing project location.

It provides:

- remote version control

- project visibility

- repository backup

- a place for recruiters and developers to inspect the project

## Editor and Notebook Tools

VS Code and Jupyter are appropriate tools for future project development.

VS Code can be used for:

- source code

- Markdown documentation

- Git integration

- general project navigation

Jupyter notebooks can later be used for:

- exploratory analysis

- data inspection

- visualization

- modeling experiments

No analysis notebooks have been created yet because data analysis has not started.

## Python Environment

No project-specific Python environment or dependency file has been created yet.

Dependencies will be added only when they are actually required in later phases.

This avoids adding speculative packages before the project needs them.

## Current Tooling Principle

The project will use the simplest tools that adequately support reproducible Data Science work.

Additional tools will only be introduced when they solve a real project requirement.

