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
}

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# TODO 1. Prompt user by asking "what would you like ? (espresso, latte, cappuccino): "
user_choice = input("What would you like ? (espresso, latte, cappuccino): ")

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
if user_choice == "off":
    exit()
# TODO 3. Print report
if user_choice == "report":
    print(resources)


# TODO 4. Check resources sufficient?


def check_resources(drink):
    required_ingredient = MENU[drink]["ingredients"]
    for ingredient in required_ingredient:
        if resources[ingredient] < required_ingredient[ingredient]:
            return False
    return True


if check_resources(user_choice):
    print("Please insert coins.")
else:
    print("not enough")

# TODO 5. Process coins.
# if resources ok, program input user to insert coins
# quarter = $0.25  dime = $0.1  nickle = $0.05  penny = $0.01
inserted_quarters = int(input("How many quarters ?: "))
inserted_dimes = int(input("How many dimes ?: "))
inserted_nickels = int(input("How many nickles ?: "))
inserted_pennies = int(input("How many pennies?: "))


# calculate the monetary value of coins inserted
def coins_calculator(quarters, dimes, nickels, pennies):
    """take the numbers of coins, return the sum in dollars"""
    quarters *= QUARTER
    dimes *= DIME
    nickels *= NICKEL
    pennies *= PENNY
    return quarters + dimes + nickels + pennies


inserted_coins = coins_calculator(inserted_quarters, inserted_dimes, inserted_nickels, inserted_pennies)
price = MENU[user_choice]['cost']


def monetary_calculator(coins, coffee_price):
    """take coins and coffee_price, return rounded difference between"""
    diff = coins - coffee_price
    return round(diff, 2)


monetary = monetary_calculator(inserted_coins, price)
print(f"Here is ${monetary} in change.")

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.
