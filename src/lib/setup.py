"""
One-time startup helpers: loading the program's data and files before
the main menu starts.
"""

import csv

# TODO
# Author: TBA
def get_group_settings():
    """
    To be updated.
    """
    return 0

# TODO
# Author: TBA
def get_group_seed():
    """
    To be updated.
    """
    return 0

# Author: TBA
def load_setup():
    """
    To be updated.
    For every setup function is created. Call the function here as well.
    """

    output_dict = {
        "group_seed" : get_group_seed(),
        "group_settings": get_group_settings(),
    }

    return output_dict