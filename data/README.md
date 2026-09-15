# Data Directory

This directory is reserved for datasets used by the project.

## Structure

Project data may be organized into:

- `raw/` - original source data kept unchanged after acquisition
- `processed/` - cleaned or transformed data produced during later project phases

## GitHub Data Policy

Raw and processed datasets are excluded from Git tracking by default.

This helps prevent accidentally committing:

- large data files
- private or sensitive data
- licensed or restricted datasets
- generated intermediate datasets

Small, non-sensitive example files may be committed later when there is a clear reason to include them.

## Current Data Source

The approved primary historical data source is the U.S. Department of Transportation Bureau of Transportation Statistics (BTS) T-100 data.

The table used for the project is:

- **Table:** T-100 Segment (All Carriers)
- **Frequency:** Monthly
- **Unit represented by the source:** Directional nonstop segment activity
- **Carrier scope during acquisition:** All carriers
- **Acquisition method:** Official BTS TranStats download interface
- **Historical investigation period:** January 2024 through May 2026
- **Selected project carrier:** WN — Southwest Airlines Co.

Phase 4.1 data acquisition and structural verification are complete.

Phase 4.2 carrier investigation and route-history analysis are analytically complete and awaiting final documentation closure.

Phase 4.3 is next.

## Service-Class and Active-Route Scope

`CLASS = F` represents scheduled passenger/cargo service and is the project's scheduled passenger-service scope.

For the Phase 4.2 active passenger-route recurrence investigation, `PASSENGERS > 0` was used to identify route-month observations with realized passenger activity.

This `PASSENGERS > 0` filter applies specifically to the Phase 4.2 active passenger-route recurrence investigation.

The final treatment of zero-passenger scheduled route-months is deferred to Phase 4.3 and has not yet been decided.

## Raw Data

Original BTS downloads are stored under:

`data/raw/`

Raw source files are preserved unchanged after acquisition and remain local.

Raw data files are excluded from Git tracking.

The T-100 Segment (All Carriers) source has been acquired and investigated for the January 2024 through May 2026 historical period.

## Processed Data

Future cleaned or transformed datasets will be stored under:

`data/processed/`

No final route-month modeling dataset has been built yet.

Construction of the modeling dataset and the final treatment of zero-passenger scheduled route-months are deferred to Phase 4.3.