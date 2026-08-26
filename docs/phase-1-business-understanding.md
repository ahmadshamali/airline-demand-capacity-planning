# Phase 1 - Business Understanding

## Project

**Airline Passenger Demand Forecasting & Capacity Planning**

The project models a single airline operating multiple routes and is intended to support airline network and capacity planning decisions.

## Primary Stakeholder

The primary stakeholder is the:

**Network Planning / Capacity Planning Team**

The team needs information about:

- expected passenger demand by route and time period

- available or planned seat capacity

- potential mismatches between expected demand and capacity

The system is intended to support investigation of whether planners should consider:

- increasing capacity

- maintaining capacity

- reducing capacity

- making seasonal capacity adjustments

The system does not make operational decisions automatically.

## Business Problem

Passenger demand varies across routes and over time, making it difficult for an airline to determine appropriate seat capacity in advance.

Incorrect capacity decisions may result in:

- excessive capacity and empty seats

- insufficient capacity and missed passenger demand

- lost revenue opportunities

- inefficient operations

Capacity-planning decisions must therefore consider the relationship between expected passenger demand and available or planned seat capacity.

## Data Science Objective

Use historical airline data to estimate future passenger demand for each route and time period so that the Capacity Planning Team can identify potential capacity mismatches and begin investigating adjustments before the demand occurs.

No forecasting algorithm has been selected at this stage.

## Conceptual Unit of Analysis

The conceptual unit of analysis is:

**Origin-destination route over a time period**

Weekly analysis is currently a conceptual preference, but the final time granularity has not been fixed.

The final granularity will depend on the dataset selected in a later phase.

## Project Scope

### In Scope

Future project work may include:

- historical passenger-demand analysis by route and time

- passenger-demand forecasting

- comparison of forecast demand with available or planned capacity

- identification of possible demand-capacity mismatches

- capacity-planning decision-support signals

- historical and seasonal demand-pattern analysis

- route-level planning insights

### Out of Scope

The project will not perform:

- automatic aircraft assignment

- fleet-assignment optimization

- aircraft-routing optimization

- crew scheduling

- airport-slot optimization

- automatic flight cancellation

- automatic flight addition

- full airline scheduling optimization

- revenue-management algorithms

- dynamic ticket-pricing optimization

- autonomous operational decisions

## Key Assumptions

At this stage, the project assumes that:

- historical demand patterns may contain useful information for forecasting

- route-level analysis is an appropriate conceptual level

- useful seat-capacity information may be obtainable

- seasonal or recurring demand patterns may exist

These assumptions have not yet been validated.

## Key Risk - Capacity Data Availability

The largest known project risk is the availability of reliable seat-capacity information by route and time period.

Public datasets may not contain sufficient capacity information.

If suitable capacity information cannot later be obtained or reasonably derived, the capacity-planning component may need to be redesigned.

This issue is intentionally deferred to later data and methodology phases.

## Important Capacity-Planning Guardrail

Passenger volume alone does not determine whether capacity is sufficient.

High passenger demand does not automatically mean insufficient capacity, and low passenger demand does not automatically mean excess capacity.

The relevant relationship is:

**Forecast Passenger Demand vs. Planned Seat Capacity**

A high-volume route may still have excess capacity if planned seat supply is even higher.

A lower-volume route may still have insufficient capacity if planned seat supply is below expected demand.

## Current Phase Status

Phase 1 business understanding has been defined and approved.

Dataset selection, data validation, forecasting methodology, modeling, and capacity analysis have not yet been performed.

