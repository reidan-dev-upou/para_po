# Pseudocode for Menu Option 2

### Function: get_stop_names(stop_rows)
    IMPORT read_stops FROM src.lib.io

    FUNCTION get_stop_names(stop_rows)

        CREATE an empty list called names

        FOR EACH row IN stop_rows
            GET the stop_name from the current row
            REMOVE leading and trailing spaces from stop_name
            ADD stop_name TO names
        END FOR

        SORT names alphabetically, ignoring uppercase and lowercase
        RETURN names

    END FUNCTION

### Function: show_menu_2()

    FUNCTION show_menu_2()

        READ all stops using read_stops()
        PASS the stop data to get_stop_names()
        STORE the returned list in stops

        IF the length of stops is equal to 0 THEN
            DISPLAY "No stops to show. Check that data/stops.csv exists and is not empty."  

        ELSE
            DISPLAY the total number of stops

            SET number to 1

            FOR EACH name IN stops
            DISPLAY number and name
            INCREASE number by 1
            END FOR

        END IF

        WAIT for user to press Enter
        RETURN to the main menu

     END FUNCTION
