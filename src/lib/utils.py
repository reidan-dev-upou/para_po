"""
Small shared helpers used by more than one feature: input validation,
formatting, and the like.
"""

# Author: Reiniel Dan Pablo
def build_graph(routes):
    """
    Turn the flat rows from read_routes() into an adjacency dict for
    find_all_paths: each stop maps to a list of (neighbor_stop,
    distance_km, route_name). A jeepney can be ridden either way, so
    each route row adds a neighbor link in both directions.
    """
    graph = {}
    for route in routes:
        stop_a = route["stop_a"]
        stop_b = route["stop_b"]
        distance_km = float(route["distance_km"])
        route_name = route["route_name"]

        # Make sure each stop has a neighbor list before adding to it.
        if stop_a not in graph:
            graph[stop_a] = []
        if stop_b not in graph:
            graph[stop_b] = []

        graph[stop_a].append((stop_b, distance_km, route_name))
        graph[stop_b].append((stop_a, distance_km, route_name))

    return graph

# Author: Reiniel Dan Pablo
def find_all_paths(graph, current_stop, destination_stop, path_so_far=None):
    """
    Recursively find every possible path from current_stop to
    destination_stop, without ever visiting the same stop twice.

    graph: a dict where each stop maps to a list of its neighbors, like
        {"Cubao": [("Kamuning", 1.2, "Route 1"), ...]}
        (neighbor_stop, distance_km, route_name)

    Returns a list of paths. Each path is a list of "segment" dicts, one
    per ride taken, with keys: from_stop, to_stop, distance_km, route_name.
    """
    # Avoid the mutable-default-argument trap.
    if path_so_far is None:
        path_so_far = []

    # Base case: we're at the destination, so this path is complete.
    if current_stop == destination_stop:
        return [path_so_far]

    # A stop is visited if we started there or already rode to it.
    visited_stops = {current_stop}
    for segment in path_so_far:
        visited_stops.add(segment["from_stop"])

    found_paths = []
    for neighbor_stop, distance_km, route_name in graph.get(current_stop, []):
        if neighbor_stop in visited_stops:
            continue

        segment = {
            "from_stop": current_stop,
            "to_stop": neighbor_stop,
            "distance_km": distance_km,
            "route_name": route_name,
        }

        # Recursive case: take that ride, then keep searching from there.
        new_path_so_far = path_so_far + [segment]
        found_paths += find_all_paths(graph, neighbor_stop, destination_stop, new_path_so_far)

    return found_paths
