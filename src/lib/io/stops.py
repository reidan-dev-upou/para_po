"""
Reading and writing data/stops.csv.
"""

from src.lib.constants import DATA_DIR
from src.lib.io import read_csv, overwrite_csv

# Author: Reiniel Dan Pablo
def read_stops():
    """
    Read data/stops.csv
    """
    return read_csv(DATA_DIR / "stops.csv")

# Author: Reiniel Dan Pablo
def overwrite_stops(new_stops_data):
    """
    Overwrite data/stops.csv with new_stops_data.
    """
    overwrite_csv(DATA_DIR / "stops.csv", new_stops_data)
