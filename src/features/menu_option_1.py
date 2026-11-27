"""
Menu option 1: find a route.
"""



import math

from src.lib.setup import get_group_settings
from src.lib.utils import find_all_paths, stop_names
from src.lib.io.trip_history import add_trip_history
from src.features.menu_option_4 import rank_paths_by_fewest_transfers

# Author: Reiniel Dan Pablo
def validate_input_stop(label):
    stop = ""
    while True:
        stop = input(f"{label}: ")
        if stop in stop_names():
            break
        elif stop == "0":
            return 0
        else:
            print(f"Sorry, {stop} is not a stop.")
            print("Choose [2] at the MAIN MENU to see all stops.")
            print("Press [0] to return to MAIN MENU.\n")
    return stop

def get_fare_breakdown(distance, passenger_type):
    """Work out a ride's fare, and the "how the fare was computed" lines for it.

    Part of a km counts as a whole km. Discount applies when
    passenger_type is "D" (student/senior/PWD).

    Returns (fare, lines).
    """
    base_fare, base_distance, fare_per_extra_km, discount_rate = get_group_settings()

    if distance <= base_distance:
        extra_km = 0
        subtotal = base_fare
        lines = [f"  {distance} km, within the {base_distance} km base fare"]
    else:
        extra_distance = distance - base_distance
        extra_km = math.ceil(extra_distance)
        subtotal = base_fare + extra_km * fare_per_extra_km
        lines = [f"  {distance} km = {base_distance} km base + {round(extra_distance, 1)} extra km (counted as {extra_km} km)"]

    subtotal_text = f"P{base_fare:.2f} + ({extra_km} x P{fare_per_extra_km:.2f}) = P{subtotal:.2f}" if extra_km else f"P{base_fare:.2f}"

    if passenger_type.upper() == "D":
        fare = round(subtotal * (1 - discount_rate / 100), 2)
        lines.append(f"  {subtotal_text}, less {discount_rate}% discount = P{fare:.2f}")
    else:
        fare = round(subtotal, 2)
        lines.append(f"  {subtotal_text}")

    return fare, lines

def get_total_fare(distance, passenger_type):
    fare, _ = get_fare_breakdown(distance, passenger_type)
    return fare



# Author: Reiniel Dan Pablo
def get_search_inputs():
    """Ask for the origin/destination stops, passenger type, and sort choice.

    Returns (origin, destination, passenger_type, sort_choice), or None if
    the user pressed [0] at any prompt to go back to the main menu.
    """
    origin = validate_input_stop("From")
    if origin == 0:
        return None

    destination = validate_input_stop("To")
    if destination == 0:
        return None

    passenger_type = ""
    while True:
        passenger_type = input("Passenger type - [R] Regular | [D] Student/Senior/PWD: ").upper()
        if passenger_type in ["R", "D"]:
            break
        elif passenger_type == "0":
            return None
        else:
            print("Invalid passenger type. Please enter either [R] or [D].")
            print("Press [0] to return to MAIN MENU.\n")

    sort_choice = ""
    while True:
        sort_choice = input("Sort by - [1] Cheapest fare | [2] Shortest distance | [3] Fewest transfers: ")
        if sort_choice in ["1", "2", "3"]:
            break
        elif sort_choice == "0":
            return None
        else:
            print("Invalid sort choice. Please enter either [1], [2], or [3].")
            print("Press [0] to return to MAIN MENU.\n")

    return origin, destination, passenger_type, sort_choice

# Author: Reiniel Dan Pablo
def find_route(origin, destination, passenger_type, sort_choice):
    """Search for every path between origin and destination and print each
    one, broken down by ride (one per route used) with distance and fare.
    """
    print("Searching...")
    paths = find_all_paths(start=origin, end=destination)

    # Fewest transfers: keep only the top 3 paths, in ranked order.
    if sort_choice == "3":
        ranked = rank_paths_by_fewest_transfers(paths)
        paths = [path for path, transfers in ranked]
    print(f"Found {len(paths)}. Sorted by SORT_TYPE_PLACEHOLDER")

    #TODO: Use sort_choice to sort the found list of possible paths to take
    # from point A to point B

    path_summaries = []

    for path_index, path in enumerate(paths, start=1):
        print(f"---------------PATH {path_index}---------------")

        # Group the path's hops into rides: a new ride starts each time the route changes.
        rides = []
        for from_stop, to_stop, distance_km, route_name in path:
            if not rides or rides[-1]["route_name"] != route_name:
                rides.append({"route_name": route_name, "distance": 0, "stops": [from_stop]})
            rides[-1]["distance"] += distance_km
            rides[-1]["stops"].append(to_stop)

        # Round away floating point noise (e.g. 3.0999999999999996) now that
        # each ride's distance is fully summed, so every print and fare
        # calculation below works off the same clean number.
        for ride in rides:
            ride["distance"] = round(ride["distance"], 1)

        total_distance = round(sum(ride["distance"] for ride in rides), 1)
        total_fare = round(sum(get_total_fare(ride["distance"], passenger_type) for ride in rides), 2)
        transfer_count = len(rides) - 1

        # The full stop-by-stop path, stitching each ride's stops together
        # without repeating the stop where one ride hands off to the next.
        full_path_stops = []
        for ride in rides:
            full_path_stops.extend(ride["stops"] if not full_path_stops else ride["stops"][1:])
        path_summaries.append({"path": " > ".join(full_path_stops), "fare": total_fare})

        print(f"#{path_index}  Php {total_fare}  |  {total_distance} km  |  {transfer_count} transfer(s)")

        for ride_index, ride in enumerate(rides, start=1):
            ride_fare = get_total_fare(ride["distance"], passenger_type)
            print(f" Ride {ride_index}: {ride['route_name']}    {ride['distance']} km.    Php {ride_fare}")
            print("\t"," > ".join(ride["stops"]))
            print("")

        print(f"How the fare of #{path_index} was computed:")
        for ride_index, ride in enumerate(rides, start=1):
            _, fare_breakdown = get_fare_breakdown(ride["distance"], passenger_type)
            print(f" Ride {ride_index}:")
            for line in fare_breakdown:
                print(line)
        print("")

    if not path_summaries:
        return

    while True:
        choice = input(f"Save which path to your trip history? (1-{len(path_summaries)}, or 0 to skip): ")
        if choice == "0":
            break
        if choice.isdigit() and 1 <= int(choice) <= len(path_summaries):
            chosen = path_summaries[int(choice) - 1]
            add_trip_history(origin, destination, chosen["path"], chosen["fare"])
            print("Trip saved to data/trip_history.csv.")
            break
        print(f"Invalid choice. Enter a number from 1 to {len(path_summaries)}, or 0 to skip.")

def show_menu_1():
    print("--- FIND A ROUTE ---")

    search_inputs = get_search_inputs()
    if search_inputs is None:
        return

    origin, destination, passenger_type, sort_choice = search_inputs
    find_route(origin, destination, passenger_type, sort_choice)
    input("Press anything to continue...")
        





