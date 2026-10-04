# Operational Resource Planning Dashboard

A workforce-planning and operations analytics portfolio project built with Python, pandas, SQL, SQLite, Excel, and Power BI.

## Overview

This project simulates an operational resource-planning workflow using synthetic workforce, workload, staffing, coverage, and utilization data.

The project demonstrates how raw operational records can be cleaned, transformed, analyzed, summarized, and presented through an interactive Power BI dashboard.

It also includes Excel reporting, staffing-gap analysis, workload-growth scenarios, and an executive recommendation.

## Technologies

- Python
- pandas
- SQL
- SQLite
- Excel
- openpyxl
- Power BI
- DAX
- Git
- GitHub

## Project Workflow

```text
Synthetic Workforce Data
        ↓
Python / pandas
        ↓
Data Cleaning and Transformation
        ↓
SQLite
        ↓
SQL Analysis
        ↓
Excel Reporting
        ↓
Power BI Dashboard
        ↓
Forecast Scenarios
        ↓
Executive Recommendation
```

## Dataset

The synthetic dataset contains 30 days of modeled operations across:

- Dallas
- Chicago
- Miami

Each station contains:

- Morning shifts
- Afternoon shifts
- Evening shifts

The dataset includes fields such as:

- Date
- Day of week
- Station
- Shift
- Workload
- Required staff
- Scheduled staff
- Staffing gap
- Coverage rate
- Hours available
- Hours scheduled
- Utilization
- Coverage risk

## Data Cleaning

`generate_data.py` creates a synthetic raw workforce-planning dataset.

The raw dataset intentionally contains several data-quality issues for cleaning practice, including:

- Duplicate records
- Inconsistent capitalization
- Extra whitespace
- Inconsistent category formatting

`clean_data.py` uses pandas to:

- Remove duplicate records
- Standardize station and shift values
- Validate dates
- Validate numeric fields
- Recalculate staffing metrics
- Recalculate coverage risk
- Produce an analysis-ready dataset

## SQL Analysis

`database.py` loads the cleaned dataset into a local SQLite database.

`sql/resource_analysis.sql` contains queries for:

- Overall staffing KPIs
- Station performance
- Shift performance
- Daily staffing trends
- High-risk shifts
- Weekday versus weekend comparisons

The project demonstrates SQL concepts including:

- SELECT
- WHERE
- SUM
- AVG
- GROUP BY
- ORDER BY
- CASE
- Aggregate calculations

## Excel Reporting

`export_excel.py` creates:

`output/resource_planning_analysis.xlsx`

The workbook contains:

- Executive Summary
- Station Analysis
- Shift Analysis
- Daily Trend
- High Risk Shifts
- Forecast Scenarios
- Clean Data

## Power BI Dashboard

The Power BI report is located at:

`powerbi/Operational_Resource_Planning_Dashboard.pbix`

### Operations Overview

The first report page includes:

- Total Workload
- Required Staff
- Scheduled Staff
- Staffing Gap
- Coverage Rate
- Average Utilization
- Understaffed Shifts
- High-Risk Shifts
- Required versus scheduled staffing by station
- Daily staffing coverage trend
- Utilization by shift
- Coverage risk by station
- High-risk shift details
- Station and shift slicers

### Forecast Scenarios

The second page evaluates hypothetical workload increases of:

- 0%
- 5%
- 10%
- 15%

It displays:

- Projected required staffing
- Current scheduled staffing
- Projected staffing gap
- Projected coverage rate
- Projected risk

## Scenario Analysis

The scenario model holds scheduled staffing constant while increasing workload and required staffing.

This answers a simple resource-planning question:

"What could happen to staffing coverage if operational workload increases but staffing levels do not change?"

These scenarios are what-if analyses and are not predictions.

## Executive Recommendation

An executive-style summary is included in:

`docs/executive-recommendation.md`

The PowerPoint version is stored in:

`presentation/Operational_Resource_Planning_Executive_Summary.pptx`

## Documentation

Metric definitions:

`docs/metric-definitions.md`

Forecast assumptions:

`docs/forecast-assumptions.md`

Executive recommendation:

`docs/executive-recommendation.md`

## Installation

Clone the repository:

```bash
git clone https://github.com/GeorgeChriz101/operational-resource-planning-dashboard.git
```

Enter the project:

```bash
cd operational-resource-planning-dashboard
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Rebuild the Analysis

Generate the synthetic raw data:

```bash
python generate_data.py
```

Clean and transform the dataset:

```bash
python clean_data.py
```

Build the SQLite database:

```bash
python database.py
```

Run the SQL/Python analysis:

```bash
python analysis.py
```

Generate the Excel workbook:

```bash
python export_excel.py
```

## Concepts Demonstrated

### Workforce Planning

- Staffing demand
- Scheduled staffing
- Staffing gaps
- Coverage rates
- Resource utilization
- Coverage risk
- Scenario planning

### Data Analytics

- Data cleaning
- Data transformation
- Data validation
- Aggregation
- KPI development
- Trend analysis
- Data visualization

### Business Intelligence

- DAX measures
- KPI cards
- Interactive slicers
- Staffing comparisons
- Trend charts
- Risk analysis
- Scenario visualization
