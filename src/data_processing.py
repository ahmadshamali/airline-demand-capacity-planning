import pandas as pd


def _validate_required_columns(df, required_columns):
    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

def filter_project_scope(df):
    """
    Filters the DataFrame to include only rows that are within the project scope.
    The project scope is defined as rows where:

    - UNIQUE_CARRIER = WN
    - CLASS = F

    Then validate identity:
    - AIRLINE_ID == 19393
    - UNIQUE_CARRIER_NAME == "Southwest Airlines Co."

    Parameters:
    df (pd.DataFrame): Raw BTS historical data.

    Returns:
    pd.DataFrame: A filtered DataFrame containing only rows within the project scope.
    """
    required_columns = [
        "UNIQUE_CARRIER",
        "AIRLINE_ID",
        "UNIQUE_CARRIER_NAME",
        "CLASS",
        "YEAR",
        "MONTH",
        "ORIGIN",
        "DEST",
        "PASSENGERS",
        "SEATS",
        "DEPARTURES_SCHEDULED",
        "DEPARTURES_PERFORMED",
        "DISTANCE",
    ]

    _validate_required_columns(df, required_columns)

    filtered_df = df.loc[
        (df['CLASS'] == 'F') &
        (df["UNIQUE_CARRIER"] == "WN") ,
        required_columns
    ].copy()

    if filtered_df.empty:
        raise ValueError(
            "No rows found for project scope: "
            "UNIQUE_CARRIER='WN' and CLASS='F'."
        )

    airline_ids = set(filtered_df["AIRLINE_ID"].unique())

    if airline_ids != {19393}:
        raise ValueError(
            f"Unexpected AIRLINE_ID values for WN/F scope: {airline_ids}"
        )
    
    carrier_names = set(filtered_df["UNIQUE_CARRIER_NAME"].unique())

    if carrier_names != {"Southwest Airlines Co."}:
        raise ValueError(
            f"Unexpected UNIQUE_CARRIER_NAME values for WN/F scope: {carrier_names}"
        )
    

    return filtered_df


def _validate_distance_consistency(df):
    """
    Validate that each route-month has exactly one distinct DISTANCE.

    Parameters:
    df (pd.DataFrame): Filtered WN/F raw data.

    Returns:
    None
    """
    distance_check = df.groupby(
        ['YEAR', 'MONTH','ORIGIN', 'DEST']
    )['DISTANCE'].nunique()

    inconsistent_routes = distance_check[distance_check > 1]

    if not inconsistent_routes.empty:
        raise ValueError(
            "Conflicting DISTANCE values found within route-month groups."
        )

def _validate_no_missing_values(df):
    """
    Validate that required analytical fields contain no missing values.

    """
    required_columns = [
        "UNIQUE_CARRIER",
        "AIRLINE_ID",
        "UNIQUE_CARRIER_NAME",
        "YEAR",
        "MONTH",
        "ORIGIN",
        "DEST",
        "PASSENGERS",
        "SEATS",
        "DEPARTURES_SCHEDULED",
        "DEPARTURES_PERFORMED",
        "DISTANCE"
    ]

    missing_values = df[required_columns].isnull().sum()
    missing_columns = missing_values[missing_values > 0].index.tolist()

    if missing_columns:
        raise ValueError(
            f"Missing values found in required columns: {missing_columns}"
        )

def _validate_non_negative_values(df):
    """
    Validate that operational numeric fields contain no negative values.
    """
    numeric_columns = [
        "PASSENGERS",
        "SEATS",
        "DEPARTURES_SCHEDULED",
        "DEPARTURES_PERFORMED",
        "DISTANCE",
    ]

    negative_counts = (df[numeric_columns] < 0).sum()
    negative_counts = negative_counts[negative_counts > 0]

    if not negative_counts.empty:
        raise ValueError(
            f"Negative values found in required numeric columns:\n{negative_counts}"
        )

def _validate_additive_reconciliation(input_df, route_month_df):
    """
    Validate that route-month aggregation preserves additive totals.
    """
    additive_columns = [
        "PASSENGERS",
        "SEATS",
        "DEPARTURES_SCHEDULED",
        "DEPARTURES_PERFORMED"
    ]

    input_totals = input_df[additive_columns].sum()
    route_month_totals = route_month_df[additive_columns].sum()

    if not input_totals.equals(route_month_totals):
        raise ValueError(
            f"Additive reconciliation failed. Input totals:\n{input_totals}\nRoute-month totals:\n{route_month_totals}"
        )

def get_eligible_routes(route_month_df, forecast_origin):
    """
Return directional routes eligible at a given forecast origin.

A route must have at least 6 active historical months and be active
at least once during the previous 3 calendar months.

Parameters:
    route_month_df (pd.DataFrame): Validated route-month foundation.
    forecast_origin: Monthly forecast origin as a Pandas Period or
        a value convertible to one.

Returns:
    pd.DataFrame: Eligible ORIGIN-DEST routes with historical active-month counts.
"""
    min_historical_active_months = 6
    recency_window_months = 3

    required_columns = [
        "YEAR_MONTH",
        "ORIGIN",
        "DEST",
        "IS_ACTIVE",
    ]

    _validate_required_columns(route_month_df, required_columns)

    ## Ensure forecast_origin is a pandas Period with monthly frequency
    if not isinstance(forecast_origin, pd.Period):
        forecast_origin = pd.Period(forecast_origin, freq="M")

    if forecast_origin.freqstr != "M":
        raise ValueError(
            "forecast_origin must represent a monthly period."
        )
    
    ## Filter the route-month dataset to include only historical active months before the forecast origin
    historical_active = route_month_df.loc[
        (route_month_df["YEAR_MONTH"] < forecast_origin) &
        (route_month_df["IS_ACTIVE"])
    ].copy()

    ## Count the number of historical active months for each route
    historical_counts = (
    historical_active
    .groupby(["ORIGIN", "DEST"])
    .size()
    .reset_index(name="HISTORICAL_ACTIVE_MONTHS")
    )

    ## Filter to only include routes with at least 6 historical active months
    history_eligible = historical_counts.loc[
    historical_counts["HISTORICAL_ACTIVE_MONTHS"] >= min_historical_active_months 
    ].copy()

    ## Filter the historical active dataset to include only the last 3 months before the forecast origin
    recent_start = forecast_origin - recency_window_months 

    recent_active = historical_active.loc[
        historical_active["YEAR_MONTH"] >= recent_start
    ]

    recent_routes = (
        recent_active[
            ["ORIGIN", "DEST"]
        ]
        .drop_duplicates()
    )
    ### Merge the historical eligible routes with the recent active routes to get the final eligible routes
    eligible_routes = ( 
        history_eligible
        .merge(
            recent_routes,
            on=["ORIGIN", "DEST"],
            how="inner"
        )
        .sort_values(by=["ORIGIN", "DEST"])
        .reset_index(drop=True)
    )

    return eligible_routes


def build_route_month_dataset(df):
    """
Build the validated WN route-month foundation from raw BTS history.

Parameters:
    df (pd.DataFrame): Raw BTS historical data.

Returns:
    pd.DataFrame: Validated route-month dataset with YEAR_MONTH and IS_ACTIVE.
"""
    filtered_df = filter_project_scope(df)

    ## Validate the filtered dataset for missing values, non-negative values, and distance consistency
    _validate_no_missing_values(filtered_df)
    _validate_non_negative_values(filtered_df)
    _validate_distance_consistency(filtered_df)
    

    route_month_df = filtered_df.groupby(

        [
            'UNIQUE_CARRIER',
            'YEAR',
            'MONTH',
            'ORIGIN',
            'DEST'
        ]

        ).agg({
        'PASSENGERS': 'sum',
        'SEATS': 'sum',
        'DEPARTURES_SCHEDULED': 'sum',
        'DEPARTURES_PERFORMED': 'sum',
        'AIRLINE_ID': 'first',
        'UNIQUE_CARRIER_NAME': 'first',
        'DISTANCE': 'first'
        }).reset_index()
    
    ## Create a YEAR_MONTH column for time series analysis
    route_month_df['YEAR_MONTH'] = pd.PeriodIndex.from_fields(
    year=route_month_df['YEAR'],
    month=route_month_df['MONTH'],
    freq='M'
    )

    ### Create an IS_ACTIVE column to indicate if the route-month is active
    route_month_df["IS_ACTIVE"] = (
    route_month_df["DEPARTURES_PERFORMED"] > 0
    )

    ## Check for duplicates in the analytical key columns
    key_columns = [
        "UNIQUE_CARRIER",
        "YEAR",
        "MONTH",
        "ORIGIN",
        "DEST",
    ]

    
    duplicate_count = route_month_df.duplicated(
    subset=key_columns
    ).sum()

    if duplicate_count > 0:
        raise ValueError(
        f"Route-month dataset contains {duplicate_count} duplicate analytical keys."
        )

    route_month_df = route_month_df[
    [
        "UNIQUE_CARRIER",
        "AIRLINE_ID",
        "UNIQUE_CARRIER_NAME",
        "YEAR",
        "MONTH",
        "YEAR_MONTH",
        "ORIGIN",
        "DEST",
        "PASSENGERS",
        "SEATS",
        "DEPARTURES_SCHEDULED",
        "DEPARTURES_PERFORMED",
        "DISTANCE",
        "IS_ACTIVE"
    ]
]

    ## Validate additive reconciliation between the input filtered dataset and the aggregated route-month dataset
    _validate_additive_reconciliation(filtered_df, route_month_df)

    return route_month_df

