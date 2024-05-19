from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

########### Coffee Machine V2 ###########

# Objects
machine_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Global Variables
machine_on = True


# Function
def stop_cycle():
    global machine_on
    machine_on = False


def run_cycle():
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        current_item = machine_menu.find_drink(choice)
        enough_resources = coffee_maker.is_resource_sufficient(current_item)
        if enough_resources:
            if money_machine.make_payment(current_item.cost):
                coffee_maker.make_coffee(current_item)
                return
            else:
                return
        else:
            return
    elif choice == "off":
        stop_cycle()
        return
    else:
        return


while machine_on:
    try:
        run_cycle()
    except KeyboardInterrupt:
        print("\nMachine turned off. Goodbye!")
