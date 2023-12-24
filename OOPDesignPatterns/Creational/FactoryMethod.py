# Define Vehicle classes
class Car:
    def drive(self):
        return "Car is driving"

class Truck:
    def drive(self):
        return "Truck is driving"

class Motorcycle:
    def drive(self):
        return "Motorcycle is driving"

# Define Vehicle Factory
class VehicleFactory:
    def get_vehicle(self, vehicle_type):
        if vehicle_type == "Car":
            return Car()
        elif vehicle_type == "Truck":
            return Truck()
        elif vehicle_type == "Motorcycle":
            return Motorcycle()
        else:
            raise ValueError("Unknown vehicle type")

# Using the factory to create instances
factory = VehicleFactory()
car = factory.get_vehicle("Car")
print(car.drive())  # Outputs: Car is driving
