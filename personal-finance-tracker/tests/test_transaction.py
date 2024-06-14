import unittest
from tracker.transaction import TransactionManager

class TestTransactionManager(unittest.TestCase):
    def setUp(self):
        self.manager = TransactionManager()

    def test_add_transaction(self):
        self.manager.add_transaction("Income", 1000, "Salary")
        self.assertEqual(len(self.manager.get_transactions()), 1)

    def test_save_load_csv(self):
        self.manager.add_transaction("Income", 1000, "Salary")
        self.manager.save_to_csv("test_transactions.csv")
        self.manager.transactions = []  # Clear current transactions
        self.manager.load_from_csv("test_transactions.csv")
        self.assertEqual(len(self.manager.get_transactions()), 1)

if __name__ == '__main__':
    unittest.main()
