# Build Route Graph
# Pseudocode

1. Start
2. Get routes (the rows read from routes.csv: each has route_name, stop_a, stop_b, distance_km)
3. Create an empty dictionary called graph (stop -> list of (neighbor, distance_km, route_name))
4. Create an empty set called seen_pairs
5. For each row in routes, do steps 6 to 11
6. Set stop_a and stop_b to the row's stop_a and stop_b
7. Set pair to the unordered pair {stop_a, stop_b}
8. If pair is already in seen_pairs, skip this row and go back to step 5 for the next row
9. Add pair to seen_pairs
10. Add (stop_b, distance_km, route_name) to graph's list for stop_a, creating the list if it doesn't exist yet
11. Add (stop_a, distance_km, route_name) to graph's list for stop_b, creating the list if it doesn't exist yet, then go back to step 5 for the next row
12. Return graph
13. End

# Check Travel Cache
# Pseudocode

1. Start
2. Get start (the origin stop) and end (the destination stop)
3. Read the cached trips from trip_cache.csv
4. For each row in the cached trips, do step 5
5. If the row's stop_a and stop_b match start and end, in either order, return that row and go to step 7
6. Return nothing (no cached trip found)
7. End

# Search Recursively
# Pseudocode

1. Start
2. Get graph (from Build Route Graph), start (the origin stop), end (the destination stop), and visited (the set of stops already on the current path; empty on the first call, defaulting to just {start})
3. BASE CASE: If start is equal to end, return a list containing one empty path and go to step 10
4. RECURSIVE CASE (steps 5-9): try every unvisited neighbor and build this stop's paths from theirs
5. Create an empty list called paths
6. For each (neighbor, distance_km, route_name) in graph's list for start, do steps 7 to 9
7. If neighbor is already in visited, skip it and go back to step 6 for the next neighbor
8. Recursively call Search Recursively with start set to neighbor, end unchanged, and visited set to visited plus neighbor; store the result as sub_paths
9. For each sub_path in sub_paths, add (start, neighbor, distance_km, route_name) followed by sub_path to paths, then go back to step 6 for the next neighbor
10. Return paths
11. End

# Find All Paths
# Pseudocode

1. Start
2. Get graph (from Build Route Graph), start (the origin stop), end (the destination stop), and visited
3. Call Check Travel Cache with start and end; store the result as cached
4. If cached is not nothing, return cached and go to step 6
5. Return the result of Search Recursively called with graph, start, end, and visited
6. End
