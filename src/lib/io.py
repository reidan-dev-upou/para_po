"""
Reading and writing functions.
"""


# Author: Reiniel Dan Pablo
def read_menu_input():
    input_choice = input("Enter choice (1-5): ")
    
    # Do a continuous loop
    while True:
        # If input is invalid a.) not within 1-5, and b.) is not a digit
        # The program will ask again until input is valid.
        if input_choice.isdigit():
            if 1 <= int(input_choice) <= 5:
                break
            print("Invalid input. Try again!\n")
        else:
            print("Invalid input. Try again!\n")

        input_choice = input("Enter choice (1-5): ")
    return int(input_choice)
    
# TODO
# Author: TBA
def read_csv(file_path):
    """
    To be updated.
    """
    pass

# TODO
# Author: TBA
def write_csv(file_path):
    """
    To be updated.
    """
    pass