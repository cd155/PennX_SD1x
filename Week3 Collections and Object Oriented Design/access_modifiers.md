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