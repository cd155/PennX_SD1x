import unittest
from bank_account_quiz_two import BankAccountQuizTwo

class TestBankAccountQuizTwo(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccountQuizTwo("default")

    def tearDown(self):
        self.bank_account = None

    def test_deposit(self):
        self.assertLessEqual(abs(self.bank_account.balance - 27), 0.1)
        self.bank_account.deposit(1)
        self.assertLessEqual(abs(self.bank_account.balance - 28), 0.1)
    
    def test_owner1(self):
        self.assertEqual(self.bank_account, BankAccountQuizTwo("default"))
    
    def test_owner2(self):
        print("double start: " + str(self.bank_account == BankAccountQuizTwo("default")))
        self.assertTrue(self.bank_account == BankAccountQuizTwo("default"))

    def test_owner3(self):
        self.assertTrue(self.bank_account.equals(BankAccountQuizTwo("default")))

if __name__ == '__main__':
    unittest.main()