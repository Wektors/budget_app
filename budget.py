class Category:
    def __init__(self, name):
        self.name = name
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
    
    def transfer(self, amount, another_cat):
        self.withdraw(amount, "Transfer from " + self.name)
        another_cat.deposit(amount, "Transfer to " + self.name)

budget = Category("budget")

budget.deposit(50, "initial")

savings = Category("savings")

savings.deposit(50, "initialfunds")

budget.transfer(30, savings)

print(budget.get_balance())

print(savings.get_balance())


def create_spend_chart(categories):
    none = 0
