"""
Menu option 3: admin mode (add/remove stops and segments).
"""
from src.lib.io.stops import read_stops
from src.lib.io.routes import read_routes
from src.lib.constants import DATA_DIR
from src.lib.io import append_csv
from src.lib.io.routes import add_route
from src.lib.io.routes import remove_route
from src.lib.io.stops import overwrite_stops



# Author: Jose Paolo Aguiluz
def admin_mode_password_checker(admin_mode_user_attempt):
    """This function checks if the user can access admin mode by entering the correct password. 
    The function accepts one parameter named admin_mode_user_attempt and returns a boolean value """
    if admin_mode_user_attempt == "Hex":
        return True
    else:
        return False

    
# Author: Jose Paolo Aguiluz
def admin_mode_choices():
    """This function shows the admin mode menu where all the choices are seen. 
    The function does not have a parameter and does not return a value"""
    while True:
        print("")
        print("--- ADMIN MODE ---")
        print("")
        print("[1] Add a stop  [2] Remove a stop  [3] Add a segment  [4] Remove a segment  [5] Back")
        choice = input("Choice: ")
        if choice.strip() == "1":
            add_a_stop()
        elif choice.strip() == "2":
            remove_a_stop()
        elif choice.strip() == "3":
            add_a_segment()
        elif choice.strip() == "4":
            print("remove_a_segment function here")
        elif choice.strip() == "5":
            return
        else:
            print("Incorrect choice. Please only choose from 1-5.")


# Author: Jose Paolo Aguiluz
def show_menu_3():
   """This function asks for the password again and again until it's right or when the user enters 0. 
   If the password is correct, it calls admin_mode_choices function. If user enters 0, returns to the main menu"""
   checker_result = False
   while True:
       print("")
       print("Enter 0 to exit")
       admin_mode_user_attempt = input("Please enter password: ").strip()
       if admin_mode_user_attempt == "0":
           break
       checker_result = admin_mode_password_checker(admin_mode_user_attempt)
       if checker_result == True:
           break
       else:
           print("Incorrect password. Please try again")
   if checker_result == True:
       admin_mode_choices()
   else:
       return


# Author: Jose Paolo Aguiluz
def choose_route():
    """This function displays the routes and asks for input. 
    It takes in no parameters and returns full_route_name or None as output"""
    csv_routes = read_routes()
    while True:
        print("")
        unique_route = []
        for row in csv_routes:
            if row["route_name"] not in unique_route:
                unique_route.append(row["route_name"])
        for items in unique_route:
            splitted_items = items.split(" ", 1)
            print(f"[{splitted_items[0]}] {splitted_items[1]}")
    
        print("")
        print("Enter 0 to exit")
        new_route = input("Please enter a route (e.g. R1): ").strip().upper()
        print("")
        if new_route == "0":
            return None
        route_checker = False
        for route in unique_route:
            if new_route == route.split(" ", 1)[0]:
                route_checker = True
                full_route_name = route
                break
        if route_checker == True:
            break
        else:
            print("")
            print(f"{new_route} is not a route. Please choose from the list or enter 0 to exit")
    return full_route_name
    


# Author: Jose Paolo Aguiluz
def add_a_stop():
    """This function lets the user add a new stop to stops.csv and routes.csv using add_route function. 
    It takes no parameters and does not return an output."""
    
    csv_stops = read_stops()
    csv_routes = read_routes()
    

    while True:
        print("Enter 0 to exit")
        new_stop = input("Please enter stop name: ").strip().lower()
        if new_stop == "0":
            return 
         
        duplicate_checker = False
        
        for stop in csv_stops:
            if stop["stop_name"].lower() == new_stop:
                duplicate_checker = True

        if duplicate_checker == True:
            print("")
            print(f"{new_stop.title()} already exists. Please try again or enter 0 to exit")
            print("")
        elif new_stop == "":
            print("")
            print("Stop names must contain letters and/or numbers. Please try again or enter 0 to exit")
            print("")
        else:
            break
        
    new_stop = new_stop.title()

    full_route_name = choose_route()
    if full_route_name == None:
        return
    
    while True:
        chosen_route = []
        for row in csv_routes:
            if row["route_name"] == full_route_name:
                if row["stop_a"] not in chosen_route:
                    chosen_route.append(row["stop_a"])
                if row["stop_b"] not in chosen_route:
                    chosen_route.append(row["stop_b"])

        counter = 1
        for places in chosen_route:
            print(f"[{counter}] {places}")
            counter += 1

        print("")
        connection_choice = input(f"Where does {new_stop} connect? Enter a number from the list or enter 0 to exit: ").strip()
        if connection_choice == "0":
            return
        if not connection_choice.isdigit():
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        elif int(connection_choice) > len(chosen_route) or int(connection_choice) < 1:
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        else:
            break
        
    while True:
        total_distance = 0
        for row in csv_routes:
            if row["route_name"] == full_route_name:
                total_distance += float(row["distance_km"])
        print("")
        new_distance = input(f"How far is {new_stop} from {chosen_route[int(connection_choice) - 1]}? Enter 0.1 to {total_distance:.2f} km, or 0 to exit: ").strip()
        if new_distance == "0":
            return 
        if "nan" in new_distance.lower():
            print("")
            print(f"Invalid distance. Enter a number from 0.1 to {total_distance:.2f} km or enter 0 to exit")
            continue
        try:
            floated_distance = float(new_distance)
        except ValueError:
            print("")
            print(f"Invalid distance. Enter a number from 0.1 to {total_distance:.2f} km or enter 0 to exit")
            continue
        if floated_distance > total_distance or floated_distance < 0.1:
            print("")
            print(f"Distance must be between 0.1 and {total_distance:.2f} km. Please try again or enter 0 to exit")
        else:
            break

    while True:
        print("")
        save_stop = input("Save this stop? (Y/N): ").strip().lower()
        if save_stop == "y":
            break
        elif save_stop == "n":
            return
        else:
            print("")
            print("Invalid input. Please enter Y or N only")

    try:
        new_segment = {
            "route_name": full_route_name,
            "stop_a": chosen_route[int(connection_choice) - 1],
            "stop_b": new_stop,
            "distance_km": new_distance
            }
        add_route(new_segment)
        append_csv(DATA_DIR / "stops.csv", {"stop_name": new_stop})
        print("")
        print("------------------------")
        print("stop successfully added!")  
        print("------------------------") 
    except:
        print("Saving failed. Please contact technical support")
        


    

# Author: Jose Paolo Aguiluz 
def add_a_segment():
    """This function lets the user add a new segment between two nonconnected stops and save it to routes.csv using add_route function. 
    It takes no parameters and does not return an output."""
    
    csv_routes = read_routes()
    full_route_name = choose_route()
    if full_route_name == None:
        return

    while True:
        chosen_route = []
        for row in csv_routes:
            if row["route_name"] == full_route_name:
                if row["stop_a"] not in chosen_route:
                    chosen_route.append(row["stop_a"])
                if row["stop_b"] not in chosen_route:
                    chosen_route.append(row["stop_b"])

        counter = 1
        for places in chosen_route:
            print(f"[{counter}] {places}")
            counter += 1

        print("")
        print("Enter 0 to exit")
        stop_1 = input("Choose stop A (enter a number): ").strip()
        print("")
        if stop_1 == "0":
            return
        if not stop_1.isdigit():
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        elif int(stop_1) > len(chosen_route) or int(stop_1) < 1:
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        else:
            break
                

    while True:
        counter = 1
        for places in chosen_route:
            print(f"[{counter}] {places}")
            counter += 1
        print("")
        print(f"Stop A: {chosen_route[int(stop_1) -1]}")
        print("Enter 0 to exit")
        print("")
        stop_2 = input("Choose stop B (enter a number): ").strip()
        if stop_2 == "0":
            return
        if not stop_2.isdigit():
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        elif int(stop_2) == int(stop_1):
            print("")
            print(f"Stop B can't be the same as stop A {chosen_route[int(stop_1) - 1]}. Please choose another stop or enter 0 to exit")
            print("")
        elif int(stop_2) > len(chosen_route) or int(stop_2) < 1:
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        else:
            does_exist = False
            for items in csv_routes:
                if (items["stop_a"] == chosen_route[int(stop_1) -1] and items["stop_b"] == chosen_route[int(stop_2) -1]) or (items["stop_a"] == chosen_route[int(stop_2) -1] and items["stop_b"] == chosen_route[int(stop_1) -1]):
                    does_exist = True
            if does_exist == True:
                print("")
                print(f"A segment between {chosen_route[int(stop_1) -1]} and {chosen_route[int(stop_2) -1]} already exists. Please choose another stop or enter 0 to exit")
                print("")
            else:
                break

    while True:
        print("")
        print(f"Stop A: {chosen_route[int(stop_1) -1]}")
        print(f"Stop B: {chosen_route[int(stop_2) -1]}")
        print("Enter 0 to exit")
        total_distance = 0
        for row in csv_routes:
            if row["route_name"] == full_route_name:
                total_distance += float(row["distance_km"])
        
        new_distance = input(f"Distance in km between {chosen_route[int(stop_1) -1]} and {chosen_route[int(stop_2) -1]} (0.1 to less than {total_distance:.2f} km): ").strip()
        if new_distance == "0":
            return 
        if "nan" in new_distance.lower():
            print("")
            print(f"Invalid distance. Enter a number from 0.1 to less than {total_distance:.2f} km or enter 0 to exit")
            continue
        try:
            floated_distance = float(new_distance)
        except ValueError:
            print("")
            print(f"Invalid distance. Enter a number from 0.1 to less than {total_distance:.2f} km or enter 0 to exit")
            continue
        if floated_distance >= total_distance or floated_distance < 0.1:
            print("")
            print(f"Distance must be between 0.1 and less than {total_distance:.2f} km. Please try again or enter 0 to exit")
        else:
            break

    while True:
        print("")
        save_segment = input("Save this segment? (Y/N): ").strip().lower()
        if save_segment == "y":
            break
        elif save_segment == "n":
            return
        else:
            print("")
            print("Invalid input. Please enter Y or N only")

    try:
        new_segment = {
            "route_name": full_route_name,
            "stop_a": chosen_route[int(stop_1) - 1],
            "stop_b": chosen_route[int(stop_2) - 1],
            "distance_km": new_distance
            }
        add_route(new_segment)
        print("")
        print("---------------------------")
        print("segment successfully added!")  
        print("---------------------------") 
    except:
        print("Saving failed. Please contact technical support")


# Author: Jose Paolo Aguiluz         
def remove_a_stop():
    """This function lets the user remove a stop from a chosen route using remove_route function. 
    It then joins the remaining segments from its neighbors using add_route. If no other route uses
    the stop, it is removed from stops.csv using overwrite_stops. This function does not have any parameters
    and returns no value."""  
    csv_routes = read_routes()    
    full_route_name = choose_route()
    if full_route_name == None:
        return

    endpoints = full_route_name.split(" ", 1)[1]
    endpoint_parts = endpoints.split(" - ")    

    while True:
        chosen_route = []
        for row in csv_routes:
            if row["route_name"] == full_route_name:
                if row["stop_a"] not in chosen_route:
                    chosen_route.append(row["stop_a"])
                if row["stop_b"] not in chosen_route:
                    chosen_route.append(row["stop_b"])

        counter = 1
        for places in chosen_route:
            print(f"[{counter}] {places}")
            counter += 1

        print("Enter 0 to exit")
        delete_choice = input("Which stop would you like to remove?: ").strip()
        if delete_choice == "0":
            return
        if not delete_choice.isdigit():
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        elif int(delete_choice) > len(chosen_route) or int(delete_choice) < 1:
            print("")
            print(f"Invalid choice. Enter a number from 1 to {len(chosen_route)} or enter 0 to exit")
            print("")
        elif chosen_route[int(delete_choice) - 1] in endpoint_parts:
            print("")
            print(f"{endpoint_parts[0]} and {endpoint_parts[1]} are the end points of {full_route_name} and can't be removed. Please choose another stop or enter 0 to exit.")
            print("")
        else:
            break

    delete_stop = chosen_route[int(delete_choice) - 1]
    neighbors = []
    for item in csv_routes:
        if item["route_name"] == full_route_name: 
            if delete_stop == item["stop_a"]:
                neighbors.append((item["stop_b"], item["distance_km"]))
            elif delete_stop == item["stop_b"]:
                neighbors.append((item["stop_a"], item["distance_km"]))  

    while True:
        print("")
        save_stop = input("Remove this stop? (Y/N): ").strip().lower()
        print("")
        if save_stop == "y":
            break
        elif save_stop == "n":
            return
        else:
            print("")
            print("Invalid input. Please enter Y or N only")       

    try:
        for neighbor in neighbors:
            delete_segment_neighbor = {
                "route_name": full_route_name,
                "stop_a": delete_stop,
                "stop_b": neighbor[0]
            }
            remove_route(delete_segment_neighbor)

        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                connect_new_neighbors = {
                    "route_name": full_route_name,
                    "stop_a": neighbors[i][0],
                    "stop_b": neighbors[j][0],
                    "distance_km": round(float(neighbors[i][1]) + float(neighbors[j][1]), 2) 
                }
                add_route(connect_new_neighbors)

        checker = False
        for item in csv_routes:
            if item["route_name"] != full_route_name:
                if delete_stop == item["stop_a"] or delete_stop == item["stop_b"]:
                    checker = True
        if checker == False:
            listed_stops = read_stops()
            new_csv_stops = []
            for item in listed_stops:
                if item["stop_name"] != delete_stop:
                    new_csv_stops.append(item)

            overwrite_stops(new_csv_stops)
        print("")
        print(f"{delete_stop} successfully removed!")
    except:
        print("Removal failed. Please contact technical support.")