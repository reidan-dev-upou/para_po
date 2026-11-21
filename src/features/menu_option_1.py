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


# Author: Kayleen Rosette Lagunday
from src.lib.io import read_members_info, read_routes

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

def calculate_route_distance(routes, origin, destination):
    origin = origin.strip().lower()
    destination = destination.strip().lower()
    if origin == destination:
        return 0.0

    route_groups = {}
    for route in routes:
        route_name = route["route_name"]
        if route_name not in route_groups:
            route_groups[route_name] = []
        route_groups[route_name].append(route)

    for segments in route_groups.values():
        stops = [segments[0]["stop_a"]]
        stops.extend(segment["stop_b"] for segment in segments)
        for start_index, stop in enumerate(stops):
            if stop.strip().lower() != origin:
                continue

            total_distance = 0.0
            for i in range(start_index, len(segments)):
                segment = segments[i]
                total_distance = total_distance + float(segment["distance_km"])
                if segment["stop_b"].strip().lower() == destination:
                    return total_distance
    return None

def main():
    members = read_members_info()
    routes = read_routes()
    student_numbers = [
        member["student_number"].strip()
        for member in members
        if member.get("student_number", "").strip()]
    
    group_seed = compute_group_seed(student_numbers)
    base_fare, base_distance, fare_per_extra_km, discount_rate = get_group_settings(group_seed)

    origin = input("Enter starting point: ")
    destination = input("Enter destination: ")

    total_distance = calculate_route_distance(routes,origin,destination)

    if total_distance is None:
        print("No route found. Please check your starting point and destination.")
    elif total_distance == 0.0:
        print("Starting point and destination cannot be the same.")

    return {
        "group_seed": group_seed,
        "base_fare": base_fare,
        "base_distance": base_distance,
        "fare_per_extra_km": fare_per_extra_km,
        "discount_rate": discount_rate,
        "origin": origin,
        "destination": destination,
        "total_distance": total_distance}

if __name__ == "__main__":
    main()