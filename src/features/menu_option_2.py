"""
Menu option 2: view all stops.
"""

from src.lib.io import read_stops

def get_stop_names(stop_rows):
    """Turn the rows of stops.csv into a clean, sorted list of stop names.
    stop_rows: list of dictionaries from read_stops().
    Returns a list of stop names, sorted A to Z ignoring capital letters.
    """
    
    # Create an empty list to store the stop names.
    names = []
    
    for row in stop_rows:
        name = row["stop_name"].strip()
        names.append(name)
    return sorted(names, key=str.casefold)

def show_menu_2():
    """Print every stop as a numbered list, A to Z.
    Takes no parameters and returns nothing.
    """
    stops = get_stop_names(read_stops())

    if len(stops) == 0:
        print("No stops to show. Check that data/stops.csv exists and is not empty.")
    else:
        print(f"\n--- ALL STOPS ({len(stops)} total) ---")
        for number, name in enumerate(stops, start=1):
            print(f"{number:>3}. {name}")

    # Pause so this doesn't go straight back to the main menu.
    input("\nEnter any button to go back to the main menu...")