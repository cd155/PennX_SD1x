class BankAccountQuizTwo:
    def __init__(self, account_owner = None):
        self.balance = 27
        self.account_owner = account_owner

    def deposit(self, amount):
        self.balance += amount
    
    def equals(self, bank_account):
        return bank_account.account_owner == self.account_owner