"""
Reading and writing functions.
"""

import csv
from pathlib import Path

from src.lib.constants import DATA_DIR

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

# Author: Reiniel Dan Pablo
def read_routes():
    """
    Read data/routes.csv
    """
    return read_csv(DATA_DIR / "routes.csv")

# Author: Reiniel Dan Pablo
def read_stops():
    """
    Read data/stops.csv
    """
    return read_csv(DATA_DIR / "stops.csv")

# Author: Reiniel Dan Pablo
def read_members_info():
    """
    Read data/members.csv
    """
    return read_csv(DATA_DIR / "members.csv")

# Author: Andrian Mondares, Reiniel Dan Pablo
def read_csv(file_path):
    """
    Read csv files
    """
    # If the file doesn't exist, just report it and do nothing.
    if not Path(file_path).exists():
        print(f"File not found: {file_path}. Returning an empty list.")
        return []

    with open(file_path, 'r', newline="", encoding="utf-8") as file:
            #Reading the csv rows as a dictionary.
            reader = csv.DictReader(file)

            print(f"Succesfully loaded {file_path}")
            #Return all records as a list.
            return list(reader)
    

# Author: Andrian Mondares, Reiniel Dan Pablo
# TODO: Recheck this function if we need to just update the data instead of just only `appending`
# TODO: Might be useful for just updating/deleting data as well.
def write_csv(file_path, data):
    """
    Writing additional rows of data to CSV files
    """
    # If the file already exists, make sure its header matches the new data's keys before appending.
    file_exists = Path(file_path).exists()
    existing_rows = []
    if file_exists:
        existing_rows = read_csv(file_path)
        # No existing rows means no header to compare, so skip the check.
        existing_header = list(existing_rows[0].keys()) if existing_rows else None

        if existing_header is not None and list(data.keys()) != existing_header:
            print("Not writing new data into csv file; incompatible csv headers")
            return

    # Using the 'a' mode to append data to the csv file. To preserve existing records and headers
    with open(file_path, 'a', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    print(f"Successfully added new row/s to {file_path}")
    #Return the full picture: existing rows plus the one just appended.
    return existing_rows + [data]