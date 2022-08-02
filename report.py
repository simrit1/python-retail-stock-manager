from inventory import inventory
from assets import total_assets
import pandas


def report_inventory():
    inventory_reported = pandas.DataFrame(inventory)
    inventory_reported.to_csv("reports/current_inventory.csv")
    print(inventory_reported)
    print("\n")


def report_total_assets():
    total_cost_list = inventory["Total Cost"]
    total_inventory = 0
    for total_cost in total_cost_list:
        total_inventory += total_cost
    total_assets["Total Inventory"] = total_inventory

    assets_reported = pandas.DataFrame(total_assets)
    assets_reported.to_csv("reports/total_assets.csv")
    print(assets_reported)