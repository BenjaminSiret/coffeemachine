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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


# TODO 1. Prompt user by asking "what would you like ? (espresso, latte, cappuccino): "
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3. Print report
# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee.


# FUNCTIONS

def check_resources(drink):
    """check if there is enough resources to make a drink"""
    for key, value in MENU[drink]["ingredients"].items():
        if resources[key] < value:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def coins_calculator(quarters, dimes, nickels, pennies):
    """take the numbers of coins, return the sum in dollars"""
    quarters *= QUARTER
    dimes *= DIME
    nickels *= NICKEL
    pennies *= PENNY
    return quarters + dimes + nickels + pennies


def monetary_calculator(coins, coffee_price):
    """take coins and coffee_price, return rounded difference between"""
    diff = coins - coffee_price
    return round(diff, 2)


def check_transaction(coins, coffee_price):
    """take coins and coffee_price, return true if transaction possible and add price to money, else return false"""
    if coffee_price > coins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources['money'] += coffee_price
        return True


# MACHINE IN ACTION
should_continue = True
while should_continue:
    user_choice = input("What would you like ? (espresso, latte, cappuccino): ")

    if user_choice in MENU:
        if check_resources(user_choice):
            print("Please insert coins.")

            inserted_quarters = int(input("How many quarters ?: "))
            inserted_dimes = int(input("How many dimes ?: "))
            inserted_nickels = int(input("How many nickles ?: "))
            inserted_pennies = int(input("How many pennies?: "))

            inserted_coins = coins_calculator(inserted_quarters, inserted_dimes, inserted_nickels, inserted_pennies)
            price = MENU[user_choice]['cost']

            # if transaction ok and resources ok => make the drink and deducted the resources
            if check_transaction(inserted_coins, price):
                required_ingredients = MENU[user_choice]["ingredients"]
                monetary = monetary_calculator(inserted_coins, price)
                print(f"Here is ${monetary} in change.")
                for ingredient in required_ingredients:
                    resources[ingredient] -= required_ingredients[ingredient]
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                print("Something goes wrong...")

    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['money']}")

    elif user_choice == 'off':
        exit()
