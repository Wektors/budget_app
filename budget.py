class Category:
    def __init__(self):
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        curr_amount = 0
        for each in self.ledger:
            curr_amount += each["amount"]

        negative_amount = amount * -1
        if curr_amount >= amount:
            self.ledger.append(
                {"amount": negative_amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        sum = 0
        for each in self.ledger:
            sum += each["amount"]
        return sum
    

budget = Category()

budget.deposit(50, "initial")

budget.withdraw(35, "apples")


print(budget.ledger)

print(budget.get_balance())

def create_spend_chart(categories):
    none = 0
