## shortest distance

# Search and collect possible jeepney routes or paths (starting point and destination).
# Identify the distance in kilometers of connected stop and get the total distance of each path.
# Arrange all valid paths according to total distance
# Compare the total distance of each path to determine which route provides the shortest distance.
# Display the results with ff information: (subject for review and changes)
    + Rank of the route
    + jeepney route or path (sequence of stops)
    + total distance "km"
    + estimated fare
    + number of transfers


START

Get all possible paths from starting point todestination.

INPUT starting_point
INPUT destination

IF no valid paths are found THEN 
    DISPLAY "No available jeepney route found."
ELSE
    For each valid_path:

        SET total_distance = 0

        FOR each connection in the path:
            ADD distance to total_distance 

Sort all paths from shortest to longest distance

Display the top 3 shortest paths.

    DISPLAY rank 
    DISPLAY jeepney_route_or_path 
    DISPLAY total_distance "km"
    DISPLAY estimated_fare
    DISPLAY number_of_transfers
     
END
