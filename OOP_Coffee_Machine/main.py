from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Menu Object -> Methods: get_items(), find_drink(order_name)
coffee_menu = Menu()

#
price = MoneyMachine()

# coffee maker Object -> Methods: report(), is_resource_sufficient(drink)
coffee_making = CoffeeMaker()

# object menu item -> attributes: name, cost, ingredients
object_menu_item = MenuItem

machine_operation = True


while machine_operation:
    user_choice = input(f'What would you like to have: {coffee_menu.get_items()} ').lower()\

    if user_choice == 'report':
        print(coffee_making.report())
        print(price.report())
    elif user_choice == 'off':
        machine_operation = False
    else:
        found_drink = (coffee_menu.find_drink(user_choice))
        if coffee_making.is_resource_sufficient(found_drink) and price.make_payment(found_drink.cost) == True:
            coffee_making.make_coffee(found_drink)




