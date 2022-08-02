from inventory import inventory
from assets import total_assets


class Sell:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

        inventory["Quantity"][self.product_index()] -= self.quantity
        inventory["Total Cost"][self.product_index()] = self.total_cost()

        self.cash_increase()
        self.gross_profits()

    def product_index(self):
        product_index = inventory["Product"].index(self.name)
        return product_index

    def total_cost(self):
        total_cost = inventory["Quantity"][self.product_index()] * inventory["Price"][self.product_index()]
        return total_cost

    def cash_increase(self):
        selling_price = inventory["Selling Price"][self.product_index()]
        cash_inc = float(selling_price * self.quantity)
        total_assets["Cash"][0] += cash_inc

    def gross_profits(self):
        product_profit_margin = inventory["Profit Margin"][self.product_index()]
        product_gross_profits = float(self.quantity * product_profit_margin)
        total_assets["Total Gross Profits"][0] += product_gross_profits