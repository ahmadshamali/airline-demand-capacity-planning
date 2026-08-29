# Phase 3 — CRISP-DM, Data Strategy & Evaluation Design

## 1. Purpose

Phase 3 converts the approved airline capacity-planning business problem into a defensible analytical and data strategy before implementation begins.

The project remains a decision-support system for a single airline's Network Planning / Capacity Planning Team. It forecasts passenger volume and compares that forecast with seat capacity to identify route-periods that may require investigation. It does not make autonomous operational decisions.

---

## 2. Final Analytical Approach

### Prediction problem

The primary forecasting problem is:

> Predict next-month observed passenger volume for each directional origin-destination route operated by one airline, using only information legitimately available at forecast time.

One prediction represents:

> one airline + one directional origin -> destination route + one future month.

The model target is passenger volume, not a direct capacity label or operational action.

### Directionality

Routes are directional.

`RDU -> MIA` and `MIA -> RDU` are treated as different route series because demand can differ by direction.

### Time granularity

The original preference was weekly because monthly aggregation can hide short-term demand-capacity mismatches.

After source research, the working project granularity was changed to **monthly** because the strongest authoritative, reproducible public source that provides both passenger volume and seat capacity is BTS T-100 Segment, which is monthly.

Weekly remains the preferred real-world design if a legitimate finer-grained source becomes available later.

### Forecast horizon

Primary horizon:

> **one month ahead**

Optional later analysis may evaluate +2 and +3 month horizons separately.

### Multi-route system

The business-facing system is one multi-route forecasting system for a single airline.

The final modeling architecture is intentionally not selected in Phase 3. Later experiments may compare global, route-specific, or hybrid approaches.

---

## 3. Target Definition

### Target variable

> Future observed passenger volume for a directional route-month.

Observed passengers are used as a practical proxy for passenger demand.

### Important limitation

Observed passengers are not identical to unconstrained market demand.

If capacity is binding, some potential passengers may be unable to travel and therefore never appear in transported-passenger data. Historical observed passenger counts may therefore understate true market demand in constrained periods.

This limitation must be considered when interpreting forecasts and capacity signals.

---

## 4. Data Requirements

### Essential

- time period
- origin airport
- destination airport
- observed passenger count
- planned future seat capacity for the final real-world capacity signal
- carrier identifier when the source contains multiple airlines

### Highly useful

- historical available seats
- scheduled departures / flight frequency
- performed departures
- fare information, if valid at prediction time
- holiday / calendar variables
- seasonal variables derived from date
- operational indicators for historical understanding
- historical capacity context

### Optional / context-dependent

- aircraft type
- route distance
- additional route characteristics
- other operational or commercial variables discovered later

A variable is not automatically a valid predictor merely because it exists in the dataset. Predictor eligibility depends on whether the information would genuinely be known when the forecast is generated.

---

## 5. Candidate Data Sources Evaluated

### BTS T-100 Segment — selected primary historical source

Owner: U.S. Department of Transportation, Bureau of Transportation Statistics.

Relevant fields include:

- carrier
- origin
- destination
- passengers transported
- available seats
- scheduled departures
- performed departures
- aircraft type
- distance
- load factor

Key properties:

- non-stop segment data
- monthly frequency
- historical coverage beginning in 1990
- public and reproducible
- supports filtering to a single carrier
- supports historical passenger-capacity analysis

Main limitation:

- monthly rather than weekly/daily
- reported seats are realized historical capacity, not the airline's historical one-month-ahead planning snapshot

### BTS Reporting Carrier On-Time Performance

Useful for:

- flight-date-level operations
- carrier
- route
- delays
- cancellations
- operational context

Not selected as the passenger-demand target source because it does not provide the required route-level passenger counts and seat-capacity measures for this project.

### BTS DB1C Origin and Destination Survey

Useful for:

- passenger travel patterns
- ticket fares
- carrier
- origin/destination
- itinerary information

DB1C is a monthly 40% ticket sample beginning in July 2025.

It was not selected as the primary historical source because its history is currently short and it does not replace T-100's capacity fields.

It may later be considered as a supplementary fare / itinerary source if compatibility and leakage rules permit.

### OAG Passenger Booking / Schedule Data

Commercial aviation data can provide much richer demand and schedule information, including weekly passenger-booking delivery in some products.

It was not selected as a required project dependency because commercial access would weaken reproducibility for a public portfolio project.

### Cirium Schedule Data

Cirium provides extensive historical and forward-looking commercial schedule data and was investigated as a possible future planned-capacity source.

It was not selected as a required dependency because practical API access was not established and the product is commercial.

---

## 6. Selected Data Strategy

### Primary historical source

> **BTS T-100 Segment**

### Working unit of analysis

> **one airline + directional origin-destination route + month**

### Aggregation principle

If multiple valid T-100 records contribute to the same route-month, additive quantities such as passengers, seats, scheduled departures, and performed departures should generally be summed after confirming the original record dimensions.

Ratios such as load factor should be recomputed from the aggregated totals rather than blindly averaged.

### Specific airline

The project remains single-airline, but the specific airline is intentionally deferred to Phase 4.

Carrier selection will prioritize:

- long historical continuity
- sufficient route coverage
- reliable passenger and seat reporting
- enough observations per route
- limited major gaps
- sufficient stable routes for a meaningful multi-route system

Data quality and continuity take priority over selecting the airline with the largest possible network.

---

## 7. Capacity-Data Feasibility

### Historical capacity

Feasible.

T-100 provides historical available-seat information together with passenger volume and route/carrier identifiers.

### Planned future capacity

Public T-100 data does not provide the airline's actual one-month-ahead capacity-planning snapshot.

For the portfolio:

> realized T-100 seat capacity for the forecast month will be used only after the period as an explicitly labeled **ex-post proxy** for retrospective capacity-signal evaluation.

It must not be treated as information that was known when the forecast was generated.

In a real airline deployment:

> planned future seat capacity would be supplied by the airline's internal scheduling / capacity systems and compared with the passenger forecast at prediction time.

No future seat plan will be fabricated for the portfolio.

---

## 8. Information Availability and Leakage Rules

Every predictor must satisfy:

> Would the airline genuinely know this value when the forecast is generated?

### Allowed examples

- historical passenger counts through the forecast date
- historical seat capacity
- historical scheduled/performed departures
- historical fares when available
- route identity
- route distance
- calendar information known in advance
- holidays known in advance
- other information genuinely available at forecast time

### Not allowed

- actual passenger count from the forecast month
- realized seat capacity from the forecast month as a demand-model predictor
- realized average fare from the forecast month
- future delays or cancellations
- variables calculated using future observations
- actual intermediate future observations when simulating a multi-step forecast

Predicted future values may potentially be used by a legitimate recursive forecasting method later, but the prediction process itself must use only information available at the original forecast time.

### Capacity-related predictors

Planned future seats and planned future departures remain primarily outside the primary demand model so that the forecast is not made circular with the capacity signal being evaluated.

---

## 9. Data Understanding / Quality Inspection Plan

Later phases must inspect before cleaning:

- missing values
- true duplicate records
- multiple valid records at lower T-100 dimensions
- zero passengers
- zero seats
- passengers greater than reported seats
- route-month gaps
- route starts and stops
- newly launched routes
- discontinued routes
- seasonal routes
- irregular service
- carrier-code changes
- airport-code changes
- airline mergers / reporting changes
- extreme passenger or capacity values
- structural breaks
- pandemic-era anomalies
- other external shocks
- sparse route histories
- long periods of non-operation

### Zero-value rule

Zero passengers and/or zero seats must be investigated before deletion.

A zero may represent real non-operation, seasonal service, temporary suspension, missing reporting, or another condition.

### Missing route-month rule

A missing route-month must first be checked against route activity.

Genuine non-operation is not equivalent to missing data and must not be automatically interpolated.

### Outlier rule

Extreme values must be investigated before removal.

Valid seasonal peaks, holidays, schedule changes, or operational events may contain useful forecasting signal.

### Structural-break rule

Major shocks such as the COVID period are retained initially and evaluated before deciding whether they remain in training, receive indicators, or are excluded in specific experiments.

### Route identity rule

Airport and carrier identifiers must be validated across time. Historical code changes, mergers, and reporting changes should only be standardized when supported by authoritative mappings or documentation.

---

## 10. Route Inclusion Strategy

Initial modeling should prioritize routes with sufficient historical continuity.

The exact minimum-history requirement will be decided after Phase 4 data inspection rather than invented in Phase 3.

Route treatment:

- active route with sufficient history -> normal forecasting candidate
- active/new route with sparse history -> possible cold-start case; evaluate separately
- discontinued route -> do not forecast unless evidence shows it will restart
- seasonal route -> preserve valid seasonal non-operation rather than treating it as missing data
- route with major gaps -> investigate before inclusion

A route must be active or planned to operate during the forecast period; historical existence alone is not enough.

---

## 11. Data Preparation Plan

Later Python phases should:

1. acquire the required T-100 data reproducibly
2. inspect schema and documentation
3. select a carrier using the approved evidence-based criteria
4. keep fields required for forecasting and capacity analysis
5. standardize time, carrier, airport, and numeric fields
6. determine the original T-100 observation level
7. aggregate valid records to airline + origin + destination + month
8. investigate duplicates before removal
9. investigate missing and zero observations
10. identify route starts, stops, seasonal patterns, and gaps
11. investigate impossible or suspicious passenger/seat relationships
12. inspect outliers and structural breaks
13. determine routes with sufficient usable history
14. create calendar/seasonal information without future leakage
15. preserve chronological order
16. produce model-ready data using only forecast-time-valid information

No substantial cleaning or feature engineering was performed in Phase 3.

---

## 12. Validation Strategy

Random train/test splitting is rejected.

Evaluation must preserve time order.

### Primary approach

Use expanding or rolling one-month-ahead backtesting.

Conceptually:

- train through Month T -> forecast T+1
- extend available history -> forecast the next month
- repeat across the validation period

This simulates how the forecasting system would behave as time advances.

### Final holdout

A recent period should remain untouched during model selection and be used as a final test after the forecasting approach is chosen.

Exact calendar boundaries will be decided after data inspection.

### Route coverage

Later validation must also confirm that route inclusion and history requirements remain valid across train, validation, and test periods.

---

## 13. Baseline Strategy

The preferred baseline candidate is:

> **seasonal naive: predict a month using the same month from the previous year**

Example:

> March 2026 forecast = March 2025 observed passengers.

This is appropriate because monthly airline demand may exhibit strong annual seasonality.

Additional simple benchmarks may later include:

- previous-month naive
- a recent seasonal-history benchmark

The exact definition of "recent" should be based on observed route history rather than an arbitrary number of years.

More complex models must demonstrate improvement over simple baselines.

---

## 14. Modeling Principle

No final forecasting algorithm is selected in Phase 3.

Later modeling should compare:

1. simple baseline forecasts
2. one or more reasonable statistical / machine-learning approaches
3. the final selected approach based on evidence

The model should win because it performs better under time-aware evaluation, not because it is more advanced or fashionable.

Global, local, and hybrid route-modeling architectures remain open for later experimentation.

---

## 15. Technical Evaluation Strategy

Forecast evaluation should include both absolute and relative error.

### Recommended primary metrics

**MAE — Mean Absolute Error**

Provides operational interpretation in passenger counts.

Example interpretation:

> forecasts miss actual passenger volume by an average of X passengers per route-month.

**WAPE — Weighted Absolute Percentage Error**

Provides a relative error measure across routes with different traffic volumes.

WAPE is preferred over blindly relying on MAPE because zero and very low-demand observations can make MAPE undefined or unstable.

### Secondary diagnostic

RMSE may be considered as a secondary metric because it penalizes large forecast misses more heavily.

### Reporting levels

Performance should be evaluated:

- across the airline/network
- by individual route
- by meaningful route groups where useful

A good network-level score must not hide routes with consistently poor forecasts.

No arbitrary performance threshold is defined in Phase 3.

---

## 16. Business Evaluation Strategy

Forecast quality and business usefulness are separate evaluation dimensions.

A forecasting error must be interpreted relative to available/planned capacity.

The project should later evaluate whether forecasts help identify meaningful route-month demand-capacity mismatches and prioritize planner attention.

Two forecasts with the same passenger error may have very different planning consequences depending on seat capacity.

No monetary ROI will be invented without reliable cost/revenue information.

---

## 17. Capacity Signal Strategy

The capacity layer should conceptually compare:

> forecast passenger volume <-> planned seat capacity

while also considering forecast uncertainty.

Conceptual signal categories:

- possible insufficient capacity
- roughly aligned capacity
- possible excess capacity

No numerical thresholds are defined in Phase 3.

The system must not convert these signals directly into automatic instructions such as adding or canceling flights.

Aircraft availability, crew availability, airport slots, maintenance, economics, and schedule optimization remain outside project scope and are factors for human planners and other airline systems to investigate.

---

## 18. Forecast Uncertainty

A point forecast is an estimate, not a fact.

Later modeling should investigate an appropriate way to communicate forecast uncertainty.

Borderline demand-capacity situations should not be interpreted with the same confidence as large, clear mismatches.

Prediction intervals or other uncertainty estimates may be considered later if supported by the chosen modeling approach.

---

## 19. Conceptual Deployment and Feedback Loop

In a real airline setting:

1. generate next-month route-level passenger forecasts
2. obtain planned future seat capacity from internal airline planning systems
3. compare forecast demand with planned capacity
4. produce prioritized investigation signals
5. planners review relevant route-months
6. the operating month occurs
7. actual passenger volume becomes available
8. forecast performance is measured
9. capacity-signal usefulness is reviewed
10. model and data strategy are iterated using performance and planner feedback

This is a conceptual workflow only.

No API, dashboard, cloud system, Docker deployment, or MLOps implementation is part of Phase 3.

---

## 20. Public-Data Proxy Assumption

The project represents an internal airline decision-support system.

BTS T-100 is used as a reproducible public proxy for historical airline traffic/capacity records.

The publication delay of the public BTS dataset is not treated as the hypothetical airline's internal data latency.

When backtesting, only historical information that would conceptually have been available internally at forecast time may be used to generate forecasts.

Future actual passenger counts are used only after the forecast period to evaluate forecast quality.

---

## 21. CRISP-DM / Data Science Methodology Mapping

### Business Understanding

Completed primarily in Phase 1.

The business problem, stakeholder, project scope, decision-support purpose, and demand-capacity guardrail were already established.

### Analytic Approach

Defined as one-month-ahead directional route-level passenger forecasting followed by a separate capacity-comparison layer.

### Data Requirements

Essential, useful, optional, and forecast-time-sensitive information has been classified.

### Data Collection

Serious public and commercial aviation sources were evaluated. BTS T-100 Segment was selected as the primary historical source.

### Data Understanding

A formal inspection plan was created for data quality, route continuity, structural breaks, zeros, missing observations, code changes, and aggregation issues.

### Data Preparation

A future preparation strategy was defined without performing cleaning or feature engineering.

### Modeling

No final algorithm was selected. Baseline comparison and evidence-based model selection are required later.

### Evaluation

Time-aware backtesting, a final holdout, MAE/WAPE, route-level evaluation, and capacity-planning usefulness were defined.

### Deployment

A conceptual planner-facing monthly workflow was defined.

### Feedback

Actual future outcomes and planner feedback feed into later model review and iteration.

### Iteration

CRISP-DM is treated as iterative. Later data evidence may require revisiting route selection, preparation, modeling, or earlier assumptions.

---

## 22. Assumptions Confirmed

- the project can remain a single-airline, multi-route forecasting system
- passenger volume can be studied by directional origin-destination route
- authoritative historical passenger data is publicly available
- authoritative historical seat-capacity data is publicly available
- historical departures and other useful route information are available
- demand-capacity comparison remains a feasible project concept
- human planners remain the final decision-makers

---

## 23. Assumptions Changed or Refined

### Weekly -> monthly

Weekly was preferred for better operational precision.

It was changed to monthly for the reproducible portfolio implementation because the selected authoritative passenger/capacity source is monthly and no suitable public weekly route-passenger source was established.

### Demand terminology

The target was refined from generic "demand" to **observed passenger volume as a proxy for demand**.

### Future seat capacity

The project cannot reconstruct the airline's actual historical one-month-ahead capacity plans from T-100.

Realized seats will therefore be used only as an ex-post proxy during retrospective portfolio evaluation.

### Specific airline

Carrier selection is deferred until Phase 4 data inspection.

---

## 24. Open Questions for Later Phases

- Which specific airline best satisfies the approved coverage and continuity criteria?
- What minimum route-history requirement is justified by the actual data?
- How should cold-start/new routes be handled?
- How should pandemic-era and other structural breaks be treated experimentally?
- Which historical variables improve forecasts without leakage?
- Is DB1C fare information worth integrating after compatibility checks?
- Which modeling architecture performs best: global, local, or hybrid?
- Which final uncertainty representation works with the selected models?
- Which capacity-signal thresholds, if any, can be justified later?
- How well do ex-post capacity signals approximate real planning usefulness?

---

## 25. Phase 4 Boundary

Phase 3 does not download or clean the full dataset, perform EDA, engineer substantial features, or train models.

The recommended next phase is:

> **Phase 4 — Python Data Acquisition & Processing Foundations**

Phase 4 should begin with reproducible T-100 acquisition, schema inspection, carrier comparison, route-history inspection, and implementation of the approved preparation rules.

---

## References

1. Bureau of Transportation Statistics — T-100 Segment (U.S. Carriers Only):  
   https://www.transtats.bts.gov/TableInfo.asp?QO_fu146_anzr=Nv4+Pn44vr45&gnoyr_VQ=GDM

2. Bureau of Transportation Statistics — T-100 Domestic Segment fields:  
   https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FIM

3. Bureau of Transportation Statistics — Reporting Carrier On-Time Performance:  
   https://www.transtats.bts.gov/DL_SelectFields.aspx?QO_fu146_anzr=b0-gvzr&gnoyr_VQ=FGJ

4. Bureau of Transportation Statistics — Origin and Destination Survey (DB1B / DB1C):  
   https://www.bts.gov/topics/airlines-and-airports/origin-and-destination-survey-data

5. OAG — Passenger Booking Data:  
   https://www.oag.com/passenger-booking-data

6. Cirium — Flight Schedules and Connections Data:  
   https://www.cirium.com/data/flight-schedules/schedules-and-connections-data/
