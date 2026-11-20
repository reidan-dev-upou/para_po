"""
Menu option 1: find a route.
"""


def show_menu_1():
    print("WIP: Menu 1")

    # Pause so this doesn't go straight back to the main menu.
    input("Press any button to continue...")

# Author: Karol Anne Panaligan
# TO DO: Merge this with menu 1 and test
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


# Author: Kayleen Rosette Lagunday
from src.lib.constants import DATA_DIR
from src.lib.io import read_csv
file_path = DATA_DIR / "members.csv"

def read_members_info():
  return [r["student_number"].strip() for r in read_csv(file_path) if r.get("student_number", "").strip()]

def compute_group_seed(student_numbers):
  group_seed = 0
  for student_number in student_numbers:
    individual_seed = int(student_number[-4:])
    group_seed = group_seed + individual_seed
  return group_seed

def get_group_settings(seed):
  base_fare = 11 + (seed % 5)
  base_distance = 3 + (seed % 3)
  fare_per_extra_km = 1.50 + (seed % 4) * 0.25
  discount_rate = 15 + (seed % 3) * 5
  return base_fare, base_distance, fare_per_extra_km, discount_rate

if __name__ == "__main__":
  student_numbers = read_members_info()
  group_seed = compute_group_seed(student_numbers)
  base_fare, base_distance, fare_per_extra_km, discount_rate = get_group_settings(group_seed)

def read_routes():
  return read_csv(DATA_DIR / "routes.csv")
routes = read_routes()