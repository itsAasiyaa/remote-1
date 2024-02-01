import random

def modelYear():
    year = [2021, 2022, 2023, 2024]
    return random.choice(year)

print("This is file cars.py")
cars = ["GMC", "Audi", "Mercedes-Benz", "Lexus"]
print("Randomly selected car:",random.choice(cars))
print("Randomly selected model year:",modelYear())
