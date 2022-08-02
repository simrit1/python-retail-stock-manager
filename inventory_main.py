from report import report_inventory, report_total_assets

from new_product import NewProduct

from sell_product import Sell
from buy_product import Buy

from assets import total_assets

cash = float(input("Cash opening balance: "))
total_assets["Cash"][0] = cash


on = True
while on:
    admin = input("\n1. Add a new product.\n2. Buy/Sell a product.\n3. Print a report.\n")

    if admin == "1":
        name = input("Name: ")
        quantity = float(input("Quantity: "))
        cost = float(input("Cost: "))
        profit_margin_percentage = float(input("Profit margin percentage: %")) / 100.0

        new_product = NewProduct(name, quantity,  cost, profit_margin_percentage)
    elif admin == "2":
        choice = input("1. Sell.\n2. Buy.\n")

        if choice == "1":
            name = input("Name: ")
            quantity = float(input("Quantity: "))
            sell = Sell(name, quantity)

        elif choice == "2":
            name = input("Name: ")
            quantity = float(input("Quantity: "))
            buy = Buy(name, quantity)
    elif admin == "3":
        report_inventory()
        report_total_assets()
        print("A report is printed in /reports")
    elif admin == "0":
        on = False