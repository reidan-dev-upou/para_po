START
    FUNC build_graph(routes)
        LET graph = {}

        FOR EACH route IN routes DO
            LET stop_a = route["stop_a"]
            LET stop_b = route["stop_b"]
            LET distance_km = FLOAT route["distance_km"]
            LET route_name = route["route_name"]

            # a jeepney can be ridden either way, so link both directions
            APPEND (stop_b, distance_km, route_name) TO graph[stop_a]
            APPEND (stop_a, distance_km, route_name) TO graph[stop_b]
        ENDFOR

        RETURN graph
    ENDFUNC

    FUNC find_all_paths(graph, current_stop, destination_stop, path_so_far)
        IF path_so_far IS NONE THEN
            path_so_far = []
        ENDIF

        # BASE CASE: already standing at the destination, path is complete
        IF current_stop == destination_stop THEN
            RETURN [path_so_far]
        ENDIF

        LET visited_stops = {current_stop}
        FOR EACH segment IN path_so_far DO
            ADD segment["from_stop"] TO visited_stops
        ENDFOR

        LET found_paths = []
        FOR EACH (neighbor_stop, distance_km, route_name) IN graph[current_stop] DO
            IF neighbor_stop IN visited_stops THEN
                CONTINUE
            ENDIF

            LET segment = {
                "from_stop": current_stop,
                "to_stop": neighbor_stop,
                "distance_km": distance_km,
                "route_name": route_name,
            }
            LET new_path_so_far = path_so_far + [segment]

            # RECURSIVE CASE: take that ride, keep searching from the neighbor
            found_paths = found_paths + find_all_paths(graph, neighbor_stop, destination_stop, new_path_so_far)
        ENDFOR

        RETURN found_paths
    ENDFUNC
END
