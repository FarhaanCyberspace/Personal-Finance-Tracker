class ReportManager:
    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def generate_report(self):
        transactions = self.transaction_manager.get_transactions()
        income = sum(float(t["amount"]) for t in transactions if t["type"] == "Income")
        expenses = sum(float(t["amount"]) for t in transactions if t["type"] == "Expense")
        savings = income - expenses

        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expenses}")
        print(f"Total Savings: ${savings}")
