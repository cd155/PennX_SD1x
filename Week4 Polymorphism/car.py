class Car:

    def __init__(self, owner_name, license_num, registration_num):
        self.__owner_name = owner_name
        self.__license_num = license_num
        self.__registration_num = registration_num
        self.__parking_location = 0
    
    def get_owner_name(self):
        return self.__owner_name
    
    def set_owner_name(self, new_name):
        self.__owner_name = new_name
    
    def get_owner_license_num(self):
        return self.__license_num
    
    def get_owner_registration_num(self):
        return self.__registration_num
    
    def get_parking_location(self):
        return self.__parking_location
    
    def set_parking_location(self, new_location):
        self.__parking_location = new_location

    def __str__(self):
        return self.__owner_name + " owned car " + self.__license_num
    
    def __eq__(self, other):
        return self.__owner_name == other.get_owner_name() and \
               self.__license_num == other.get_owner_license_num()

car1 = Car("John", "Iowa1", 1)
print(car1)

car2 = Car("Ted", "Iowa2", 1)
car3 = Car("John", "Iowa1", 1)
print(car1 == car2)
print(car1 == car3)