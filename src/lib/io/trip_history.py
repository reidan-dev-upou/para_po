"""
Reading and saving data/trip_history.csv.
"""

from src.lib.constants import DATA_DIR
from src.lib.io import read_csv, append_csv

# Author: Karol Anne Panaligan
def read_trip_history():
    """
    Read data/trip_history.csv
    """
    return read_csv(DATA_DIR / "trip_history.csv")

# Author: Karol Anne Panaligan
def add_trip_history(date, origin, destination, chosen_path, fare):
    """This function appends a trip to data/trip_history.csv without rewriting existing rows.

    Uses the following input details: date, origin, destination, chosen_path, fare

    Returns none."""
    if not date or not origin or not destination or not chosen_path or not fare:
        print("Required information not provided")
        return

    append_csv(DATA_DIR / "trip_history.csv", {
        "date": date,
        "origin": origin,
        "destination": destination,
        "chosen_path": chosen_path,
        "fare": fare,
    })
    print("Trip saved successfully!")
