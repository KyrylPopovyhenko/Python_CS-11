## How to start the program

Open console for Windows/Linux or terminal for Mac 
Open the directory using cd ~/trip_budget and start the program using python trip_budget.py or python3 trip_budget.py

## What the program does

What you need to input:
    1. A trip distance in one direction (km)
    2. Fuel consumption (L/100km)
    3. Current fuel price per liter
    4. Passengers count

This program can easily calculate the next values:
    1. Total trip distance 
    2. Total fuel needed 
    3. Total fuel cost
    4. Cost per person
    5. Canisters needed
    6. Liters remaining
    7. Minimal canisters needed

## How fuel_needed calculates

fuel_needed = fuel * (full_dist/100)

At first we divide the full distance of trip by 100 at the next we multiply it by fuel consumption

## Testing 

Test 1 

Data: 
Distance - 100 | Fuel - 8 | Fuel price - 60 | Passengers - 4 |

Expected result:
Total distance: 200.0 km 
Fuel needed: 16.00 L 
Total fuel cost: 960.00 
Cost per person: 240.00 
Canisters needed: 0 
Liters remaining: 16.00 L 
Minimal canisters needed: 1

Result:
Total distance: 200.0 km 
Fuel needed: 16.00 L 
Total fuel cost: 960.00 
Cost per person: 240.00 
Canisters needed: 0 
Liters remaining: 16.00 L 
Minimal canisters needed: 1


Test 2 

Data: 
Distance - 75 | Fuel - 7.5 | Fuel price - 60 | Passengers - 3 |

Expected result:
Total distance: 150.0 km
Fuel needed: 11.25 L
Total fuel cost: 675.00
Cost per person: 225.00
Canisters needed: 0
Liters remaining: 11.25 L
Minimal canisters needed: 1

Result:
Total distance: 150.0 km
Fuel needed: 11.25 L
Total fuel cost: 675.00
Cost per person: 225.00
Canisters needed: 0
Liters remaining: 11.25 L
Minimal canisters needed: 1


Test 3 

Data:
Distance - 100 | Fuel - 20 | Fuel price - 100 | Passengers - 2 |

Expected result:
Total distance: 200.0 km 
Fuel needed: 40.00 L 
Total fuel cost: 4000.00 
Cost per person: 2000.00 
Canisters needed: 2 
Liters remaining: 0.00 L 
Minimal canisters needed: 2

Result: 
Total distance: 200.0 km 
Fuel needed: 40.00 L 
Total fuel cost: 4000.00 
Cost per person: 2000.00 
Canisters needed: 2 
Liters remaining: 0.00 L 
Minimal canisters needed: 2


Test 4

Data:
Distance - 122.23 | Fuel - 14 | Fuel price - 100 | Passengers - 2 |

Expected result:
Total distance: 244.46 km
Fuel needed: 34.22 L
Total fuel cost: 3422.44
Cost per person: 1711.22
Canisters needed: 1
Liters remaining: 14.22 L
Minimal canisters needed: 2

Result:
Total distance: 244.46 km
Fuel needed: 34.22 L
Total fuel cost: 3422.44
Cost per person: 1711.22
Canisters needed: 1
Liters remaining: 14.22 L
Minimal canisters needed: 2