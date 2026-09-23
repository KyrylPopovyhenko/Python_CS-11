cost = float(input("Введіть суму: "))
mass = float(input("Введіть масу: "))
dist = float(input("Введіть відстань: "))
fragile = input("Крихке?: ").lower().strip()

check = cost<0 or mass<=0 or dist<0 or (fragile!="так" and fragile!="ні")

self_pickup = dist == 0
a_delivery = fragile=="так" and mass>10

free_delivery = cost>=1500 and dist<=20 and mass<=15

if check:
    print("Некоректні дані")
elif self_pickup:
    print("Самовивіз")
elif a_delivery:
    print("Звичайна доставка недоступна")
elif free_delivery: 
    print("Безкоштовна кур'єрська доставка")
else:
    print("Платна кур'єрська доставка")