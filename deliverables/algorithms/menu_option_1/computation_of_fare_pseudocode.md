# Computation of Fare Pseudocode

1. Start

2. Initialize the student numbers for each group members

rose = "2026-31173"
louis = "2026-31059"
karol = "2026-31141"
dan = "2026-31194"
mondi = "2026-31076"
haze =  "2026-31131"
kayleen = "2026-31221"
jp = "2006-78502"

3. Store all the student numbers in a list

student_numbers = [rose, louis, karol, dan, mondi, haze, kayleen, jp]

4. Initialize group_seed to 0 and calculate the sum of the last 4 digits of each student number

group_seed = 0
for student_number in student_numbers:
    individual_seed = int(student_number[-4:])
    group_seed = group_seed + individual_seed

5. Define a function to calculate the base fare, base distance, fare per extra km and discount

def get_group_settings(seed):
    base_fare = 11 + (seed % 5) 
    base_distance = 3 + (seed % 3) 
    fare_per_extra_km = 1.50 + (seed % 4) * 0.25 
    discount_rate = 15 + (seed % 3) * 5  
    return base_fare, base_distance, fare_per_extra_km, discount_rate

6. Set base_fare, base_distance, fare_per_extra_km, discount_rate = get_group_settings(group_seed)

7. Get distance in km from user input

8. Get total transfers from user input  

9. Get passenger type from user input

10. If distance is less than or equal to base distance, set fare to base fare

11. Else, calculate extra km as distance minus base distance and set fare to base fare plus (extra km multiplied by fare per extra km)

12. If passenger type is 'D', apply discount to fare by multiplying fare by (1 minus (discount rate / 100))    

13. Print fare, distance, and transfers in the format: "P{fare:.2f}  |  {distance} km  |  {transfers} transfers"

14. End 