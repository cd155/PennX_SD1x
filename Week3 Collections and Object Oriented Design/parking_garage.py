from car import Car

class ParkingGarage:
    
    def __init__(self, spots) -> None:
        self.__spots = spots
        self.__cars = []
        for _ in range(spots):
            self.__cars.append(None)
        
    
    def park(self, car_to_be_parked):
        i = 0
        while i < len(self.__cars) and self.__cars[i] != None:
            i += 1
        
        if i == len(self.__cars):
            return False
        
        # i will now be the first empty spot
        self.__cars[i] = car_to_be_parked

        # car's parking spot is being set
        car_to_be_parked.set_parking_location(i)
        return True

car1 = Car("John", "ABC100", 1)
car2 = Car("Ted", "TH000", 2)
car3 = Car("Tracy", "XYZ88", 3)

print(car1.get_owner_name(), car1.get_owner_license_num(), car1.get_owner_registration_num())

# change car1's owner name
car1.set_owner_name("Mike")

print(car1.get_owner_name(), car1.get_owner_license_num(), car1.get_owner_registration_num())
print(car2.get_owner_name(), car2.get_owner_license_num(), car2.get_owner_registration_num())
print(car3.get_owner_name(), car3.get_owner_license_num(), car3.get_owner_registration_num())

parking_garage = ParkingGarage(2)
print(parking_garage.park(car1))
print(parking_garage.park(car2))
print(parking_garage.park(car3))