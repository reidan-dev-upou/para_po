"""
The main menu: the setup header, the menu loop, and the handlers
for each menu option.
"""

from src.lib.constants import GROUP_NAME, MENU_SETUP_HEADER, MENU_OPTIONS
from src.lib.io import read_menu_input
from src.features.menu_option_1 import show_menu_1
from src.features.menu_option_2 import show_menu_2
from src.features.menu_option_3 import show_menu_3
from src.features.menu_option_4 import show_menu_4
from src.features.menu_option_5 import show_menu_5


def update_setup_header():
    """Fill in the setup header template with real values.

    Returns the setup header text, ready to print.
    """
    setup_header = MENU_SETUP_HEADER

    setup_header_dict = {
        "GROUP_NAME": GROUP_NAME,
        "MEMBER_NAMES": "AA, BB, CC",
        "GROUP_SEED": "00000",
        "BASE_FARE": "XXX",
        "EXTRA_FARE": "YY",
        "DISCOUNT_PERCENTAGE": "Z",
        "DATA_STOPS": "DD",
        "DATA_ROUTES": "EE",
    }

    for placeholder, actual_value in setup_header_dict.items():
        # replace() returns a new string, it doesn't change setup_header in place
        setup_header = setup_header.replace(placeholder, str(actual_value))

    return setup_header

# Author: Reiniel Dan Pablo
def show_setup_header():
    setup_header = update_setup_header()
    print(setup_header)

# Author: Reiniel Dan Pablo
def show_main_menu():
    # Loop until the user picks Exit (5), instead of each option
    # recursing back into this function.
    while True:
        print(MENU_OPTIONS)
        input_choice = read_menu_input()

        if input_choice == 1:
            show_menu_1()
        elif input_choice == 2:
            show_menu_2()
        elif input_choice == 3:
            show_menu_3()
        elif input_choice == 4:
            show_menu_4()
        elif input_choice == 5:
            show_menu_5()
            break
