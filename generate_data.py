import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)


# -------------------------------------------------
# CONFIGURATION
# -------------------------------------------------

stations = [
    "Dallas",
    "Chicago",
    "Miami"
]

shifts = [
    "Morning",
    "Afternoon",
    "Evening"
]

start_date = datetime(2026, 9, 1)

number_of_days = 30


# -------------------------------------------------
# GENERATE WORKFORCE DATA
# -------------------------------------------------

records = []

record_id = 1

for day_offset in range(number_of_days):

    current_date = start_date + timedelta(
        days=day_offset
    )

    day_of_week = current_date.strftime(
        "%A"
    )

    for station in stations:

        for shift in shifts:

            # -------------------------------------
            # CREATE SYNTHETIC WORKLOAD
            # -------------------------------------

            if shift == "Morning":
                base_workload = 145

            elif shift == "Afternoon":
                base_workload = 125

            else:
                base_workload = 100


            # Dallas is our largest simulated
            # operation.
            if station == "Dallas":
                station_adjustment = 25

            elif station == "Chicago":
                station_adjustment = 15

            else:
                station_adjustment = 5


            # Weekend workload adjustment
            if day_of_week in [
                "Saturday",
                "Sunday"
            ]:
                weekend_adjustment = 20

            else:
                weekend_adjustment = 0


            workload = (
                base_workload
                + station_adjustment
                + weekend_adjustment
                + random.randint(-15, 15)
            )


            # -------------------------------------
            # REQUIRED STAFF
            # -------------------------------------

            # Simple planning assumption:
            # approximately one worker for
            # every 15 workload units.

            required_staff = max(
                5,
                round(workload / 15)
            )


            # -------------------------------------
            # SCHEDULED STAFF
            # -------------------------------------

            staffing_variation = random.choice(
                [
                    -3,
                    -2,
                    -2,
                    -1,
                    -1,
                    0,
                    0,
                    0,
                    1,
                    1,
                    2
                ]
            )

            scheduled_staff = max(
                1,
                required_staff
                + staffing_variation
            )


            # -------------------------------------
            # HOURS
            # -------------------------------------

            hours_available = (
                scheduled_staff * 8
            )

            workload_hours = (
                workload * 0.45
            )

            hours_scheduled = min(
                hours_available,
                round(
                    workload_hours,
                    1
                )
            )


            # -------------------------------------
            # COVERAGE RATE
            # -------------------------------------

            coverage_rate = round(
                (
                    scheduled_staff
                    / required_staff
                ) * 100,
                1
            )


            # -------------------------------------
            # STAFFING GAP
            # -------------------------------------

            staffing_gap = (
                scheduled_staff
                - required_staff
            )


            # -------------------------------------
            # UTILIZATION
            # -------------------------------------

            if hours_available > 0:

                utilization = round(
                    (
                        hours_scheduled
                        / hours_available
                    ) * 100,
                    1
                )

            else:

                utilization = 0


            # -------------------------------------
            # COVERAGE RISK
            # -------------------------------------

            if coverage_rate < 85:
                coverage_risk = "High"

            elif coverage_rate < 100:
                coverage_risk = "Medium"

            else:
                coverage_risk = "Low"


            records.append(
                {
                    "record_id": record_id,
                    "date": current_date.strftime(
                        "%Y-%m-%d"
                    ),
                    "day_of_week": day_of_week,
                    "station": station,
                    "shift": shift,
                    "workload": workload,
                    "required_staff": required_staff,
                    "scheduled_staff": scheduled_staff,
                    "staffing_gap": staffing_gap,
                    "coverage_rate": coverage_rate,
                    "hours_available": hours_available,
                    "hours_scheduled": hours_scheduled,
                    "utilization": utilization,
                    "coverage_risk": coverage_risk
                }
            )

            record_id += 1


# -------------------------------------------------
# CREATE DATAFRAME
# -------------------------------------------------

workforce_df = pd.DataFrame(
    records
)


# -------------------------------------------------
# CREATE RAW DATASET
# -------------------------------------------------

raw_df = workforce_df.copy()


# Intentional quality issue:
# extra spaces around a station name.
raw_df.loc[4, "station"] = " Dallas "


# Intentional quality issue:
# inconsistent shift capitalization.
raw_df.loc[12, "shift"] = "morning"


# Intentional quality issue:
# inconsistent risk capitalization.
raw_df.loc[20, "coverage_risk"] = "medium"


# Intentional quality issue:
# duplicate record.
raw_df = pd.concat(
    [
        raw_df,
        raw_df.iloc[[0]]
    ],
    ignore_index=True
)


# -------------------------------------------------
# SAVE RAW DATA
# -------------------------------------------------

raw_df.to_csv(
    "data/workforce_planning_raw.csv",
    index=False
)


# -------------------------------------------------
# DISPLAY SUMMARY
# -------------------------------------------------

print(
    "Synthetic RAW workforce planning data "
    "created successfully."
)

print()

print(
    f"Raw records created: "
    f"{len(raw_df)}"
)

print(
    f"Date range: "
    f"{raw_df['date'].min()} "
    f"to "
    f"{raw_df['date'].max()}"
)

print(
    f"Stations represented: "
    f"{raw_df['station'].nunique()}"
)

print(
    f"Shifts represented: "
    f"{raw_df['shift'].nunique()}"
)

print()

print(
    "Intentional data-quality issues "
    "were added for cleaning practice."
)