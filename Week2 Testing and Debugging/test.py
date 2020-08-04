import unittest
from bank_account import BankAccount

class TestCase(unittest.TestCase):
    bank_account = BankAccount()
    def test_deposit_a(self):
        self.bank_account.deposit(50)
        self.assertEqual(self.bank_account.balance, 50)

    def test_deposit_b(self):
        self.bank_account.deposit(-10)
        self.assertEqual(self.bank_account.balance, 40)

if __name__ == '__main__':
    unittest.main()