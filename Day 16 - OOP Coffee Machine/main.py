from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
manage_money = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        quit()
    if choice == "report":
        coffee_machine.report()
        manage_money.report()
    else:
        order = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(order) and manage_money.make_payment(order.cost):
            coffee_machine.make_coffee(order)

