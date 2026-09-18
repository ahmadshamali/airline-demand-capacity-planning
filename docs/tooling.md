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

VS Code and Jupyter are actively used for project development.

VS Code is used for:

- Python source code
- Markdown documentation
- Git integration
- repository navigation

Jupyter is used for:

- data acquisition validation
- exploratory analysis
- raw-grain investigation
- route-month aggregation
- activity-rule analysis
- reusable-pipeline validation

The current notebooks are:

- `01_data_acquisition.ipynb`
- `02_carrier_investigation.ipynb`
- `03_route_month_foundation.ipynb`

## Python Environment

The project uses a local `.venv` environment on Windows.

Current environment:

- **Python 3.14.7**
- **pandas 3.0.5**
- **ipykernel 7.3.0**

Direct project dependencies are recorded in:

`requirements.txt`

Current contents:

- `pandas==3.0.5`
- `ipykernel==7.3.0`

Only direct project dependencies are listed. Transitive dependencies are not added manually unless the project uses them directly.