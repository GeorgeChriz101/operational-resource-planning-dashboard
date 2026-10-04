# Operational Resource Planning Metric Definitions

## Purpose

This document defines the workforce-planning metrics used in the Operational Resource Planning Dashboard.

## Total Workload

**Definition:** The total modeled operational workload across all dates, stations, and shifts.

Workload is a synthetic unit representing operational demand.

A larger workload generally creates a larger modeled staffing requirement.

## Required Staff

**Definition:** The modeled number of employees required to support the operational workload.

The synthetic model uses approximately one worker for every 15 workload units.

This is a portfolio assumption and is not an actual airline staffing formula.

## Scheduled Staff

**Definition:** The number of employees modeled as scheduled for a station and shift.

Scheduled staffing may be:

- Below required staffing
- Equal to required staffing
- Above required staffing

## Staffing Gap

**Formula:**

Scheduled Staff - Required Staff

A negative number indicates a staffing shortage.

Example:

Required Staff = 12  
Scheduled Staff = 9

Staffing Gap = -3

This means the shift is modeled as three employees below the staffing requirement.

A positive value indicates staffing above the modeled requirement.

## Coverage Rate

**Formula:**

Scheduled Staff / Required Staff × 100

Example:

Scheduled Staff = 9  
Required Staff = 10

Coverage Rate = 90%

Coverage rate shows how much of the modeled staffing requirement is covered by scheduled staff.

## Coverage Risk

The project uses the following demonstration thresholds:

- High Risk: coverage below 85%
- Medium Risk: coverage from 85% to below 100%
- Low Risk: coverage of 100% or greater

These thresholds are project assumptions and are not official airline operating thresholds.

## Utilization

**Formula:**

Hours Scheduled / Hours Available × 100

Utilization estimates how much of the modeled available workforce capacity is being used.

Higher utilization indicates that scheduled resources are being used more heavily.

## Understaffed Shift

A shift is classified as understaffed when:

Staffing Gap < 0

The Understaffed Shifts KPI counts the number of station-and-shift records meeting this condition.

## High-Risk Shift

A shift is considered High Risk when its coverage rate is below the project threshold of 85%.

The High-Risk Shifts KPI counts the number of records classified as High Risk.

## Workload Growth Scenario

The forecast page evaluates hypothetical workload increases of:

- 0%
- 5%
- 10%
- 15%

Scheduled staffing is held constant while required staffing increases with modeled workload.

This demonstrates what could happen if operational demand increases without a corresponding staffing adjustment.

## Projected Staffing Gap

**Formula:**

Current Scheduled Staff - Projected Required Staff

A larger negative value indicates a greater potential staffing shortage under the selected workload scenario.

## Projected Coverage Rate

**Formula:**

Current Scheduled Staff / Projected Required Staff × 100

As projected workload and required staffing increase while current staffing remains fixed, projected coverage generally decreases.

## Interpretation

These metrics are designed to help answer questions such as:

- Where are staffing shortages occurring?
- Which stations have greater coverage risk?
- Which shifts have heavier resource utilization?
- How does staffing coverage change over time?
- How sensitive is staffing coverage to increases in workload?