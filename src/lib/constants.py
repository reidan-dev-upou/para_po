"""Fixed values shared across the program. Make sure to name variables here as all uppercase. Example: VARIABLE_NAME"""

# Team Information Constants
GROUP_NAME = "Team HEX"



# Pre-made menu setup header. 
# Replace with correct values with a function
MENU_SETUP_HEADER = f"""
============================================================== 
   PARA PO! Jeepney Route Finder 
   Group: GROUP_NAME 
   Members: MEMBER_NAMES
   Group Seed: GROUP_SEED
   Fare rules (from get_group_settings): 
     Base fare ....... PBASE_FARE for the first 3 km of each ride 
     Extra distance .. PEXTRA_FARE per km (part of a km counts as 1 km) 
     Discount ........ DISCOUNT_PERCENTAGE% for students, senior citizens, and PWDs 
============================================================== 
Loading data/stops.csv ...... DATA_STOPS stops loaded. 
Loading data/routes.csv ..... DATA_ROUTES routes, 17 segments loaded.
"""

MENU_OPTIONS = f"""
=========== MAIN MENU =========== 
[1] Find a route 
[2] View all stops 
[3] Admin mode (add/remove stops and segments) 
[4] Most searched destinations 
[5] Exit
"""

