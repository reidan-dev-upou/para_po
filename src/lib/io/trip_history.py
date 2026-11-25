"""
Reading and saving data/trip_history.csv.
"""

import csv
from datetime import datetime

from src.lib.constants import DATA_DIR
from src.lib.io import read_csv, append_csv

# Author: Karol Anne Panaligan
def read_trip_history():
    """
    Read data/trip_history.csv, creating it with just a header if it doesn't exist yet.
    """
    file_path = DATA_DIR / "trip_history.csv"
    if not file_path.exists():
        with open(file_path, 'w', newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(["date", "origin", "destination", "chosen_path", "fare"])

    return read_csv(file_path)

# Author: Karol Anne Panaligan, Reiniel Dan PAblo
def add_trip_history(origin, destination, chosen_path, fare):
    """This function appends a trip to data/trip_history.csv without rewriting existing rows.

    date is generated at call time (for example "2026-11-24 23:22:21").

    Uses the following input details: origin, destination, chosen_path, fare

    Returns none."""
    if not origin or not destination or not chosen_path or not fare:
        print("Required information not provided")
        return

    append_csv(DATA_DIR / "trip_history.csv", {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "origin": origin,
        "destination": destination,
        "chosen_path": chosen_path,
        "fare": fare,
    })
    print("Trip saved successfully!")
