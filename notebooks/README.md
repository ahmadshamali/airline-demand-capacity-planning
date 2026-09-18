# Notebooks

This directory contains the Jupyter notebooks used for project acquisition, validation, investigation, and route-month foundation work.

## Current Notebooks

### `01_data_acquisition.ipynb`

Phase 4.1 notebook for acquiring and structurally verifying the U.S. DOT BTS T-100 Segment (All Carriers) source.

Phase 4.1 is complete.

### `02_carrier_investigation.ipynb`

Phase 4.2 notebook for carrier investigation, route recurrence and continuity analysis, selection of WN — Southwest Airlines Co., and design of a leakage-safe route-eligibility framework.

The historical investigation covers January 2024 through May 2026.

Phase 4.2 is complete.

The `PASSENGERS > 0` activity definition used in this notebook belongs to the Phase 4.2 exploratory recurrence analysis. The final operational activity definition was established later in Phase 4.3.

### `03_route_month_foundation.ipynb`

Phase 4.3 notebook for:

- raw T-100 grain and multiplicity investigation
- directional route-month aggregation
- analytical schema validation
- final operational activity definition
- reusable processing-pipeline validation
- leakage-safe route-eligibility validation
- processed route-month artifact validation

The final operational activity rule is:

`DEPARTURES_PERFORMED > 0`

The validated route-month foundation contains:

- **55,395** source-observed route-months
- **4,271** directional routes
- **29** calendar months
- coverage from **2024-01 through 2026-05**

Phase 4.3 is technically complete pending final Master Chat approval.

## Current Project Boundary

- BTS T-100 Segment (All Carriers) has been acquired and investigated.
- The selected carrier is **WN — Southwest Airlines Co.**
- The service scope is `CLASS = F`.
- Raw source files remain local and Git-ignored.
- The validated processed route-month foundation is stored locally under `data/processed/wn_route_month.csv`.
- Processed bulk data remains Git-ignored.
- No forecasting features or forecasting models have been implemented yet.