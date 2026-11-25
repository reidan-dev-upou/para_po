"""
Menu option 4: most searched destinations.
"""


def show_menu_4():
    print("WIP: Menu 4")

    # Pause so this doesn't go straight back to the main menu.
    input("Press any button to continue...")



from src.lib.io.trip_history import read_trip_history

# Author: Karol Anne Panaligan
#TO DO: Integrate with the rest of Menu 4.
def get_most_searched_destinations():
    """This function retrieves trip history and displays the top 5 most searched destinations

    Returns None. Prints most searched destinations with ranks names and counts."""

    trip_history = read_trip_history()
    print(trip_history)

    if not trip_history:
        print("No trip history available")
        return

    destination_counts = {}

    for trip in trip_history:
        destination = trip.get("destination")
        if destination:
            destination_counts[destination] = destination_counts.get(destination, 0) + 1

    counts = destination_counts
    names = list(counts)

    for i in range(len(names)):
        best = i

        for j in range(i + 1, len(names)):
            if counts[names[j]] > counts[names[best]]:
                best = j
            elif counts[names[j]] == counts[names[best]]:
                if names[j] < names[best]:
                    best = j

        names[i], names[best] = names[best], names[i]

    rank = 0
    previous_count = None

    for name in names[:5]:
        count = counts[name]

        if count != previous_count:
            rank += 1

        print(rank, name, count)
        previous_count = count