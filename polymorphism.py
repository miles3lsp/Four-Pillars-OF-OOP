class Plane:
    def move(self):
        print("The plane is flying in the sky")

class Ship:
    def move(self):
        print("The ship is sailing on the water")

# Same function calls the same method name but behaves differently depending on the object
def start_journey(vehicle_object):
    vehicle_object.move()

plane = Plane()
ship = Ship()

start_journey(plane)
start_journey(ship)