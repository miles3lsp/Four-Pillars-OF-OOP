# Base parent class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.brand}, Year: {self.year}")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, year, max_speed):
        super().__init__(brand, year) # Reuse parent constructor
        self.max_speed = max_speed

    def drive(self):
        print(f"{self.brand} is driving at {self.max_speed} km/h.")

my_car = Car("Tesla", 2024, 250)
my_car.display_info()
my_car.drive()