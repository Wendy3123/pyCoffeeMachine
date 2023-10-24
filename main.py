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
    "water": 1300,
    "milk": 700,
    "coffee": 300,
}

def resourceSufficient(order_ingredients):
    '''returns true when we made enough ingredients returns false if insufficient ingredients'''
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return is_enough

def process_coins():
    '''returns total calculated coins inserted'''
    print('Please insert coins.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickels?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total

def is_transaction_successful(money_received, cost_of_drink):
    '''return true if payment is accepted returns false otherwise'''
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink,2)
        print(f'Your changed is ${change}')
        global profit #use global so we can reach it from outside this fucntion
        profit+= cost_of_drink
        return True
    else:
        print('❌ Insufficent fund, refund processing!')
        return False
    
def make_coffee(drink_name,order_ingredients):
    '''deduct the required ingredients from the resources everytime a drink is made'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} 🤩')


is_on = True
profit = 0

while is_on:
    choice = input('What would you like? (espresso, latte, or cappuccino): ').lower()
    if choice == 'off':
        is_on = False
    elif choice== 'report':
        for item in resources:
            print(f'{item}: {resources[item]}')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if resourceSufficient(drink['ingredients']):        #if true, there is enough ingredients we ask user to insert coins
            payment = process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])






