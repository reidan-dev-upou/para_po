"""
Para Po! Jeepney Route Finder entry point. Runs the program only;
the actual code lives under src/.
"""

from src.features.menu import show_main_menu, show_setup_header

def main():

    # Once loaded, display setup menu header
    show_setup_header()

    
    # Displaying the main menu interface
    show_main_menu()



if __name__ == "__main__":
    main()    
