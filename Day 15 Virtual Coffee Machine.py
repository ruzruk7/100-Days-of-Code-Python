import os
MENU = {
    "espresso": {"ingredients": {"water": 50,"coffee": 18,},"cost": 1.5,},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24,}, "cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24,}, "cost": 3.0,}
    }

RESOURCES = {'water': 300, 'milk': 300, 'coffee': 100, 'money': 0}
power_on = True

def money_processor(quarter, dime, nickel, penny):
    '''Take in coins and returns dollar amount'''
    penny *= 0.01
    nickel *= 0.05
    dime *= 0.10
    quarter *= 0.25
    total = (penny + nickel + dime + quarter)
    return total


while  power_on:
    task = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if task == 'off':
        break
    if task == 'report':
        for k, v in RESOURCES.items():
            if k == 'water' or k == 'milk':
                print(f'{k}: {v}ml')
            elif k == 'coffee':
                print(f'{k}: {v}g')
            elif k == 'money':
                print(f'{k}: ${v}')
        continue
    quarters = int(input("How many Quarters?: "))
    dimes = int(input("How many Dimes?: "))
    nickels = int(input("How many Nickels?: "))
    pennies = int(input("How many Pennies?: "))
    money_given = money_processor(quarters, dimes, nickels, pennies)
    total = (money_given - MENU[f"{task}"]["cost"])
    if total >= 0:
        print(f"Here is ${total:.2f} in change")
        if task == 'espresso':
            cooked = False
            for k in MENU[f'{task}']['ingredients']:
                ingred_used = RESOURCES[k] - MENU[f'{task}']['ingredients'][k]
                if ingred_used < 0:
                    print(f'Sorry there is not enough {k}.')
                    break
                else:
                    cooked = True
                    RESOURCES[k] -= MENU[f'{task}']['ingredients'][k]
            if cooked:
                print("Here is your espresso ☕. Enjoy!")
                continue
        if task == 'latte':
            cooked = False
            for k in MENU[f'{task}']['ingredients']:
                ingred_used = RESOURCES[k] - MENU[f'{task}']['ingredients'][k]
                if ingred_used < 0:
                    print(f'Sorry there is not enough {k}.')
                    break
                else:
                    cooked = True
                    RESOURCES[k] -= MENU[f'{task}']['ingredients'][k]
            if cooked:
                print("Here is your latte ☕. Enjoy!")
                continue
        if task == 'cappuccino':
            cooked = False
            for k in MENU[f'{task}']['ingredients']:

                ingred_used = RESOURCES[k] - MENU[f'{task}']['ingredients'][k]
                if ingred_used < 0:
                    print(f'Sorry there is not enough {k}.')
                    break
                else:
                    cooked = True
                    RESOURCES[k] -= MENU[f'{task}']['ingredients'][k]
            if cooked:
                print("Here is your cappuccino ☕. Enjoy!")
                continue

    else:
        print("Sorry that is not enough money. Money refunded.")
        continue
        
