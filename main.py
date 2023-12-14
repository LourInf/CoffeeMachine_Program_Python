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

# 3b. create var to hold report:
profit = 0

# 4b.function to check if sufficient ingredients to make the drink
# Returns True when order can be made, False if lack of ingredient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients [item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# 5b. function to calculate the total from coins inserted:
# Returns the total
def process_coins():
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# 6b. function to check if the transaction is successful:
# Returns True when payment accepted, False if not enough money
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the change: {change} $")
        global profit # profit is outside this local scope, so we need to add global to reach it.
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

#7b. function to make the coffee
# it will deduct the required ingredients from the resources
def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here's your {drink_name} ☕ ")


# 1. Prompt user when the machine is on:
is_on = True

while is_on:
    choice = input("What would you like? Espresso/Latte/Cappuccino \n").lower()
    # 2. If "Off", exit the loop
    if choice == "Off":
        is_on = False
    # 3a. If "report", generate resources available
    elif choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"money: {profit} $")
        is_on = False
    # 4a. a maintainer would choose off or report, otherwise (else) is a client and will choose a drink from the choice input
    # check if there are enough ingredients to make the drink
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            # 5a. we need to calculate the total user has to pay
            payment = process_coins()
            # 6a. we need to check if there are enough coins to pay
            if is_transaction_successful(payment, drink["cost"]):
                # 7a. make coffee
                make_coffee(choice, drink["ingredients"])