"""Para Po! Jeepney Route Finder entry point. Runs the program only;
the actual code lives under src/.
"""

from src.lib.setup import load_setup
from src.features.menu import show_main_menu, show_setup_header

def main():

    # Calling all the declared setups before the main interface is loaded
    setup_data = load_setup()
    # Once loaded, display setup menu header
    show_setup_header()

    
    # Displaying the main menu interface
    show_main_menu()



if __name__ == "__main__":
    main()    



