"""
Reading and writing data/routes.csv.
"""

from src.lib.constants import DATA_DIR
from src.lib.io import read_csv, overwrite_csv, append_csv

# Author: Reiniel Dan Pablo
def read_routes():
    """
    Read data/routes.csv
    """
    return read_csv(DATA_DIR / "routes.csv")

# Author: Reiniel Dan Pablo
def overwrite_routes(new_routes_data):
    """
    Overwrite data/routes.csv with new_routes_data.
    """
    overwrite_csv(DATA_DIR / "routes.csv", new_routes_data)

# Author: Reiniel Dan Pablo
# TODO: Add author - JP
def add_route(new_route):
    """
    Add a new segment row (route_name, stop_a, stop_b, distance_km) to routes.csv.
    Rejects missing fields, a non-positive distance, a stop connected to itself,
    and a segment that already exists (in either direction) for that route.
    """
    required_keys = ("route_name", "stop_a", "stop_b", "distance_km")
    if not all(new_route.get(key) for key in required_keys):
        print("Required route information not provided")
        return

    if new_route["stop_a"] == new_route["stop_b"]:
        print("Stop A and Stop B cannot be the same stop")
        return

    try:
        distance = float(new_route["distance_km"])
        if distance <= 0:
            raise ValueError
    except ValueError:
        print("Distance must be a number greater than 0")
        return

    routes = read_routes()
    for route in routes:
        same_stops = {route["stop_a"], route["stop_b"]} == {new_route["stop_a"], new_route["stop_b"]}
        if route["route_name"] == new_route["route_name"] and same_stops:
            print("This segment already exists for this route")
            return

    append_csv(DATA_DIR / "routes.csv", new_route)

# Author: Reiniel Dan Pablo
# TODO: Add author - JP
def remove_route(route_to_remove):
    """
    Remove the segment row matching route_to_remove (route_name, stop_a, stop_b)
    from routes.csv, in either stop direction.
    """
    required_keys = ("route_name", "stop_a", "stop_b")
    if not all(route_to_remove.get(key) for key in required_keys):
        print("Required route information not provided")
        return

    routes = read_routes()
    remaining_routes = []
    removed = False
    for route in routes:
        same_stops = {route["stop_a"], route["stop_b"]} == {route_to_remove["stop_a"], route_to_remove["stop_b"]}
        if route["route_name"] == route_to_remove["route_name"] and same_stops:
            removed = True
            continue
        remaining_routes.append(route)

    if not removed:
        print("Segment not found")
        return

    overwrite_routes(remaining_routes)
