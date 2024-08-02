class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category

    def __str__(self):
        return (f"Vehicle ID: {self.vehicle_id} | Make: {self.make} | Model: {self.model} | Year: {self.year} | Category: {self.category}")


class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = []
        self.vehicle_set = set()
        self.categorized_vehicles = {}

    def add_vehicle(self, vehicle):
        if vehicle.vehicle_id not in self.vehicle_set:
            self.vehicles.append(vehicle)
            self.vehicle_set.add(vehicle.vehicle_id)
            self.categorize_vehicles()
            print("Vehicle " + vehicle.vehicle_id + " added successfully")
        else:
            print("Vehicle already exists")

    def remove_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                self.vehicles.remove(vehicle)  #
                self.vehicle_set.remove(vehicle_id)
                self.categorize_vehicles()
                print("Vehicle " + vehicle_id + " removed successfully")
                return
        print("Vehicle not found")

    def search_vehicles(self, search_term):
        result = [vehicle for vehicle in self.vehicles if search_term in vehicle.make or search_term in vehicle.model]
        return result

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def categorize_vehicles(self):
        self.categorized_vehicles = {}
        for vehicle in self.vehicles:
            if vehicle.category not in self.categorized_vehicles:
                self.categorized_vehicles[vehicle.category] = []
            self.categorized_vehicles[vehicle.category].append(vehicle)

    def display_categorized_vehicles(self):
        for category, vehicles in self.categorized_vehicles.items():
            print(f"Category: {category}")
            for vehicle in vehicles:
                print(vehicle)
            print()



system = VehicleRentalSystem()


vehicle1 = Vehicle("V1", "Toyota", "Supra", "2011", "Sports")
vehicle2 = Vehicle("V2", "Hyundai", "Creta", "2020", "SUV")
vehicle3 = Vehicle("V3", "Ford", "Mustang", "2020", "Sports")
vehicle4 = Vehicle("V4", "Toyota", "Camry", "2012", "Sedan")
vehicle5 = Vehicle("V5", "Mercedes", "Maybach", "2012", "Sedan")

system.add_vehicle(vehicle1)
system.add_vehicle(vehicle2)
system.add_vehicle(vehicle3)
system.add_vehicle(vehicle4)
system.add_vehicle(vehicle5)

system.list_vehicles()


system.display_categorized_vehicles()


search_results = system.search_vehicles("Mercedes")
for vehicle in search_results:
    print(vehicle)


system.remove_vehicle("V3")

system.list_vehicles()
