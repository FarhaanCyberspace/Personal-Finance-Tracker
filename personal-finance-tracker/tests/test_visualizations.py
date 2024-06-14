import unittest
from tracker.transaction import TransactionManager
from tracker.visualizations import VisualizationManager

class TestVisualizationManager(unittest.TestCase):
    def setUp(self):
        self.transaction_manager = TransactionManager()
        self.visualization_manager = VisualizationManager(self.transaction_manager)

    def test_generate_visualizations(self):
        self.transaction_manager.add_transaction("Expense", 100, "Food")
        self.transaction_manager.add_transaction("Expense", 50, "Transport")
        
        # This test simply ensures no exceptions are raised during visualization
        try:
            self.visualization_manager.generate_visualizations()
        except Exception as e:
            self.fail(f"generate_visualizations raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
