"""Gets and displays the top 5 most searched destinations.

    Returns a list of ranked destinations with their names and search counts.
"""

from src.lib.assertions import run_test

from src.features.menu_option_4 import get_most_searched_destinations

from unittest.mock import patch

result = get_most_searched_destinations()

#TC01: Return Type
run_test(
    actual=isinstance(result, list),
    expected=True,
    test_name="Popular Destinations returns a list"
)


sample_trips = [
    {"destination": "SM Megamall"},
    {"destination": "SM Megamall"},
    {"destination": "SM Megamall"},
    {"destination": "Hospital"},
    {"destination": "Hospital"},
    {"destination": "School"},
    {"destination": "School"},
    {"destination": "Art in Island"},
    {"destination": "Quezon City Hall"}
]
#TC02: Rank and Search Count
with patch("src.features.menu_option_4.read_trip_history", return_value=sample_trips):
    run_test(
    actual=get_most_searched_destinations(),
    expected=[
        (1, "SM Megamall", 3),
        (2, "Hospital", 2),
        (2, "School", 2),
        (3, "Art in Island", 1),
        (3, "Quezon City Hall", 1)
    ],
    test_name="Popular Destinations ranking"
    )

#TC03: Empty Trip History
with patch("src.features.menu_option_4.read_trip_history", return_value=[]):
    run_test(
        actual=get_most_searched_destinations(),
        expected=[],
        test_name="Empty trip history"
    )

#TC04: Single Destination
with patch("src.features.menu_option_4.read_trip_history",
           return_value=[{"destination": "School"}]):
    run_test(
        actual=get_most_searched_destinations(),
        expected=[(1, "School", 1)],
        test_name="Single destination"
    )

#TC05: Tie for 5th Place
sample_ties = [
    {"destination": "Art in Island"},
    {"destination": "SM Megamall"},
    {"destination": "Quezon City Hall"},
    {"destination": "Robinsons Magnolia"},
    {"destination": "SM City Araneta"},
    {"destination": "Ayala Malls Feliz"}
]

with patch("src.features.menu_option_4.read_trip_history", return_value=sample_ties):
    run_test(
        actual=get_most_searched_destinations(),
        expected=[
            (1, "Art in Island", 1),
            (1, "Ayala Malls Feliz", 1),
            (1, "Quezon City Hall", 1),
            (1, "Robinsons Magnolia", 1),
            (1, "SM City Araneta", 1)
        ],
        test_name="Tie for 5th place"
    )