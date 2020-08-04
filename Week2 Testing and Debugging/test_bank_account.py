import unittest
from bank_account import BankAccount

class TestBankAccountCase(unittest.TestCase):
    # start test
    def setUp(self):
        self.bank_account = BankAccount()

    # end test
    def tearDown(self):
        self.bank_account = None

    def test_one_deposit(self):
        self.bank_account.deposit(50)
        self.assertEqual(self.bank_account.balance, 50)

    def test_two_deposit(self):
        self.bank_account.deposit(50)
        self.bank_account.deposit(-10)
        self.assertEqual(self.bank_account.balance, 40)

if __name__ == '__main__':
    # start unit test
    # unittest.main()

    # start unit test with more details
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBankAccountCase)
    unittest.TextTestRunner(verbosity=2).run(suite)