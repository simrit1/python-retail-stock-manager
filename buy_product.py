from inventory import inventory
from assets import total_assets


class Buy:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

        inventory["Quantity"][self.product_index()] += self.quantity
        inventory["Total Cost"][self.product_index()] = self.total_cost()

        self.cash_decrease()

    def product_index(self):
        product_index = inventory["Product"].index(self.name)
        return product_index

    def total_cost(self):
        total_cost = inventory["Quantity"][self.product_index()] * inventory["Price"][self.product_index()]
        return total_cost

    def cash_decrease(self):
        buying_price = inventory["Price"][self.product_index()]
        cash_dec = float(buying_price * self.quantity)
        total_assets["Cash"][0] -= cash_dec