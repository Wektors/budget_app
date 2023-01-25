class Category:
    def __init__(self):
        self.ledger = []
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

budget = Category()
budget.deposit(50, "apples")
print(budget.ledger)


def create_spend_chart(categories):
    none = 0

