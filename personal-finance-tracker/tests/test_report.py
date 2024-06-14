import unittest
from tracker.transaction import TransactionManager
from tracker.report import ReportManager
from io import StringIO
import sys

class TestReportManager(unittest.TestCase):
    def setUp(self):
        self.transaction_manager = TransactionManager()
        self.report_manager = ReportManager(self.transaction_manager)

    def test_generate_report(self):
        self.transaction_manager.add_transaction("Income", 1000, "Salary")
        self.transaction_manager.add_transaction("Expense", 200, "Food")
        
        captured_output = StringIO()
        sys.stdout = captured_output
        self.report_manager.generate_report()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Total Income: $1000.0", output)
        self.assertIn("Total Expenses: $200.0", output)
        self.assertIn("Total Savings: $800.0", output)

if __name__ == '__main__':
    unittest.main()
