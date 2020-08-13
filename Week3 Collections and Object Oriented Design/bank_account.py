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
print(a1.account_number, a2.account_number)