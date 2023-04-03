class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def check_funds(self, amount):
        curr_amount = 0
        for each in self.ledger:
            curr_amount += each["amount"]
        if curr_amount >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):

        negative_amount = amount * -1
        if self.check_funds(negative_amount):
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

        if self.check_funds(amount):
            self.withdraw(amount, "Transfer from " + self.name)
            another_cat.deposit(amount, "Transfer to " + self.name)
            return True

        else:
            return False

    def __str__(self):
        asts = []  # asterisks
        for each in range(round((29 - len(self.name)) / 2)):
            asts.append("*")

        if len(self.name) % 2 == 0:
            extra_ast = ""
        else:
            extra_ast = "*"

        title_line = ''.join(asts) + extra_ast + \
            self.name + ''.join(asts) + "\n"

        second_line = ""

        for item in self.ledger:
            desc = str(item["description"])
            spacing = ""
            value = str("{:.2f}".format(float(item["amount"]) * 1.00, 0))
            for i in range(30 - len(desc) - len(value)):
                spacing += " "
            total = 0

            second_line += desc[0:23] + spacing + value[0:7] + "\n"

        sum = 0
        for each in self.ledger:
            sum += each["amount"]

        third_line = "Total: " + str("{:.2f}".format(float(sum) * 1.00, 0))
        return title_line + second_line + third_line


budget = Category("budget")

budget.deposit(50, "initial")
budget.withdraw(5, "initial")


savings = Category("savings")

savings.deposit(50, "initialfunds")
savings.withdraw(45, "initial")


def create_spend_chart(categories):

    def get_spends(category):
        sum = 0
        for each in category.ledger:
            if each["amount"] < 0:
                sum += each["amount"]

        return sum

    spend_list = []

    for each in categories:
        spend_list.append([get_spends(each), each.name, 0])

    spend_sum = 0

    for each in spend_list:
        spend_sum += each[0]

    for each in spend_list:  # add percentages to the list
        each[2] = int(round(each[0] / spend_sum, 1) * 100)

    percentage_list = ["100|", " 90|", " 80|", " 70|",
                       " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]

    perc_lines = ""

    for each in percentage_list:
        perc_lines += each + "\n"

    hyphens = "    --"

    for each in categories:
        hyphens += "---"

    hyphens += "\n"

    longest_name = spend_list[0][1]

    for each in spend_list:
        if len(each[1]) > len(longest_name):
            longest_name = each[1]

    sorted_spend_list = sorted(spend_list)

    names_list = []
    curr_cat = 0
    for category in sorted_spend_list:
        names_list.append([])
        for letter in category[1]:
            names_list[curr_cat].append(letter)
        curr_cat += 1

    name_lines = []


    result="Percentage spent by category \n" + str(name_lines)
    perc_lines + hyphens + str(spend_list)

    return result


print(create_spend_chart([budget, savings]))
