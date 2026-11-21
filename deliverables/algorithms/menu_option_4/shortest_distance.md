# Rank the results: shortest distance 

1. START

2. Input the starting point and destination

    starting_point = INPUT ("Enter starting_point") 
    destination = INPUT ("Enter destination")

3. Get all possible paths from the starting point to the destination.

    valid_paths = FIND all possible paths 
                  from starting_point to destination

4. Check if there are available routes or paths

    IF valid_paths is empty THEN
        DISPLAY "No available jeepney route found."

5. Initialize the total distance for each valid path and calculate the distance in kilometers of connected stops.

    ELSE 
        FOR each valid_path in valid_paths:
            total_distance = 0

            FOR each connection in valid_path:
                ADD distance to total_distance

6. Calculate the total distance in each path

    STORE total_distance for each valid_path

7. Arrange all valid paths according to their total distance from shortest to longest

    SORT valid_paths by total_distance 
            in ascending order

8. Display the top 3 shortest paths.

    DISPLAY rank 
    DISPLAY jeepney_route_or_path 
    DISPLAY total_distance "km"
    DISPLAY estimated_fare
    DISPLAY number_of_transfers

9. END

