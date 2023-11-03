import random
brands_of_car = {
    "BMW": {'fuel': 100, "strength": 100, 'consumption': 6},
    "Ford": {'fuel': 80, "strength": 80, 'consumption': 8},
    "Lada": {'fuel': 40, "strength": 20, 'consumption': 12},
    "Volvo": {'fuel': 60, "strength": 150, 'consumption': 10}
}

print(list(brands_of_car))

brand = random.choice(list(brands_of_car))
print(brand)
print(brands_of_car[brand])
print(brands_of_car[brand]['strength'])