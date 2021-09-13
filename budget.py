class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.catwith = 0


    def deposit(self, amount, description = ""):
#        self.amount = amount
#        self.description = description
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += (i["amount"])
        return balance

    def withdraw(self, amount, description = ""):
#        self.amount = amount
#        self.description = description
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.catwith += amount
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

    def transfer(self, amount, transferto):
#        self.amount = amount
#        self.transferto = transferto
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": "Transfer to {}".format(transferto.name)})
            transferto.ledger.append({"amount": amount, "description": "Transfer from {}".format(self.name)})
            return True
        else:
            return False

    def __str__(self):
        title = str(self.name.center(30,"*")) + '\n'
        body = ''
        for i in self.ledger:
            body += i["description"][:23].ljust(23) + str("{:.2f}".format(i["amount"]))[:7].rjust(7) + '\n'
        total = "Total: " + str("{:.2f}".format(self.get_balance()))
        return title + body + total

def create_spend_chart(categories):
    spend_chart = "Percentage spent by category"
    y_axis = []
    x_label = []
    totalspend = 0
    maxlength = 0
    percent = []
    bars = []
    catnames = []

    for i in range(100, -10, -10):
        y_axis.append("\n" + str(i).rjust(3) + "|")

    for category in categories:
        totalspend += category.catwith
        catnames.append(category.name)

    for category in categories:
        percent.append(100 * category.catwith / totalspend)

    for catpercent in percent:
        for i in range(11):
            if len(bars) <= 10:
                if catpercent > (10 * (10-i)):
                    bars.append(" o ")
                else:
                    bars.append("   ")
            else:
                if catpercent > (10 * (10-i)):
                    bars[i] += " o "
                else:
                    bars[i] += "   "

    for name in catnames:
        if maxlength < len(name):
            maxlength = len(name)

    for i in range(maxlength):
        x_label.append("    ")
        for name in catnames:
            try:
                x_label[i] += (" " + name[i] + " ")
            except:
                x_label[i] += ("   ")
        x_label[i] += " \n"

    for a, b in zip(y_axis, bars):
        spend_chart += a + b + " "

    spend_chart += "\n    " + "-" * (len(percent) * 3 + 1) + "\n"

    for i in x_label:
        spend_chart += i

    spend_chart = spend_chart.rstrip("\n")

    return spend_chart
