import sqlite3

import pandas as pd


DATABASE = (
    "data/resource_planning.db"
)


connection = sqlite3.connect(
    DATABASE
)


# -------------------------------------------------
# OVERALL KPI SUMMARY
# -------------------------------------------------

overall_summary = pd.read_sql_query(
    """
    SELECT
        SUM(workload)
            AS total_workload,

        SUM(required_staff)
            AS required_staff,

        SUM(scheduled_staff)
            AS scheduled_staff,

        ROUND(
            SUM(scheduled_staff) * 100.0
            / SUM(required_staff),
            1
        )
            AS coverage_rate,

        ROUND(
            AVG(utilization),
            1
        )
            AS average_utilization,

        SUM(
            CASE
                WHEN staffing_gap < 0
                THEN 1
                ELSE 0
            END
        )
            AS understaffed_shifts,

        SUM(
            CASE
                WHEN coverage_risk = 'High'
                THEN 1
                ELSE 0
            END
        )
            AS high_risk_shifts

    FROM workforce_planning
    """,
    connection
)


# -------------------------------------------------
# STATION SUMMARY
# -------------------------------------------------

station_summary = pd.read_sql_query(
    """
    SELECT
        station,

        SUM(workload)
            AS total_workload,

        SUM(required_staff)
            AS required_staff,

        SUM(scheduled_staff)
            AS scheduled_staff,

        SUM(scheduled_staff)
            - SUM(required_staff)
            AS staffing_gap,

        ROUND(
            SUM(scheduled_staff) * 100.0
            / SUM(required_staff),
            1
        )
            AS coverage_rate,

        ROUND(
            AVG(utilization),
            1
        )
            AS average_utilization

    FROM workforce_planning

    GROUP BY station

    ORDER BY coverage_rate ASC
    """,
    connection
)


# -------------------------------------------------
# SHIFT SUMMARY
# -------------------------------------------------

shift_summary = pd.read_sql_query(
    """
    SELECT
        shift,

        SUM(workload)
            AS total_workload,

        SUM(required_staff)
            AS required_staff,

        SUM(scheduled_staff)
            AS scheduled_staff,

        ROUND(
            SUM(scheduled_staff) * 100.0
            / SUM(required_staff),
            1
        )
            AS coverage_rate,

        ROUND(
            AVG(utilization),
            1
        )
            AS average_utilization

    FROM workforce_planning

    GROUP BY shift

    ORDER BY total_workload DESC
    """,
    connection
)


connection.close()


# -------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------

print()
print("=" * 60)
print("OPERATIONAL RESOURCE PLANNING SUMMARY")
print("=" * 60)

print()

print(overall_summary.to_string(
    index=False
))

print()

print("=" * 60)
print("STATION PERFORMANCE")
print("=" * 60)

print()

print(station_summary.to_string(
    index=False
))

print()

print("=" * 60)
print("SHIFT PERFORMANCE")
print("=" * 60)

print()

print(shift_summary.to_string(
    index=False
))