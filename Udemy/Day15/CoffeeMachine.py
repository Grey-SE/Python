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

money = 0

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def get_user_choice():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
def turn_off_machine():
    print("Turning off the machine...")

# TODO: 3. Print report.
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# TODO: 4. Check resources if sufficient
def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

# TODO: 5. Process coins.
def check_inserted_coins(pennies, nickels, dimes, quarters):
    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    return total


# TODO: 6. Check transaction if successful
def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO: 7. Make Coffee

def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink} ☕. Enjoy!")

def coffee_machine():
    global money
    while True:
        user_choice = get_user_choice()
        if user_choice == "off":
            turn_off_machine()
            break
        elif user_choice == "report":
            print_report()
        elif user_choice in MENU:
            if check_resources(user_choice):
                print("Please insert coins.")
                pennies = int(input("How many pennies?: "))
                nickels = int(input("How many nickels?: "))
                dimes = int(input("How many dimes?: "))
                quarters = int(input("How many quarters?: "))

                total_inserted = check_inserted_coins(pennies, nickels, dimes, quarters)

                if check_transaction(total_inserted, MENU[user_choice]["cost"]):
                    make_coffee(user_choice)
                    money += MENU[user_choice]["cost"]
        else:
            print("Invalid choice. Please try again.")

coffee_machine()
