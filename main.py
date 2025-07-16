MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
        'quarters' : 0,
        'dimes' : 0,
        'nickel' : 0,
        'pennies' : 0,
    }


def coffee_choice():
    user_choice = input('''What would you like? (espresso/latte/cappuccino):''').lower()
    if user_choice == 'report':
        print(resources)
        print(f'Total Profit: {profit}')
        coffee_choice()
    elif user_choice == 'off':
        print('Machine turned off')
        return
    else:
        making_coffee(user_choice)


def making_coffee(choice):
    to_check = MENU[choice]['ingredients']
    for _ in to_check:
        if resources[_] <= to_check[_]:
            print(f'Sorry there is not enough {_}.')
            return
    process_coins(choice)

def process_coins(choice):
    global profit
    print('please insert coins')
    for _ in coins:
        number_of_coins = int(input(f'number of {_} coins: '))
        coins[_] = number_of_coins

    user_paid =(coins['quarters']*25+ coins['dimes']*10 + coins['nickel']*5 + coins['pennies'])/100
    print(user_paid)
    print(MENU[choice]['cost'])

    if user_paid <= MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        change = user_paid - MENU[choice]['cost']
        print(f"Here is ${round(change,2)} dollars in change.")
        profit += MENU[choice]['cost']
    to_check = MENU[choice]['ingredients']
    for _ in to_check:
        resources[_] -= to_check[_]

    print(f'Here is your {choice}. Enjoy!')
    coffee_choice()



coffee_choice()