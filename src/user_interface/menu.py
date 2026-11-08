"""Menu screens and the text shown to the user: the start screen,
the main menu, and any sub-menus.
"""
from src.lib.io import read_menu_input
from src.features.menu import update_setup_header
from src.lib.constants import MENU_OPTIONS
from src.user_interface.menu_option_1 import show_menu_1
from src.user_interface.menu_option_2 import show_menu_2
from src.user_interface.menu_option_3 import show_menu_3
from src.user_interface.menu_option_4 import show_menu_4
from src.user_interface.menu_option_5 import show_menu_5

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
