"""
Menu option 1: find a route.
"""


def show_menu_1():
    print("WIP: Menu 1")

    # Pause so this doesn't go straight back to the main menu.
    input("Press any button to continue...")

from src.lib.io import read_csv, write_csv
from src.lib.constants import DATA_DIR
file_path = DATA_DIR / "trip_history.csv"

# Author: Karol Anne Panaligan
# TO DO: Merge this with menu 1 and test

def save_trip_history(date, origin, destination, chosen_path, fare):
    """This function saves the trip history to a CSV file.
    
    Uses the following input details: date, origin, destination, chosen_path, fare
    
    Returns none."""
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
