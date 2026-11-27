"""
One-time startup helpers: loading the program's data and files before
the main menu starts.
"""

from src.lib.io.members import read_members_info

# Author: Kayleen Rosette Lagunday
def get_group_settings():
    """
    Calculate and return base_fare, base_distance, fare_per_extra_km, discount_rate using the group seed.
    """
    seed = get_group_seed()

    base_fare = 11 + (seed % 5)
    base_distance = 3 + (seed % 3)
    fare_per_extra_km = 1.50 + (seed % 4) * 0.25
    discount_rate = 15 + (seed % 3) * 5
    return base_fare, base_distance, fare_per_extra_km, discount_rate

# Author: Kayleen Rosette Lagunday, Reiniel Dan Pablo
def get_group_seed():
    """
    Add up the last 4 digits of each member's student number to get the group seed.
    """
    group_seed = 0

    for info in read_members_info():
        student_id = info["student_number"]
        last_4_digits = student_id[-4:]

        #TODO: Add validation here just in case the last for digits aren't numbers.
        #Example: 2026-311AB. This will raise an error.
        if not last_4_digits.isdigit():
            print("Error: It is not a valid number.")

        else:
            last_4_digits = int(last_4_digits)
            group_seed = group_seed + last_4_digits

    return group_seed
