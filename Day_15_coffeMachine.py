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
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    for item, quantity in resources.items():
        print(f"{item}: {quantity}")


def check_resources(chosen_item, resources):
    ingredients_needed = MENU[chosen_item]["ingredients"]
    for ingredient, quantity in ingredients_needed.items():
        if resources[ingredient] < quantity:
            print(f"Sorry, there is not enough {ingredient}. {chosen_item} cannot be made")
            return False
    return True
    # ingredients_needed = MENU[chosen_item]["ingredients"] <------------------- OLD CODE, REFACTORED FOR UNITTEST
    # for ingredient, quantity in ingredients_needed.items():
    #     if resources[ingredient] < quantity:
    #         print(f"Sorry, there is not enough {ingredient}. {chosen_item} cannot be made")
    #         return False
    #
    # return True



def processing_coins(item_cost, total_inserted):
    # print("Please insert coins")                            <------------------- OLD CODE, REFACTORED FOR UNITTEST
    # quarter = 0.25 * int(input("how many quarters?: "))
    # dimes = 0.1 * int(input("how many dimes?: "))
    # nickels = 0.05 * int(input("how many nickels?: "))
    # pennies = 0.01 * int(input("how many pennies?: "))
    # total_inserted = quarter + dimes + nickels + pennies
    # if total_inserted >= item_cost:
    #     change = total_inserted - item_cost         #round(,2)
    #     if change > 0:
    #         print(f"Here is your change: ${change:.2f}")
    #     return True
    # else:
    #     print("Sorry, not enough money. Coins refunded.")
    #     return False
    if total_inserted >= item_cost:
        change = total_inserted - item_cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        return True
    else:
        print("Sorry, not enough money. Coins refunded.")
        return False

def make_coffee(chosen_item, resources):
    item_cost = MENU[chosen_item]["cost"]
    for ingredient, quantity in MENU[chosen_item]["ingredients"].items():
        resources[ingredient] -= quantity

# machine_running = True                         <------------------- OLD CODE, REFACTORED FOR UNITTEST
# while machine_running:
#     chosen_item = input("What would you like? (espresso/latte/cappuccino): ")
#     if chosen_item == 'report':
#         report()
#     elif chosen_item in MENU:
#         if check_resources(chosen_item):
#             item_cost = MENU[chosen_item]["cost"]
#             if processing_coins(item_cost):
#                 print(f"Making your {chosen_item}...")
#                 for ingredient, quantity in MENU[chosen_item]["ingredients"].items():
#                     resources[ingredient] -= quantity
#                 print(f"Enjoy your {chosen_item}!")
#     elif chosen_item == 'off':
#         print("Machine powered off.")
#         machine_running = False
#     else:
#         print("Invalid input.")
def main():
    machine_running = True
    while machine_running:
        chosen_item = input("What would you like? (espresso/latte/cappuccino): ")
        if chosen_item == 'report':
            report()
        elif chosen_item in MENU:
            if check_resources(chosen_item):
                item_cost = MENU[chosen_item]["cost"]
                total_inserted = float(input("Insert coins: "))
                if processing_coins(item_cost, total_inserted):
                    print(f"Making your {chosen_item}...")
                    make_coffee(chosen_item, resources)
                    print(f"Enjoy your {chosen_item}!")
        elif chosen_item == 'off':
            print("Machine powered off.")
            machine_running = False
        else:
            print("Invalid input.")

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
