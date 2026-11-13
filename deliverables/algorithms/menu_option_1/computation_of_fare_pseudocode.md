# Computation of fare 
# Pseudocode
1. Start
2. Set base fare to 13.00
3. Set base distance to 3 km    
4. Set fare per extra km to 2.00
5. Set discount rate to 0.15        
6. Get distance in km from user input
7. Get total transfers from user input  
8. Get passenger type from user input
9. If distance is less than or equal to base distance, set fare to base fare
10. Else, calculate extra km as distance minus base distance, and set fare to base fare plus (extra km multiplied by fare per extra km)
11. If passenger type is 'D', apply discount to fare by multiplying fare by (1 minus discount rate)                                     
12. Print fare, distance, and transfers in the format: "P{fare:.2f}  |  {distance} km  |  {transfers} transfers"
13. End 