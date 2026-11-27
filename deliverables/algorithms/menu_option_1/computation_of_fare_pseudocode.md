# Computation of Fare Pseudocode

1. Start
2. Load member records and route segments
3. Extract student numbers from member records
4. Initialize group_seed to 0 and calculate the sum of the last 4 digits of each student number
5. group_seed = 0
6. FOR each student_number IN student_numbers:
7. individual_seed = integer of last 4 characters of student_number
8. group_seed = group_seed + individual_seed
9. Define function get_group_settings(seed):
10. base_fare = 11 + (seed MOD 5)
11. base_distance = 3 + (seed MOD 3)
12. fare_per_extra_km = 1.50 + (seed MOD 4) * 0.25
13. discount_rate = 15 + (seed MOD 3) * 5
14. RETURN base_fare, base_distance, fare_per_extra_km, discount_rate
15. Set base_fare, base_distance, fare_per_extra_km, discount_rate = get_group_settings(group_seed)
16. Input origin (starting point)
17. Input destination
18. Input passenger_type: 'R' for regular passenger or 'D' if eligible for discount
19. Calculate route distance (and transfers) from origin to destination across route segments
20. If no route is found (distance is None):
21. Print "No route found. Please check your starting point and destination."
22. Stop or return result
23. Else if distance equals 0.0:
24. Print "Starting point and destination cannot be the same."
25. Stop or return result
26. If distance <= base_distance:
27. fare = base_fare
28. Else:
29. extra_km = distance - base_distance
30. fare = base_fare + (extra_km * fare_per_extra_km)
31. If passenger_type == 'D':
32. fare = fare * (1 - (discount_rate / 100))
33. Print fare, distance, and transfers in format: "P{fare:.2f}  |  {distance} km  |  {transfers} transfers"
34. End