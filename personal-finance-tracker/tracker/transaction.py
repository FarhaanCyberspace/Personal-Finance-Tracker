import csv

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction_type, amount, category):
        self.transactions.append({
            "type": transaction_type,
            "amount": amount,
            "category": category
        })

    def get_transactions(self):
        return self.transactions

    def save_to_csv(self, file_path='data/transactions.csv'):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Amount", "Category"])
            for transaction in self.transactions:
                writer.writerow([transaction["type"], transaction["amount"], transaction["category"]])

    def load_from_csv(self, file_path='data/transactions.csv'):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            self.transactions = [row for row in reader]
