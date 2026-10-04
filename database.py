import sqlite3

import pandas as pd


DATABASE = (
    "data/resource_planning.db"
)

CLEAN_FILE = (
    "data/workforce_planning_clean.csv"
)


def create_database():

    df = pd.read_csv(
        CLEAN_FILE
    )

    connection = sqlite3.connect(
        DATABASE
    )

    df.to_sql(
        "workforce_planning",
        connection,
        if_exists="replace",
        index=False
    )


    connection.execute(
        """
        CREATE INDEX IF NOT EXISTS
        idx_workforce_station
        ON workforce_planning(station)
        """
    )


    connection.execute(
        """
        CREATE INDEX IF NOT EXISTS
        idx_workforce_date
        ON workforce_planning(date)
        """
    )


    connection.execute(
        """
        CREATE INDEX IF NOT EXISTS
        idx_workforce_shift
        ON workforce_planning(shift)
        """
    )


    connection.commit()

    connection.close()

    print(
        "Resource planning database "
        "created successfully."
    )

    print(
        f"Records loaded: {len(df)}"
    )

    print(
        "Table: workforce_planning"
    )


if __name__ == "__main__":
    create_database()