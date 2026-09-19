dist = float(input("Enter a trip distance(km): "))
fuel = float(input("Enter fuel consumption (L/100km): "))
price = float(input("Enter fuel price (per L): "))
passengers = int(input("Enter passenger count: "))

full_dist = dist*2
fuel_needed = fuel * (full_dist/100)
total_fuel_cost = fuel_needed * price
cost_per_person = total_fuel_cost / passengers

canisters_capacity = 20 #int(input("Enter canister capacity (L): "))
canisters = int(fuel_needed // canisters_capacity)
liters_remaining = fuel_needed % canisters_capacity
minimal_needed_canisters = int(-(-fuel_needed//canisters_capacity))

print(f"Total distance: {full_dist} km")
print(f"Fuel needed: {fuel_needed:.2f} L")
print(f"Total fuel cost: {total_fuel_cost:.2f}")
print(f"Cost per person: {cost_per_person:.2f}")
print(f"Canisters needed: {canisters}")
print(f"Liters remaining: {liters_remaining:.2f} L")
print(f"Minimal canisters needed: {minimal_needed_canisters}")