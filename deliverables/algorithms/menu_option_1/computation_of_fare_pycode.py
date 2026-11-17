# 1. Initialize the student numbers for each group members

rose = "2026-31173"
louis = "2026-31059"
karol = "2026-31141"
dan = "2026-31194"
mondi = "2026-31076"
haze =  "2026-31131"
kayleen = "2026-31221"
jp = "2006-78502"

# 2. Store all the student numbers in a list

student_numbers = [rose, louis, karol, dan, mondi, haze, kayleen, jp]

# 3. Initialize group_seed to 0 and calculate the sum of the last 4 digits of each student number

group_seed = 0
for student_number in student_numbers:
    individual_seed = int(student_number[-4:])
    group_seed = group_seed + individual_seed

# 4. Define a function to calculate the base fare, base distance, fare per extra km and discount

def get_group_settings(seed):
    base_fare = 11 + (seed % 5) #this is in peso / P
    base_distance = 3 + (seed % 3) #this is in km
    fare_per_extra_km = 1.50 + (seed % 4) * 0.25 #this is in peso / P
    discount_rate = 15 + (seed % 3) * 5  #discount in %
    return base_fare, base_distance, fare_per_extra_km, discount_rate

# 5. Call the function 

base_fare, base_distance, fare_per_extra_km, discount_rate = get_group_settings(group_seed)

print("Group Seed:", group_seed)
print("Base Fare:", base_fare)
print("Base Distance:", base_distance)
print("Fare per Extra Km:", fare_per_extra_km)
print("Discount Rate:", discount_rate)    

# 6. Computation of fare

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
    fare = fare * (1 - (discount_rate / 100)) 

print(f"P{fare:.2f}  |  {distance} km  |  {transfers} transfers")