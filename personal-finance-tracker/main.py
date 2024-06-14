from tracker.transaction import TransactionManager
from tracker.report import ReportManager
from tracker.visualizations import VisualizationManager
from tracker.goal import GoalManager

def main():
    # Initialize managers
    transaction_manager = TransactionManager()
    report_manager = ReportManager(transaction_manager)
    visualization_manager = VisualizationManager(transaction_manager)
    goal_manager = GoalManager()

    # Example usage
    transaction_manager.add_transaction("Income", 5000, "Salary")
    transaction_manager.add_transaction("Expense", 50, "Food")
    
    report_manager.generate_report()
    visualization_manager.generate_visualizations()
    goal_manager.set_goal("Save for Vacation", 2000)

if __name__ == "__main__":
    main()
