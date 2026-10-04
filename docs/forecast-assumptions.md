# Forecast and Scenario Assumptions

## Purpose

This document describes the assumptions used for the workforce-planning scenarios in the Operational Resource Planning Dashboard.

## Baseline

The baseline scenario represents the staffing and workload values contained in the cleaned workforce-planning dataset.

The dataset includes simulated operations for three locations:

- Dallas
- Chicago
- Miami

Each location contains:

- Morning shifts
- Afternoon shifts
- Evening shifts

The dataset covers a 30-day period.

## Workload Scenarios

The project evaluates four workload scenarios:

- 0% growth
- 5% growth
- 10% growth
- 15% growth

The 0% scenario represents the current synthetic baseline.

The other scenarios represent hypothetical increases in operational workload.

## Staffing Requirement Assumption

The scenario model assumes that staffing requirements increase approximately in proportion to workload growth.

For example, if workload increases by 10%, the model increases the baseline staffing requirement by approximately 10%.

This is a simplified planning assumption used to demonstrate scenario analysis.

It is not intended to represent an actual airline staffing formula.

## Scheduled Staffing Assumption

For scenario analysis, currently scheduled staffing is held constant.

This allows the model to answer the question:

"What could happen to staffing coverage if workload increases but staffing levels do not change?"

## Staffing Gap

Staffing gap is calculated as:

Scheduled Staff - Required Staff

A negative staffing gap indicates an estimated shortage.

A positive staffing gap indicates scheduled staffing is above the modeled requirement.

## Coverage Rate

Coverage rate is calculated as:

Scheduled Staff / Required Staff × 100

A lower coverage rate indicates greater staffing pressure.

## Coverage Risk

The project uses the following demonstration thresholds:

- High Risk: coverage below 85%
- Medium Risk: coverage from 85% to below 100%
- Low Risk: coverage of 100% or greater

These thresholds are project assumptions and are not official airline operating thresholds.

## Limitations

The scenario model is intentionally simple.

It does not account for factors such as:

- Employee qualifications
- Employee availability
- Overtime restrictions
- Labor agreements
- Absences
- Shift swaps
- Weather
- Flight disruptions
- Seasonal demand
- Aircraft type
- Station-specific operating rules

A real production resource-planning model would require more detailed operational data and business rules.

## Intended Use

The scenarios are designed to demonstrate how data analysis can help an operations team evaluate potential staffing risks and compare possible resource-planning actions before operational demand changes.