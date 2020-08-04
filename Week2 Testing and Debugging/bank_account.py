class BankAccount:
    def __init__(self, balance = 0, account_owner = None):
        self.balance = balance
        self.account_owner = account_owner

    def deposit(self, amount):
        self.balance = self.balance + amount