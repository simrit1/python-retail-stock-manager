from inventory import inventory
from assets import total_assets


def product_code_generator():
    if not inventory["Code"]:
        new_code = 0
    else:
        last_code = inventory["Code"][-1]
        new_code = last_code + 1
    return new_code


class NewProduct:
    def __init__(self, name, quantity, cost, profit_margin_percentage):
        self.name = name
        self.quantity = quantity
        self.cost = cost
        self.profit_margin_percentage = profit_margin_percentage
        self.code = product_code_generator()

        inventory["Product"].append(self.name)
        inventory["Quantity"].append(self.quantity)
        inventory["Price"].append(self.cost)
        inventory["Total Cost"].append(self.total_cost())
        inventory["Profit Margin"].append(self.profit_margin())
        inventory["Selling Price"].append(self.selling_price())
        inventory["Code"].append(self.code)

        self.cash_decrease()

    def total_cost(self):
        total_cost = self.quantity * self.cost
        return total_cost

    def profit_margin(self):
        profit_margin = self.profit_margin_percentage * self.cost
        return profit_margin

    def selling_price(self):
        selling_price = self.cost + self.profit_margin()
        return selling_price

    def cash_decrease(self):
        cash_dec = float(self.cost * self.quantity)
        total_assets["Cash"][0] -= cash_dec