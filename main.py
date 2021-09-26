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
        else:
            return True


if check_resources(user_choice):
    print("it's ok")
else:
    print("not enough")

# TODO 5. Process coins.

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.


