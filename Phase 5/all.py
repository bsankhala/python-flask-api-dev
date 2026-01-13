from abc import ABC, abstractmethod


# Abstract Base Class
class Vehicle(ABC):

    total_rented = 0

    def __init__(self, vehicle_no, model, rent_per_day):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rent_per_day = rent_per_day
        self.__available = True

    def is_available(self):
        return self.__available

    def rent_out(self):
        self.__available = False
        Vehicle.total_rented += 1

    def return_back(self):
        self.__available = True
        Vehicle.total_rented -= 1

    @abstractmethod
    def calculate_rent(self, days):
        pass


class Car(Vehicle):

    def __init__(self, vehicle_no, model, rent_per_day):
        super().__init__(vehicle_no, model, rent_per_day)

    def calculate_rent(self, days):
        deposit = 2000
        return (self.rent_per_day * days) + deposit


class Bike(Vehicle):

    def __init__(self, vehicle_no, model, rent_per_day):
        super().__init__(vehicle_no, model, rent_per_day)

    def calculate_rent(self, days):
        deposit = 500
        return (self.rent_per_day * days) + deposit


class Customer:

    def __init__(self, name):
        self.name = name
        self.rented_vehicle = None

    def rent_vehicle(self, vehicle, days):
        if vehicle.is_available():
            vehicle.rent_out()
            self.rented_vehicle = (vehicle, days)
            print(self.name, "successfully rented", vehicle.model)
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        if self.rented_vehicle is None:
            print("No vehicle to return")
            return

        vehicle, days = self.rented_vehicle
        bill = vehicle.calculate_rent(days)
        vehicle.return_back()

        print("Vehicle returned:", vehicle.model)
        print("Total bill:", bill)

        self.rented_vehicle = None


# Predefined Vehicles
vehicles = [
    Car("CAR101", "Hyundai i20", 1200),
    Car("CAR102", "Maruti Swift", 1000),
    Bike("BIKE201", "Honda Shine", 300),
    Bike("BIKE202", "Royal Enfield", 600)
]


# Menu Program
customer = Customer("Arjun")

while True:
    print("\n--- Vehicle Rental System ---")
    print("1. View Available Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. Show Total Rented Vehicles")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAvailable Vehicles:")
        for v in vehicles:
            if v.is_available():
                print(v.vehicle_no, "-", v.model, "-", v.rent_per_day, "/day")

    elif choice == "2":
        print("\nSelect Vehicle:")
        for idx, v in enumerate(vehicles):
            print(idx, "-", v.model)

        vi = int(input("Enter vehicle number: "))
        days = int(input("Enter number of rental days: "))

        customer.rent_vehicle(vehicles[vi], days)

    elif choice == "3":
        customer.return_vehicle()

    elif choice == "4":
        print("Total vehicles currently rented:", Vehicle.total_rented)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
