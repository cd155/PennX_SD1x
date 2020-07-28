from datetime import datetime

class Car:
    def __init__(self, make = None, model = None, year = None, 
    is_new = None, miles = None, owner = None):
        self.make = make
        self.model = model
        self.year = year
        self.is_new = is_new
        self.miles = miles
        self.owner = owner
    
    def sell(self, new_owner):
        self.owner = new_owner
        if self.is_new:
            self.is_new = False

    def is_older_than_ten(self):
        current_year = datetime.now().year
        if current_year - self.year > 10:
            return True
        else:
            return False
    
    def void_function(self):
        print("this is void function, return None")

# Create a default car instance
car_one = Car()

# Aceess class properties
car_one.make = "Toyota"  

# Create a defined car instance
car_two = Car("Audi", "A4", 2019, True, 8750.67, "Donna")
older_than_ten = car_two.is_older_than_ten()

# sell car to Mark
car_two.sell("Mark")
print("Car owned by " + car_two.owner)

# void method
car_two.void_function()