"""
Reading data/trip_cache.csv.
"""

import csv

from src.lib.constants import DATA_DIR
from src.lib.io import read_csv, append_csv

# Author: Reiniel Dan Pablo
def read_trip_cache():
    """
    Read data/trip_cache.csv, creating it with just a header if it doesn't exist yet.
    """
    file_path = DATA_DIR / "trip_cache.csv"
    if not file_path.exists():
        with open(file_path, 'w', newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(
                ["stop_a", "stop_b", "path_index", "hop_index", "from_stop", "to_stop", "distance_km", "route_name"]
            )

    return read_csv(file_path)

# Author: Reiniel Dan Pablo
def add_trip_cache(start, end, paths):
    """Cache every path found between start and end (search_recursively's output).

    One row per hop, tagged with its path and position, so it can be
    rebuilt later.

    Returns none."""
    if not start or not end or not paths:
        print("Required information not provided")
        return

    for path_index, path in enumerate(paths):
        for hop_index, (from_stop, to_stop, distance_km, route_name) in enumerate(path):
            append_csv(DATA_DIR / "trip_cache.csv", {
                "stop_a": start,
                "stop_b": end,
                "path_index": path_index,
                "hop_index": hop_index,
                "from_stop": from_stop,
                "to_stop": to_stop,
                "distance_km": distance_km,
                "route_name": route_name,
            })