import pandas as pd


RAW_FILE = (
    "data/workforce_planning_raw.csv"
)

CLEAN_FILE = (
    "data/workforce_planning_clean.csv"
)


# -------------------------------------------------
# LOAD RAW DATA
# -------------------------------------------------

df = pd.read_csv(
    RAW_FILE
)

raw_record_count = len(df)


# -------------------------------------------------
# CHECK DUPLICATES BEFORE CLEANING
# -------------------------------------------------

duplicate_count = df.duplicated(
    subset=["record_id"]
).sum()


# -------------------------------------------------
# STANDARDIZE TEXT FIELDS
# -------------------------------------------------

df["station"] = (
    df["station"]
    .str.strip()
    .str.title()
)

df["shift"] = (
    df["shift"]
    .str.strip()
    .str.title()
)

df["coverage_risk"] = (
    df["coverage_risk"]
    .str.strip()
    .str.title()
)


# -------------------------------------------------
# CONVERT DATE
# -------------------------------------------------

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)


# Rebuild day-of-week from the date instead
# of trusting the raw text field.

df["day_of_week"] = (
    df["date"]
    .dt.day_name()
)


# -------------------------------------------------
# VALIDATE NUMERIC COLUMNS
# -------------------------------------------------

numeric_columns = [
    "workload",
    "required_staff",
    "scheduled_staff",
    "hours_available",
    "hours_scheduled"
]


for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# -------------------------------------------------
# REMOVE DUPLICATE RECORDS
# -------------------------------------------------

df = df.drop_duplicates(
    subset=["record_id"],
    keep="first"
)


# -------------------------------------------------
# REMOVE RECORDS MISSING CRITICAL FIELDS
# -------------------------------------------------

critical_columns = [
    "record_id",
    "date",
    "station",
    "shift",
    "workload",
    "required_staff",
    "scheduled_staff"
]


df = df.dropna(
    subset=critical_columns
)


# -------------------------------------------------
# RECALCULATE DERIVED METRICS
# -------------------------------------------------

df["staffing_gap"] = (
    df["scheduled_staff"]
    - df["required_staff"]
)


df["coverage_rate"] = (
    (
        df["scheduled_staff"]
        / df["required_staff"]
    )
    * 100
).round(1)


df["utilization"] = (
    (
        df["hours_scheduled"]
        / df["hours_available"]
    )
    * 100
).round(1)


def assign_coverage_risk(
    coverage_rate
):

    if coverage_rate < 85:
        return "High"

    elif coverage_rate < 100:
        return "Medium"

    else:
        return "Low"


df["coverage_risk"] = (
    df["coverage_rate"]
    .apply(assign_coverage_risk)
)


# -------------------------------------------------
# SORT CLEAN DATA
# -------------------------------------------------

df = df.sort_values(
    by=[
        "date",
        "station",
        "shift"
    ]
)


# -------------------------------------------------
# SAVE CLEAN DATA
# -------------------------------------------------

df.to_csv(
    CLEAN_FILE,
    index=False,
    date_format="%Y-%m-%d"
)


# -------------------------------------------------
# CLEANING REPORT
# -------------------------------------------------

clean_record_count = len(df)

print("=" * 50)
print("WORKFORCE DATA CLEANING REPORT")
print("=" * 50)

print()

print(
    f"Raw records: "
    f"{raw_record_count}"
)

print(
    f"Duplicate IDs detected: "
    f"{duplicate_count}"
)

print(
    f"Clean records: "
    f"{clean_record_count}"
)

print(
    f"Records removed: "
    f"{raw_record_count - clean_record_count}"
)

print()

print(
    "Text fields standardized."
)

print(
    "Dates validated."
)

print(
    "Numeric fields validated."
)

print(
    "Derived metrics recalculated."
)

print()

print(
    f"Clean file created: "
    f"{CLEAN_FILE}"
)