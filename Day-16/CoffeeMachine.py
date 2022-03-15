from coffee_maker import CoffeeMaker
from money_machine import MONEYMACHINE
from menu import MENU

is_on = True

coffee_maker = CoffeeMaker()
menu = MENU()
money_machine = MONEYMACHINE()

while is_on:
    choice = input(f"What would you like? ({menu.get_item()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficent(drink.ingredients):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)