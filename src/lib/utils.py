"""
Small shared helpers used by more than one feature: input validation,
formatting, and the like.
"""

import math

from src.lib.io.routes import read_routes
from src.lib.io.stops import read_stops
from src.lib.io.trip_cache import read_trip_cache, add_trip_cache
from src.lib.setup import get_group_settings

# Author: Reiniel Dan Pablo
def stop_names():
    return [stop["stop_name"] for stop in read_stops()]


# Author: Reiniel Dan Pablo
def build_route_graph():
    """Turn the routes.csv rows into a map of each stop's neighbors.

    Each stop lists the stops you can ride to from it, with the distance
    and route name. Works both ways, and skips repeats so the same
    stretch isn't added twice.
    """
    graph = {}
    seen_pairs = set()
    for row in read_routes():
        stop_a, stop_b = row["stop_a"], row["stop_b"]
        pair = frozenset((stop_a, stop_b))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)

        distance_km = float(row["distance_km"])
        route_name = row["route_name"]
        graph.setdefault(stop_a, []).append((stop_b, distance_km, route_name))
        graph.setdefault(stop_b, []).append((stop_a, distance_km, route_name))
    return graph

# Author: Reiniel Dan Pablo
def check_travel_cache(start, end):
    """Look up data/trip_cache.csv for paths already found between start and end.

    Checks both directions (start -> end and end -> start), rebuilding each
    cached path back into the same shape search_recursively returns: a list
    of paths, each path a list of (from_stop, to_stop, distance_km,
    route_name) hops. Returns None if this pair of stops hasn't been
    searched before.
    """
    matching_rows = [row for row in read_trip_cache() if {row["stop_a"], row["stop_b"]} == {start, end}]
    if not matching_rows:
        return None

    # A cached search was done in one direction (its stop_a); if we're asked
    # for the other direction, each path needs to be walked backwards.
    is_reversed = matching_rows[0]["stop_a"] != start

    hops_by_path = {}
    for row in matching_rows:
        path_index = int(row["path_index"])
        hop_index = int(row["hop_index"])
        hop = (row["from_stop"], row["to_stop"], float(row["distance_km"]), row["route_name"])
        hops_by_path.setdefault(path_index, {})[hop_index] = hop

    paths = []
    for path_index in sorted(hops_by_path):
        hops_by_position = hops_by_path[path_index]
        hops = [hops_by_position[position] for position in range(len(hops_by_position))]
        if is_reversed:
            hops = [(to_stop, from_stop, distance_km, route_name)
                    for (from_stop, to_stop, distance_km, route_name) in reversed(hops)]
        paths.append(hops)
    return paths

# Author: Reiniel Dan Pablo
# TODO: Karol and Kayleen add as authors
def search_recursively(graph, start, end, visited=None):
    """Find every way to get from start to end without passing the same stop twice.

    Each path it returns is a list of stops, showing the distance and
    route name used for every leg of the trip.
    """
    if visited is None:
        visited = {start}

    # Base case: reached the destination, so the only path from here is empty.
    if start == end:
        return [[]]

    # Recursive case: try every unvisited neighbor, and build this stop's
    # paths by sticking the hop to that neighbor onto whatever paths it
    # finds from there to end.
    paths = []
    for neighbor, distance_km, route_name in graph.get(start, []):
        if neighbor in visited:
            continue
        for sub_path in search_recursively(graph, neighbor, end, visited | {neighbor}):
            paths.append([(start, neighbor, distance_km, route_name)] + sub_path)
    return paths

# Author: Reiniel Dan Pablo
# TODO: Karol and Kayleen add as authors
def find_all_paths(start, end):
    """Find every way to get from start to end, reusing a cached trip if there is one.

    Checks the cache first; if start/end was already searched, returns
    that instead of searching again. Otherwise searches fresh and caches
    the result for next time.
    """
    cached = check_travel_cache(start, end)
    if cached is not None:
        return cached

    graph = build_route_graph()
    paths = search_recursively(graph, start, end, visited=None)
    add_trip_cache(start, end, paths)
    return paths

