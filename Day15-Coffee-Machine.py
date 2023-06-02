MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(money_earned):
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money_earned}")


def check_resource(command):

        if resources['water'] >= MENU[command]['ingredients']['water']:
            if resources['coffee'] >= MENU[command]['ingredients']['coffee']:
                if resources['milk'] >= MENU[command]['ingredients']['milk']:
                    return True
                else:
                    print("Sorry, there is not enough Milk!")
                    return False
            else:
                print("Sorry, there is not enough Coffee!")
                return False
        else:
            print("Sorry, there is not enough Water!")
            return False


def take_money(command):

    quarters = int(input("Enter the number of quarters : "))
    dimes = int(input("Enter the number of dimes : "))
    nickels = int(input("Enter the number of nickels : "))
    pennies = int(input("Enter the number of pennies : "))

    total_paid = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies

    return total_paid - MENU[command]['cost']


def make_coffee(command):
    resources['water'] = resources['water'] - MENU[command]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[command]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[command]['ingredients']['coffee']


if __name__ == "__main__":

    machine_on = True
    money_earned = 0

    while machine_on:

        command = input("What would you like? (espresso/latte/cappuccino) : ")

        if command == 'off':
            machine_on = False
        elif command == 'report':
            print_report(money_earned)
        else:
            availability = check_resource(command)
            if availability:
                change = take_money(command)
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change")
                    make_coffee(command)
                    money_earned += MENU[command]['cost']
                    print(f"Here is your {command}. Enjoy!")
                elif change == 0:
                    make_coffee(command)
                    money_earned += MENU[command]['cost']
                    print(f"Here is your {command}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded")