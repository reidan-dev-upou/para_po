"""
Menu option 3: admin mode (add/remove stops and segments).
"""

# Author: Jose Paolo Aguiluz
def admin_mode_password_checker(admin_mode_user_attempt):
    """ this function checks if the user can access admin mode by entering the correct password. 
    The function accepts one parameter named admin_mode_user_attempt and returns a boolean value """
    if admin_mode_user_attempt == "Hex":
        return True
    else:
        return False

    
# Author: Jose Paolo Aguiluz
def admin_mode_choices():
    """this function shows the admin mode menu where all the choices are seen. 
    The function does not have a parameter and does not return a value"""
    while True:
        print("[1] Add a stop  [2] Remove a stop  [3] Add a segment  [4] Remove a segment  [5] Back")
        choice = input("Choice: ")
        if choice.strip() == "1":
            print("add_a_stop function here")
        elif choice.strip() == "2":
            print("remove_a_stop function here")
        elif choice.strip() == "3":
            print("add_a_segment function here")
        elif choice.strip() == "4":
            print("remove_a_segment function here")
        elif choice.strip() == "5":
            return
        else:
            print("Incorrect choice. Please only choose from 1-5.")


# Author: Jose Paolo Aguiluz
def show_menu_3():
   """this function asks for the password again and again until it's right or when the user enters 0. 
   If the password is correct, it calls admin_mode_choices function. If user enters 0, returns to the main menu"""
   checker_result = False
   while True:
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
