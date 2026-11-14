# Computation of fare 
# Pseudocode

1. Start
2. Set group_seed to 16497
3. Set base fare to 11 + (seed % 5) = 13 pesos
4. Set base distance to 3 + (seed % 3) = 3 km    
5. Set fare per extra km to 1.50 + (seed % 4) * 0.25 = 1.75 pesos
6. Set discount rate to 15 + (seed % 3) * 5 = 15 percent
7. Get distance in km from user input
8. Get total transfers from user input  
9. Get passenger type from user input
10. If distance is less than or equal to base distance, set fare to base fare
11. Else, calculate extra km as distance minus base distance and set fare to base fare plus (extra km multiplied by fare per extra km)
12. If passenger type is 'D', apply discount to fare by multiplying fare by (1 minus (discount rate / 100))                                     
13. Print fare, distance, and transfers in the format: "P{fare:.2f}  |  {distance} km  |  {transfers} transfers"
14. End 