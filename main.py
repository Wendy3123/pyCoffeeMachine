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

totalMoney = 0

def resourceSufficient(drink):
    for item in MENU:
        if item == drink:
            DRINKingredients= MENU[item]['ingredients'] #this returns all the  ingredients in each drink like this {'water': 250, 'milk': 100, 'coffee': 24}

print(resources)

while True:
    choice = input('What would you like? (espresso, latte, or cappuccino): ').lower()
    if choice== 'off':
        exit()
    elif choice == 'espresso':
        print('One espresso')
    elif choice == 'latte':
        print('One latte')
    elif choice == 'cappuccino':
        print('One cappuccino')
    elif choice== 'report':
        for item in resources:
            print(f'{item}: {resources[item]}')
        print(f'Money: ${totalMoney}')


resourceSufficient(choice)