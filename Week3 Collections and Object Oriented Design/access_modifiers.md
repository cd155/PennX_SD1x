# Class video 3.4a
- What does static mean?
- Static instance variables
- Static methods

### What does static mean?
- Think of static as belonging to the class and not to the individual instances of class.
- A static method means the method exists at the class level and is not specific to the instance.
- The one static method that you have in a lot of your classes is **main**.
- Used when you do not need an instance of the object.
- **Math.sqrt** is a method that computes the square root of a number. You do not need an instance of mathematics before you know how to compute the square root.
- classname.method

### Using static methods
- To use a static method called method1 in a class called Class1 the code is Class1.method1(parameters...)
- You do not have to create an instance of the class in order to invoke the method
- Many java utility functions are static methods. Almost all math function are static methods in the **Math** class.

### Static versus non-static
- Consider the Rational number class
- To reduce 2/4 to 1/2 a common thing to do is to compute the greatest common divisor. To compute the gcd you do not need an instance of a fraction.

### Static instance variables
- Static instance variables are used if you want some information to be shared by **every instance of a class**.
- A common use case is constants
- For constants you also get to see the keyword **final**. Final meaning you do not get to override this value in any manner.
- **Python neither constant nor final are existed in python**. We can create a constant class to minic constant class that similar to Java.
- In Python, it doesn’t require a static keyword. All variables which are assigned a value in class declaration are static class variables. And variables which are assigned values inside methods are instance variables.

# Class video 3.4b
### Example: Bank Accoumt
```python
from customer import Customer

class BankAccount:
    # counts the number of account made. Shared across all instances
    counter = 10000
    def __init__(self, name, age):
        self.balance = 0
        self.customer = Customer(name, age)
        BankAccount.counter += 1
        # first account will have account number = 10,001
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

a1 = BankAccount("John", 35)
a2 = BankAccount("Ted", 16)
```

### Example: Customer
```python
class Customer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

# Class video 3.5
- Access modifiers
- What is private, public?
- What if we don't write any modifier?

### Access modifier
- Every instance variable and every method can be given one of 4 access modifiers
    - public
    - protected
    - private
    - default - no modifier provided at all
- Python default variables are public
- We will discuss what protected means later after we have covered inheritance.

### public instance variables
- With an access modifier being public the instance variable or method can be directly accessed, even outside the class.
- In example below, the Spy class can go and change the id of a Human object because the id has a public access modifier.
```python
class Human:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Spy:
    def change_id(human, new_id):
        human.id = new_id
```

### private instance variables
- For the same example(Human, Spy), if the id is made private then it cannot be accessed in the Spy class.
- It can still be accessed within the Human class
```python
class Human:
    def __init__(self, id, name):
        self.id = id
        # make name variable private
        self.__name = name

    def change_id(self, new_id):
        # same class works fine
        self.id = new_id

class Spy:
    def change_id(human, new_id):
        # this line of code no longer work
        human.id = new_id
```
### Default access modifier
- What happens if you leave out the private/public
- The default access is for every class inside the same package to be able to access the instance variable while classes in different packages cannot do so.
- This is quite uncommon in the actual software industry. Avoid it unless there is a very specific need.

### Best practice for instance variables
- The first preference for any instance variable is to make it private
- You still want to be able to access these instance variables. The correct way of doing so is via accessors and mutators
- Accessors and mutators
    - Also called getters and setters
```python
class Student:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

# print student's name in the student list
for student in students:
    print(student.get_name())
```

### public methods
- The method can be accessed from any other class.
- Public methods are the primary manner in which two classes communicate with each other
- Think of a public method as a service that one class is providing to another.

### private methods
- A private method can only be accessed within the class
- Common use case - Helper methods
```python
class Student:
    def __init__(self, age):
        self.__age = age

    def set_age(self, new_age):
        if __verify_age(new_age):
            self.__age = new_age
    
    # set a private method
    def __verify_age(age):
        return age>=1
```

### Summary
| Modifier | Class | Package | World |
|---|---|---|---|
| public | Y | Y | Y |
| default | Y | Y | N |
| private | Y | N | N |
World means any class that is outside the package.

### Quiz 3.2
The goal of the quiz is to test your understanding of the content covered in the lectures. We expect you to be able to solve the quiz questions without having to type any of the code into Eclipse.
```Java
public class Brilliant{
    static int enigma = 0;
    String name;
    int age;

    Brilliant(String name, int age){
        this.name = name;
        this.age = age;
        enigma++;
    }

    void doMagic(int trick){
        enigma = enigma + trick;
    }

    public static void main(String[] args){
        Brilliant sherry = new Brilliant("you", 24);
        System.out.println(sherry.enigma);
        sherry.doMagic(679);
        Brilliant suki = new Brilliant("anonymous", 24);
        System.out.println(suki.enigma);
    }
}
```
# Class video 3.6
- Hands on example of cars being parked in a parking garage
- We will design a car object and a parking garage object in Python

### Design
- Car
- Parking garage = Collection of cars
```python
# ParkingGarage class
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
```
```python
# Car class
class Car:

    def __init__(self, owner_name, license_num, registration_num) -> None:
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
```