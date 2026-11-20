# Fewest Route Changes (Transfers)
# Pseudocode

1. Start
2. Get valid_paths from the path search (each path is a list of segments; each segment has from_stop, to_stop, distance, and route)
3. If valid_paths is empty, return an empty list (Menu 1 caller displays "No available jeepney route found.") and go to step 15
4. Create an empty list called ranked_paths
5. For each path in valid_paths, do steps 6 to 10
6. Set transfers to 0, total_distance to 0, and previous_route to none
7. For each segment in the path, add the segment's distance to total_distance
8. If previous_route is not none and the segment's route is not equal to previous_route, add 1 to transfers
9. Set previous_route to the segment's route, then go back to step 7 for the next segment
10. Add (path, transfers, total_distance) to ranked_paths
11. Sort ranked_paths by transfers from lowest to highest, then by total_distance from shortest to longest
12. Create an empty list called results
13. For each of the first 3 entries in ranked_paths, add (path, transfers) to results (if fewer than 3 exist, add all of them)
14. Return results (for each path, rides = transfers + 1; display code starts a new ride when the route changes)
15. End
