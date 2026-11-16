"""
Reading and writing functions.
"""

import csv

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
    Read csv files
    """
    with open(file_path, 'r', newline="", encoding="utf-8") as file:
            #Reading the csv rows as a dictionary.
            reader = csv.DictReader(file)
            #Return all records as a list.
            return list(reader)
    

# TODO
# Author: TBA
def write_csv(file_path, data):
    """
    writing additional rows of data to CSV files
    """
    #using the 'a' mode to append data to the csv file. To preserve existing records and headers
    with open(file_path, 'a', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    