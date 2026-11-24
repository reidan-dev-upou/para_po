"""
Reading and writing functions shared across data files.
"""

import csv
from pathlib import Path

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
            #Return all records as a list.
            return list(reader)

# Author: Reiniel Dan Pablo, Andrian Mondares
def overwrite_csv(file_path, new_data):
    """
    Overwrite a CSV file with new_data (a list of row dicts), replacing all existing rows.
    """
    if not new_data:
        # shortcut: can't write a header with zero rows, so removing the last remaining
        # row from a CSV can't be persisted here; upgrade if routes.csv/stops.csv can ever
        # legitimately become fully empty.
        print(f"No data given; not overwriting {file_path}")
        return

    with open(file_path, 'w', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(new_data[0].keys()))
        writer.writeheader()
        writer.writerows(new_data)

    print(f"Successfully overwrote {file_path}")

# Author: Karol Anne Panaligan, Reiniel Dan Pablo
def append_csv(file_path, data):
    """
    Append a single row dict to a CSV file, writing a header first if the file
    doesn't exist yet. Does not read or rewrite the file's existing rows.
    """
    file_exists = Path(file_path).exists()

    with open(file_path, 'a', newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data.keys()))
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
