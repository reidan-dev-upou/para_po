"""
Menu option 4: most searched destinations.
"""


def show_menu_4():
    print("WIP: Menu 4")

    # Pause so this doesn't go straight back to the main menu.
    input("Press any button to continue...")



from src.lib.utils import find_all_paths, stop_names
from src.lib.io import read_csv
from src.lib.constants import DATA_DIR
file_path = DATA_DIR / "trip_history.csv"

# Author: Karol Anne Panaligan
#TO DO: Work on the ranking and testing the function in its entirety.
def get_most_searched_destinations():
    """This function retrieves the most searched destinations from the trip history CSV file.
    
    Returns trip history #a list of the most searched destinations#."""

    trip_history = read_csv(file_path)
    print(trip_history)


# Author: Mary Rose P Ramos
# Menu Option 4: Shortest Distance Feature 

def get_shortest_paths(start, end, limit=3):
    """Find and rank the shortest paths between two stops.

    Returns up to three paths arranged from shortest to longest.
    distance."""

# Get all available stop names.
    available_stops = stop_names()

    valid_start = None
    valid_end = None

# Validate the starting point and destination.
    for stop in available_stops:

        if stop.lower() == start.strip().lower():
            valid_start = stop

        if stop.lower() == end.strip().lower():
            valid_end = stop

    if valid_start is None or valid_end is None:
        return []

# Find all possible paths. 
    valid_paths = find_all_paths(valid_start, valid_end)

    if len(valid_paths) == 0:
        return []

# Calculate the distance of every path.
    ranked_paths = []

    for path in valid_paths:

        total_distance = 0
        route_names = []
        stops = []

        # Calculate the total distance.
        for hop in path:
            total_distance = total_distance + hop[2]
            route_names.append(hop[3])

        # Get the sequence of the stops.
        if len(path) > 0:
            stops.append(path[0][0])

            for hop in path:
                stops.append(hop[1])

        else:
            stops.append(valid_start)

        # Count changes between jeepney routes.
        transfers = 0

        for i in range (1, len(route_names)):
            if route_names[i] != route_names[i - 1]:
                transfers = transfers + 1

        # Store the results in a dictionary.
        path_details = {
            "path": path,
            "stops": stops,
            "total_distance": total_distance,
            "route_names": route_names,
            "transfers": transfers
        }

        ranked_paths.append(path_details)

# Sort paths from shortest to longest 
    for i in range (len(ranked_paths)):

        for j in range(0, len(ranked_paths) - i - 1):

            if ranked_paths[j]["total_distance"] > ranked_paths[j + 1]["total_distance"]:

                temporary = ranked_paths[j]
                ranked_paths[j] = ranked_paths[j + 1]
                ranked_paths[j + 1] = temporary

# Top three shortest paths.
    shortest_paths = []
    count = 0

    for path_details in ranked_paths:

        if count < limit:
            shortest_paths.append(path_details)
            count = count + 1

    return shortest_paths

