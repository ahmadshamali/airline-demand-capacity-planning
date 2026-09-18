# Source Code

This directory contains reusable Python code for the airline passenger-demand
forecasting and capacity-planning project.

## data_processing.py

Provides reusable processing logic for converting raw BTS T-100 Segment data
into the validated Southwest Airlines route-month foundation.

### Main Functions

- `filter_project_scope(df)`
  - Filters raw data to `UNIQUE_CARRIER == "WN"` and `CLASS == "F"`.
  - Validates the expected Southwest carrier identity.

- `build_route_month_dataset(df)`
  - Validates the selected source data.
  - Aggregates raw BTS rows to directional route-month grain.
  - Constructs `YEAR_MONTH`.
  - Defines `IS_ACTIVE` using `DEPARTURES_PERFORMED > 0`.
  - Performs structural and additive reconciliation checks.

- `get_eligible_routes(route_month_df, forecast_origin)`
  - Uses only active observations before the forecast origin.
  - Requires at least 6 historical active months.
  - Requires activity in at least one of the previous 3 calendar months.
  - Returns eligible directional routes.

## Processed Data

The validated route-month foundation is written locally to:

`data/processed/wn_route_month.csv`

Processed data is Git-ignored and is not committed to the repository.