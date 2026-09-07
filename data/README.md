# Data Directory

This directory is reserved for datasets used by the project.

## Structure

Future data may be organized into:

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

For Phase 4.1, the selected table is:

- **Table:** T-100 Segment (All Carriers)
- **Frequency:** Monthly
- **Unit represented by the source:** Directional nonstop segment activity
- **Carrier scope during acquisition:** All carriers
- **Acquisition method:** Official BTS TranStats download interface
- **Source reference:** https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=Nv4+Pn44vr45&gnoyr_VQ=FMG

The final airline has not yet been selected. Carrier investigation belongs to Phase 4.2.

## Raw Data

Original BTS downloads are stored under:

`data/raw/`

Raw source files are preserved unchanged after acquisition and are excluded from Git tracking.

The initial verification extract covers January 2024 and was downloaded as a ZIP archive containing a CSV file.

The January 2024 extract is used only to verify acquisition, loading, and source structure. It does not define the final historical modeling period.

## Processed Data

Future cleaned or transformed datasets will be stored under:

`data/processed/`

No processed dataset has been created during Phase 4.1.

