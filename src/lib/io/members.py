"""
Reading data/members.csv.
"""

from src.lib.constants import DATA_DIR
from src.lib.io import read_csv

# Author: Reiniel Dan Pablo
def read_members_info():
    """
    Read data/members.csv
    """
    return read_csv(DATA_DIR / "members.csv")
