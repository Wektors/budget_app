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
            self.ledger.append({"amount": negative_amount, "description": description})
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

        title_line = "".join(asts) + extra_ast + self.name + "".join(asts) + "\n"

        second_line = ""

        for item in self.ledger:
            desc = str(item["description"])
            spacing = ""
            value = str("{:.2f}".format(float(item["amount"]) * 1.00, 0))
            for i in range(30 - len(desc) - len(value)):
                spacing += " "

            second_line += desc[0:23] + spacing + value[0:7] + "\n"

        sum = 0
        for each in self.ledger:
            sum += each["amount"]

        third_line = "Total: " + str("{:.2f}".format(float(sum) * 1.00, 0))
        return title_line + second_line + third_line


def create_spend_chart(categories):
    def get_spends(category):
        sum = 0
        for each in category.ledger:
            if each["amount"] < 0:
                sum += each["amount"]
        return sum

    spend_list = []

    for each in categories:
        spend_list.append(
            [
                get_spends(each),
                each.name,
            ]
        )

    spend_sum = 0

    for each in spend_list:
        spend_sum += each[0]

    longest_name = spend_list[0][1]

    for each in spend_list:
        if len(each[1]) > len(longest_name):
            longest_name = each[1]

    total_spends = 0

    for each in spend_list:
        total_spends += each[0]

    for each in spend_list:  # add percentages to the list
        each.append(round((each[0] / total_spends) * 100))

    sorted_spend_list = sorted(spend_list)

    print(sorted_spend_list)

    percentage_list = [
        "100|",
        " 90|",
        " 80|",
        " 70|",
        " 60|",
        " 50|",
        " 40|",
        " 30|",
        " 20|",
        " 10|",
        "  0|",
    ]

    perc_lines = ""

    for each in sorted_spend_list:
        perc = int(each[2] / 10)
        to_empty = 9 - perc
        count = 0
        while count < to_empty:
            percentage_list[count] += "   "
            count += 1
        while to_empty <= 10:
            percentage_list[to_empty] += " o "
            to_empty += 1

    for each in percentage_list:
        perc_lines += each + "\n"

    hyphens = "    --"

    for each in categories:
        hyphens += "---"

    names_list = []
    for category in sorted_spend_list:
        letter_list = []
        for letter in category[1]:
            letter_list.append(letter)
        names_list.append(letter_list)

    name_lines = []
    for each in longest_name:
        name_lines.append(["     "])

    for each in names_list:
        count = 0
        for letter in each:
            name_lines[count] += str(letter) + "  "
            count += 1

    name_lines_str = ""

    for each in name_lines:
        each_str = ""
        for letter in each:
            each_str += letter
        name_lines_str += "\n" + each_str

    result = "Percentage spent by category \n" + perc_lines + hyphens + name_lines_str

    return result


budget = Category("budget")

budget.deposit(50, "initial")
budget.withdraw(5, "initial")

savings = Category("savings")

savings.deposit(50, "initialfunds")
savings.withdraw(45, "initial")

Tips = Category("Tips")

Tips.deposit(50, "initialfunds")
Tips.withdraw(25, "initial")

print(create_spend_chart([budget, savings, Tips]))
