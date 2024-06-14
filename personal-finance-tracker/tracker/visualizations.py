import matplotlib.pyplot as plt

class VisualizationManager:
    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def generate_visualizations(self):
        transactions = self.transaction_manager.get_transactions()
        categories = list(set(t["category"] for t in transactions))
        amounts = [sum(float(t["amount"]) for t in transactions if t["category"] == category) for category in categories]

        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts)
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expenses by Category')
        plt.show()
