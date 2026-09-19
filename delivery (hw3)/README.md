# Homework 3 - Delivery  

## What the program does 

The program selects a delivery method based on:
    1. order cost
    2. mass
    3. distance
    4. whether the item is fragile

The program does not calculate the delivery price.

## Boolean variables

`check` — checks if input data is invalid.
`self_pickup` — checks if the distance is 0.
`a_delivery` — checks if a fragile item weighs more than 10 kg.
`free_delivery` — checks if free courier delivery is available.

## Priority of rules

The order of `if / elif / else` is important because only the first true condition is used.

For example, a fragile 12 kg item at 0 km must use self-pickup instead of showing that normal delivery is unavailable.

## Tests

### Test 1

Data:
Cost = 1500 | Mass = 10 | Distance = 20 | Fragile = "так"

Expected result:
Безкоштовна кур'єрська доставка

Result:
Безкоштовна кур'єрська доставка

### Test 2

Data:
Cost = 1499 | Mass = 10 | Distance = 20 | Fragile = "ні"

Expected result:
Платна кур'єрська доставка

Result:
Платна кур'єрська доставка

### Test 3

Data:
Cost = 2000 | Mass = 5 | Distance = 21 | Fragile = "ні"

Expected result:
Платна кур'єрська доставка

Result:
Платна кур'єрська доставка

### Test 4

Data:
Cost = 2000 | Mass = 5 | Distance = 20 | Fragile = "ні"

Expected result:
Безкоштовна кур'єрська доставка

Result:
Безкоштовна кур'єрська доставка

### Test 5

Data:
Cost = 1000 | Mass = 10 | Distance = 10 | Fragile = "так"

Expected result:
Платна кур'єрська доставка

Result:
Платна кур'єрська доставка

### Test 6

Data:
Cost = 2000 | Mass = 12 | Distance = 1 | Fragile = "так"

Expected result:
Звичайна доставка недоступна

Result:
Звичайна доставка недоступна

### Test 7

Data:
Cost = 2000 | Mass = 12 | Distance = 0 | Fragile = "так"

Expected result:
Самовивіз

Result:
Самовивіз

### Test 8

Data:
Cost = 2000 | Mass = 5 | Distance = 10 | Fragile = "можливо"

Expected result:
Некоректні дані

Result:
Некоректні дані

### Test 9

Data:
Cost = 2000 | Mass = 0 | Distance = 10 | Fragile = "ні"

Expected result:
Некоректні дані

Result:
Некоректні дані

### Test 10

Data:
Cost = -1 | Mass = 5 | Distance = 10 | Fragile = "ні"

Expected result:
Некоректні дані

Result:
Некоректні дані