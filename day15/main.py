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
            "coffee": 24,
            "milk": 150,
            },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
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


def is_resource_sufficicient(order_ingrediant):
    """returns true when order can be made. false if ingredients are done"""
    for item in order_ingrediant:
        if order_ingrediant[item] >= resources[item]:
            print(f"sorry there is not enough {item} ")
            return False
    return True


def process_coins():
    """returns the total calculated from coins inserted"""
    print("please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dims?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return true when the payment is accepted, or false if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from the resource."""
    for item in order_ingredients:
        resources[item]  -= order_ingredients[item]
    print(f"here is your {drink_name}")

is_on = True


while is_on:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    if choose == "off":
        is_on = False
    elif choose == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: ${profit}")
    else:
        drink = MENU[choose]
        if is_resource_sufficicient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choose, drink["ingredients"])

