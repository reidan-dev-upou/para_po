# Python code
# Passenger type - [R] Regular  [D] Student/Senior/PWD: D
# Sort by - [1] Cheapest fare  [2] Shortest distance  [3] Fewest transfers: 1

seed = 16497
base_fare = 11 + (seed % 5) #this is in peso / P
base_distance = 3 + (seed % 3) #this is in km
fare_per_extra_km = 1.50 + (seed % 4) * 0.25 #this is in peso / P
discount_rate = 15 + (seed % 3) * 5  #discount in %

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
print (base_fare)
print (base_distance)
print (fare_per_extra_km)
print (discount_rate)