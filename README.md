# Airline Passenger Demand Forecasting & Capacity Planning

A Data Science portfolio project focused on forecasting passenger demand by airline route and time period to support network and capacity planning decisions.

## Business Problem

Passenger demand varies across routes and over time, making it difficult for an airline to determine appropriate seat capacity in advance.

Poor capacity decisions may contribute to:

* excess capacity and empty seats
* insufficient capacity and missed passenger demand
* lost revenue opportunities
* inefficient operations

The project focuses on the relationship between expected passenger demand and available or planned seat capacity.

## Project Objective

Use historical airline data to estimate future passenger demand for each route and time period so that the Capacity Planning Team can identify potential demand-capacity mismatches and investigate adjustments before the demand occurs.

The system is intended as decision support. It will not make autonomous airline scheduling or capacity decisions.

## Primary Stakeholder

**Network Planning / Capacity Planning Team**

The eventual system should help planners investigate whether capacity may need to be:

* increased
* maintained
* reduced
* adjusted seasonally

## Unit of Analysis

The conceptual unit of analysis is:

**Origin-destination route over a time period**

Weekly analysis is currently a conceptual preference, but the final time granularity has not been fixed. It will depend on the dataset selected later.

## Current Scope

Planned project work includes:

* historical passenger-demand analysis by route and time
* passenger-demand forecasting
* comparison of forecast demand with available or planned capacity
* identification of possible demand-capacity mismatches
* capacity-planning decision-support signals
* seasonal demand-pattern analysis
* route-level planning insights

The project does not include:

* automatic aircraft assignment
* fleet-assignment optimization
* aircraft-routing optimization
* crew scheduling
* airport-slot optimization
* automatic flight additions or cancellations
* full airline scheduling optimization
* revenue-management algorithms
* dynamic ticket-pricing optimization
* autonomous operational decisions

## Current Project Status

Phase 2 repository and tooling setup has been completed. The project is ready to proceed to methodology, data strategy, and evaluation design.

### Completed

* Phase 1 business understanding
* local Git repository setup
* GitHub remote repository setup
* initial repository organization
* `.gitignore` and data-safety rules
* Phase 1 documentation
* tooling documentation

### Not Yet Completed

* dataset selection
* dataset acquisition
* data cleaning
* exploratory data analysis
* statistical analysis
* feature engineering
* forecasting model development
* model evaluation
* capacity analysis
* dashboards
* deployment

No dataset or forecasting algorithm has been selected yet.

## Repository Structure

```text
airline-demand-capacity-planning/
├── data/
│   └── README.md
├── docs/
│   ├── phase-1-business-understanding.md
│   └── tooling.md
├── notebooks/
│   └── README.md
├── reports/
│   └── README.md
├── src/
│   └── README.md
├── .gitignore
└── README.md
```

## Directory Purpose

* `data/` - future project datasets and data-handling documentation
* `docs/` - project decisions and supporting documentation
* `notebooks/` - future Jupyter notebooks for analytical work
* `reports/` - future polished figures and project outputs
* `src/` - future reusable project source code

## Data Handling

Raw and processed project datasets are excluded from Git tracking by default.

This helps reduce the risk of accidentally committing:

* large data files
* private or sensitive data
* licensed or restricted datasets
* generated intermediate data

No project dataset has been selected or added yet.

## Tools

Current project tools include:

* **Git** - local version control
* **GitHub** - remote version control and portfolio visibility
* **VS Code** - project development and documentation
* **Jupyter** - planned for future interactive Data Science work

Project-specific dependencies will be added only when they are actually required.

## Development Roadmap

The project is being developed incrementally alongside the IBM Data Science Professional Certificate.

1. **Business Understanding** - completed
2. **Tools, GitHub, Repository & Reproducible Environment** - completed
3. **CRISP-DM, Data Strategy & Evaluation Design** - planned next
4. **Data acquisition and analytical development** - later phases
5. **Forecasting, evaluation, capacity-planning analysis and communication** - later phases

## Important Project Risk

Reliable seat-capacity information by route and time period may not be available in public datasets.

If suitable capacity information cannot later be obtained or reasonably derived, the capacity-planning component may require redesign.

## Capacity-Planning Guardrail

High passenger demand does not automatically mean insufficient capacity.

Low passenger demand does not automatically mean excess capacity.

The relevant comparison is:

**Forecast Passenger Demand vs. Planned Seat Capacity**
