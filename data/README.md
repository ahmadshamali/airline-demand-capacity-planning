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

Phase 4.2 carrier investigation and route-history analysis are complete.

Phase 4.3 route-month foundation, activity definition, reusable processing, and eligibility integration are complete pending final Master Chat approval.

## Service-Class and Activity Scope

`CLASS = F` is the project's scheduled passenger-service scope.

During Phase 4.2, `PASSENGERS > 0` was used specifically for exploratory route-recurrence analysis.

The final operational activity definition established in Phase 4.3 is:

`DEPARTURES_PERFORMED > 0`

This definition preserves source-observed route-months where service was performed even when reported passenger volume was zero.

In the final WN route-month foundation:

- **55,395** source-observed route-months are present
- **55,376** are operationally active
- **19** are source-observed but inactive
- **119** have zero passengers but positive performed departures

Absent route-months are not artificially inserted or zero-filled.

## Raw Data

Original BTS downloads are stored under:

`data/raw/`

Raw source files are preserved unchanged after acquisition and remain local.

Raw data files are excluded from Git tracking.

The T-100 Segment (All Carriers) source has been acquired for the January 2024 through May 2026 historical period.

The selected analytical scope is:

- carrier: `WN` — Southwest Airlines Co.
- service scope: `CLASS = F`
- analytical grain: directional route-month

## Processed Data

The validated processed route-month foundation is stored locally under:

`data/processed/wn_route_month.csv`

The processed dataset contains:

- **55,395 rows**
- **14 columns**
- **4,271 directional routes**
- **29 calendar months**
- coverage from **2024-01 through 2026-05**

`YEAR_MONTH` is serialized as `YYYY-MM`.

`IS_ACTIVE` is derived from:

`DEPARTURES_PERFORMED > 0`

Raw and processed bulk datasets remain excluded from Git tracking.