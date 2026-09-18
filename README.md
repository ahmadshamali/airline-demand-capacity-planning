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

- **Primary historical data source:** BTS T-100 Segment (All Carriers)
- **Historical period:** January 2024 through May 2026
- **Selected carrier:** WN — Southwest Airlines Co.
- **Service scope:** `CLASS = "F"`
- **Analytical grain:** one carrier + directional origin–destination route + month
- **Primary forecast horizon:** one month ahead
- **Final operational activity rule:** `DEPARTURES_PERFORMED > 0`
- **Phase 4.1:** complete
- **Phase 4.2:** complete
- **Phase 4.3:** technically complete; pending final Master Chat approval

### Completed

- Phase 1 — Business Understanding & Problem Definition
- Phase 2 — Tools, GitHub, Repository & Reproducible Environment
- Phase 3 — CRISP-DM, Data Strategy & Evaluation Design
- Phase 4.1 — BTS T-100 Segment acquisition and structural verification
- Phase 4.2 — carrier investigation, Southwest selection, route recurrence analysis, and route-eligibility design
- Phase 4.3 — raw-grain investigation, directional route-month aggregation, activity definition, reusable processing pipeline, and leakage-safe eligibility integration

### Route-Month Foundation

The validated WN `CLASS = "F"` foundation contains:

- **55,395** source-observed directional route-months
- **4,271** directional routes
- **29** calendar months
- coverage from **2024-01 through 2026-05**
- **55,376** operationally active route-months
- **19** source-observed inactive route-months
- **119** zero-passenger route-months that still had performed service

Operational activity is defined as:

`DEPARTURES_PERFORMED > 0`

Route eligibility at forecast origin `t` requires:

- at least **6 historical active months before `t`**
- activity during at least one of the **previous 3 calendar months**

The reusable processing implementation is located in:

`src/data_processing.py`

A validated processed artifact is generated locally at:

`data/processed/wn_route_month.csv`

Raw and processed bulk data remain excluded from Git tracking.

### Not Yet Completed

The project has not yet implemented:

- forecasting features
- target shifting
- chronological backtesting implementation
- baseline forecasting
- model training
- model evaluation
- demand-capacity signal implementation

No forecasting model has been built yet.

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
│   ├── 01_data_acquisition.ipynb
│   ├── 02_carrier_investigation.ipynb
│   ├── 03_route_month_foundation.ipynb
│   └── README.md
├── reports/
│   └── README.md
├── src/
│   ├── README.md
│   └── data_processing.py
├── .gitignore
└── README.md
```

## Directory Purpose

* `data/` - data-handling documentation and local raw/processed datasets
* `docs/` - project decisions, methodology, and tooling documentation
* `notebooks/` - reproducible analytical notebooks for acquisition, investigation, and route-month foundation work
* `reports/` - polished figures and project outputs
* `src/` - reusable project processing code

## Data Handling

Raw and processed bulk datasets are excluded from Git tracking.

The project uses BTS T-100 Segment (All Carriers) data covering January 2024 through May 2026.

The selected analytical scope is:

- carrier: `WN` — Southwest Airlines Co.
- service class: `CLASS = "F"`
- directional route-month grain

Raw source files are stored locally under:

`data/raw/`

The validated processed route-month foundation is stored locally under:

`data/processed/wn_route_month.csv`

Both raw and processed bulk data remain Git-ignored and are not committed to the repository.

The processed dataset is reproducibly generated from the local raw BTS files using:

`src/data_processing.py`

## Tools

Current project tools include:

* **Python 3.14.7** - data processing and analysis
* **pandas 3.0.5** - tabular data processing and aggregation
* **Jupyter** - interactive analysis and reproducible notebooks
* **VS Code** - project development and documentation
* **Git** - local version control
* **GitHub** - remote version control and portfolio visibility
* **project `.venv`** - isolated Python environment

Direct project dependencies are documented in:

`requirements.txt`

The current direct dependencies are:

* `pandas==3.0.5`
* `ipykernel==7.3.0`

## Development Roadmap

The project is being developed incrementally alongside the IBM Data Science Professional Certificate.

1. **Business Understanding** - completed
2. **Tools, GitHub, Repository & Reproducible Environment** - completed
3. **CRISP-DM, Data Strategy & Evaluation Design** - completed
4. **Data Acquisition, Carrier Investigation & Route-Month Foundation** - completed through Phase 4.3
5. **Feature Engineering, Forecasting & Chronological Evaluation** - later project work
6. **Demand-Capacity Analysis & Decision-Support Signals** - later project work

## Important Project Limitation

BTS T-100 provides historical passenger volume and realized historical seat capacity by route and month.

The route-month foundation therefore retains `SEATS` as a historical operational measure.

However, realized seats from the forecast month are not approved as a passenger-demand predictor because they would not represent information available before that month occurred.

BTS T-100 also does not provide the airline's actual future planned-capacity snapshot that would have been available at a historical forecast origin.

Any later retrospective comparison using realized T-100 seat capacity must therefore be explicitly treated as an ex-post capacity comparison.

In a real airline deployment, planned future capacity would come from the airline's internal scheduling or capacity-planning systems.

## Capacity-Planning Guardrail

High passenger demand does not automatically imply insufficient capacity.

Low passenger demand does not automatically imply excess capacity.

The eventual decision-support comparison is:

**Forecast Passenger Demand vs. Planned Seat Capacity**