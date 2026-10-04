-- =================================================
-- OPERATIONAL RESOURCE PLANNING ANALYSIS
-- =================================================


-- -------------------------------------------------
-- 1. OVERALL KPI SUMMARY
-- -------------------------------------------------

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
        AS overall_coverage_rate,

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

FROM workforce_planning;


-- -------------------------------------------------
-- 2. STATION PERFORMANCE
-- -------------------------------------------------

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

ORDER BY coverage_rate ASC;


-- -------------------------------------------------
-- 3. SHIFT PERFORMANCE
-- -------------------------------------------------

SELECT
    shift,

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

GROUP BY shift

ORDER BY total_workload DESC;


-- -------------------------------------------------
-- 4. DAILY STAFFING TREND
-- -------------------------------------------------

SELECT
    date,

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
        AS coverage_rate

FROM workforce_planning

GROUP BY date

ORDER BY date;


-- -------------------------------------------------
-- 5. HIGH-RISK SHIFTS
-- -------------------------------------------------

SELECT
    date,
    day_of_week,
    station,
    shift,
    workload,
    required_staff,
    scheduled_staff,
    staffing_gap,
    coverage_rate,
    utilization

FROM workforce_planning

WHERE coverage_risk = 'High'

ORDER BY
    coverage_rate ASC,
    workload DESC;


-- -------------------------------------------------
-- 6. WEEKDAY VS WEEKEND
-- -------------------------------------------------

SELECT
    CASE
        WHEN day_of_week IN (
            'Saturday',
            'Sunday'
        )
        THEN 'Weekend'
        ELSE 'Weekday'
    END
        AS day_type,

    ROUND(
        AVG(workload),
        1
    )
        AS average_workload,

    ROUND(
        AVG(coverage_rate),
        1
    )
        AS average_coverage,

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
        AS understaffed_shifts

FROM workforce_planning

GROUP BY day_type;