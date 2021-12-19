class Category:
    """
    Instantiates objects based on different budget categories
    """
    def __init__(self, name):
        """
        Initialises instance variables, takes name parameter
        """
        self.name = name
        self.ledger = []

    def __str__(self):
        """
        Returns a string output of the object
        """
        heading = self.name.center(30, "*")
        string = f"{heading}\n"
        for entry in self.ledger:
            string += entry["description"][:23].ljust(23) + format(entry["amount"],".2f").rjust(7) + "\n"
        string += f"Total: {self.get_balance()}"
        return string
        
    def deposit(self, amount, description=""):
        """
        Appends a record of the deposit to the ledger
        """
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        """
        Checks required funds are avaliable and 
        appends a record to the legder if true
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        """
        Returns the current balance for the object
        """
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount, category):
        """
        Checks if required funds are avaliable and
        appends records of withdrawal and
        deposite to the respective objects ledgers
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        Returns true if the passed amount is 
        less than or equal to the current funds
        """
        funds = 0
        for entry in self.ledger:
            funds += entry["amount"]
        if amount > funds:
            return False
        else:
            return True

def create_spend_chart(categories):
    """
    Returns a string in the form of a graph
    representing the spend% per category
    """
    # init output string
    output = "Percentage spent by category"

    # calculating expenditure per category
    spend_amounts = {}
    for category in categories:
        spend = 0
        for dict in category.ledger:
            if dict["amount"] < 0:
                spend += dict["amount"]
        spend_amounts[category.name] = spend
    
    # total spend of all categories
    total_spend = sum(spend_amounts.values())

    # calculates spend percentage rounded down to nearest 10
    spend_percentages = {}
    for category in categories:
        percentage = (spend_amounts[category.name] / total_spend) * 100
        if int(percentage) > 9:
            spend_percentages[category.name] = int(str(percentage)[0] + "0")
        else:
            spend_percentages[category.name] = 0

    # y axis 
    # builds list of y axis strings working down from 100
    lines = []
    for i in reversed(range(11)):
        lines.append(f"\n{str(i * 10).rjust(3)}| ")

    # adds marker strings of the correct x,y positions
    for category in categories:
        for i in range(len(lines)):
            if spend_percentages[category.name] >= int(lines[i][1:4]):
                lines[i] += "o  "
            else:
                lines[i] += "   "

    # adds y axis lines to output string
    for line in lines:
        output += line

    # adds x axis '---' line to output string
    output += "\n    -" + "---" * len(categories) + "\n"

    # vertical names
    lengths = []
    for category in categories:
        lengths.append(len(category.name))

    # while there is characters in the category name
    # append the letter in the correct spot, else
    # append enough blank spaces to keep the other names aligned
    names_string = ""
    count = 0
    while count < max(lengths):
        for category in categories:
            if count < len(category.name):
                if category == categories[0]:
                    names_string += f"{category.name[count].rjust(6)}"
                elif category == categories[-1]:
                    names_string += f"{category.name[count].rjust(3)}  "
                else:
                    names_string += f"{category.name[count].rjust(3)}"
            else:
                if category == categories[0]:
                    names_string += "      "
                else:
                    names_string += "   "
        names_string += "\n"
        count += 1

    # adds the vertical names to the output string
    output += names_string[:-1]

    return output