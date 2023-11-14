from data import MENU, resources


def report():
    """Print the amount of resources available."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(type_of_coffee):
    """Returns true or false depending on the availability resources."""
    for ingredient in MENU[type_of_coffee]["ingredients"]:
        if resources[ingredient] < MENU[type_of_coffee]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def calculate_money(type_of_coffee):
    """Calculate the total money and check if is enough to make a coffe"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_value = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if total_value < MENU[type_of_coffee]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += MENU[type_of_coffee]['cost']
        change = total_value - MENU[type_of_coffee]['cost']
        print(f"Here is ${round(change,2)} in change.")
        return True


def remove_resource(type_of_coffee):
    """Remove resource after making the coffee"""
    for ingredient in MENU[type_of_coffee]["ingredients"]:
        resources[ingredient] -= MENU[type_of_coffee]["ingredients"][ingredient]


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        report()
    elif user_input == "off":
        quit()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_resources(user_input):
            if calculate_money(user_input):
                remove_resource(user_input)
                print(f"Here is your {user_input} ☕️. Enjoy!")
    else:
        print("Please enter a valid order.")
