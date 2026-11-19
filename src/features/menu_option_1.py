"""
Menu option 1: find a route.
"""


def show_menu_1():
    print("WIP: Menu 1")

    # Pause so this doesn't go straight back to the main menu.
    input("Press any button to continue...")

# Author: Karol Anne Panaligan
from src.lib.io import read_csv, write_csv
from src.lib.constants import DATA_DIR
file_path = DATA_DIR / "trip_history.csv"

def save_trip_history(date, origin, destination, chosen_path, fare):
    if (not date or not origin or not destination or not chosen_path or not fare):
        print("Required information not provided")
        return

    trip_history = read_csv(file_path)
    print (trip_history)

    trip = {
        "date": date,
        "origin": origin,
        "destination": destination,
        "chosen_path": chosen_path,
        "fare": fare}

    result = write_csv(file_path, trip)
    if result is not None:
        print("Trip saved successfully!")
    else:
        print("Unable to save trip details.")
