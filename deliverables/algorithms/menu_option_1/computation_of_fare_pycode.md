# Python code
# Passenger type - [R] Regular  [D] Student/Senior/PWD: D
# Sort by - [1] Cheapest fare  [2] Shortest distance  [3] Fewest transfers: 1

base_fare = 13.00
base_distance = 3 #km
fare_per_extra_km = 2.00
discount_rate = .15 

distance = float(input("Distance in km:"))
transfers = int(input("Total transfers:"))
passenger_type = input("Passenger type - [R] Regular  [D] Student/Senior/PWD:")

if distance <= base_distance:
    fare = base_fare
else:
    extra_km = distance - base_distance  
    fare = base_fare + (extra_km * fare_per_extra_km)

# [D] Student/Senior/PWD: D
  
if passenger_type.upper() == 'D':
    fare = fare * (1 - discount_rate) 

print(f"P{fare:.2f}  |  {distance} km  |  {transfers} transfers")