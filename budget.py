class Category:
    def __init__(self):
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):  # not ready
        for each in self.ledger:
            curr_amount = 0
            curr_amount += each["amount"]

        negative_amount = amount * -1
        if curr_amount >= amount:
            self.ledger.append(
                {"amount": negative_amount, "description": description})
            return True
        else:
            return False


budget = Category()

budget.deposit(50, "apples")

if budget.withdraw(51, "apples"):
    print("git")
else:
    print("dupa")

print(budget.ledger)


def create_spend_chart(categories):
    none = 0
