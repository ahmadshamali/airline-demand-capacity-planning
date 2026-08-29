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

The working unit of analysis is:

**One airline + directional origin–destination route + month**

Routes are directional, so `RDU → MIA` and `MIA → RDU` are treated as separate route series.

Monthly granularity was selected because the primary historical data source, BTS T-100 Segment, provides authoritative passenger and seat-capacity information at monthly frequency.

The primary forecast horizon is one month ahead.

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

- **Primary historical data source:** BTS T-100 Segment
- **Working unit of analysis:** directional origin–destination route per month
- **Primary forecast horizon:** one month ahead
- **Next phase:** Phase 4 — Python Data Acquisition & Processing Foundations

### Completed

- Phase 1 — Business Understanding & Problem Definition
- Phase 2 — Tools, GitHub, Repository & Reproducible Environment
- Phase 3 — CRISP-DM, Data Strategy & Evaluation Design
- primary historical data-source selection
- analytical approach and target definition
- data-requirements specification
- data-quality inspection plan
- data-leakage rules
- temporal validation strategy
- baseline and evaluation strategy
- capacity-signal and feedback-loop design

### Not Yet Completed

- dataset acquisition
- specific airline selection
- route-history inspection
- data cleaning and preparation
- exploratory data analysis
- statistical analysis
- feature engineering
- forecasting model development
- model evaluation
- capacity-signal implementation
- dashboards
- deployment

BTS T-100 Segment has been selected as the primary historical data source. No final forecasting algorithm has been selected yet.

## Repository Structure

```text
airline-demand-capacity-planning/
├── data/
│   └── README.md
├── docs/
│   ├── phase-1-business-understanding.md
│   ├── phase-3-methodology.md
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

BTS T-100 Segment has been selected as the primary historical data source. The dataset has not yet been acquired or added to the project.

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
3. **CRISP-DM, Data Strategy & Evaluation Design** - completed
4. **Python Data Acquisition & Processing Foundations** - next
5. **Forecasting, evaluation, capacity-planning analysis and communication** - later phases

## Important Project Limitation

BTS T-100 provides historical passenger volume and historical available-seat capacity by route and month.

However, it does not provide the airline's actual planned future seat-capacity snapshot that would have been available when a historical forecast was generated.

For retrospective portfolio evaluation, realized T-100 seat capacity will therefore be used only as an explicitly labeled ex-post proxy.

In a real airline deployment, planned future seat capacity would come from the airline's internal scheduling or capacity-planning systems.

## Capacity-Planning Guardrail

High passenger demand does not automatically mean insufficient capacity.

Low passenger demand does not automatically mean excess capacity.

The relevant comparison is:

**Forecast Observed Passenger Volume vs. Planned Seat Capacity**