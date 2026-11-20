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


   
