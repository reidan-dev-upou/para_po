"""
Menu option 4: most searched destinations.
"""


def show_menu_4():
    print("WIP: Menu 4")

    # Pause so this doesn't go straight back to the main menu.
    input("Press any button to continue...")



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


# Author: Dan Louis Faurillo
def rank_paths_by_fewest_transfers(valid_paths):
    """Rank paths by fewest transfers, then shortest total distance.

    valid_paths: A list of paths, each containing
        (from_stop, to_stop, distance_km, route_name) tuples.

    Returns up to three (path, transfers) pairs.
    Returns an empty list if no paths are available.
    """
    if not valid_paths:
        # The caller handles displaying the no-route message.
        return []

    ranked_paths = []

    for path in valid_paths:
        transfers = 0
        total_distance = 0
        previous_route = None

        for from_stop, to_stop, distance_km, route_name in path:
            total_distance += distance_km

            # Initial boarding is not a transfer.
            if previous_route is not None and route_name != previous_route:
                transfers += 1

            previous_route = route_name

        ranked_paths.append((path, transfers, total_distance))

    # Prefer shorter distance when transfer counts are equal.
    ranked_paths.sort(key=lambda entry: (entry[1], entry[2]))

    results = []
    for path, transfers, total_distance in ranked_paths[:3]:
        results.append((path, transfers))

    return results


   
