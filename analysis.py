import pandas as pd


df = pd.read_csv(
    "data/workforce_planning.csv"
)


print("=" * 50)
print("WORKFORCE PLANNING DATA SUMMARY")
print("=" * 50)

print()

print(
    f"Total Records: {len(df)}"
)

print(
    f"Total Workload: "
    f"{df['workload'].sum()}"
)

print(
    f"Required Staff: "
    f"{df['required_staff'].sum()}"
)

print(
    f"Scheduled Staff: "
    f"{df['scheduled_staff'].sum()}"
)

print(
    f"Average Coverage Rate: "
    f"{df['coverage_rate'].mean():.1f}%"
)

print(
    f"Average Utilization: "
    f"{df['utilization'].mean():.1f}%"
)

print(
    f"Understaffed Shifts: "
    f"{(df['staffing_gap'] < 0).sum()}"
)

print(
    f"High-Risk Shifts: "
    f"{(df['coverage_risk'] == 'High').sum()}"
)

print()

print("Records by Station:")

print(
    df[
        "station"
    ].value_counts()
)

print()

print("Records by Shift:")

print(
    df[
        "shift"
    ].value_counts()
)