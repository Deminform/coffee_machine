from menu import MENU
from menu import resources


# Print report
def print_report():
    for key, value in resources.items():
        ends = 'g' if key == 'coffee' else 'ml'
        print(f'{key}: {value}{ends}')


# Check resources sufficient
def check_resources(request: str) -> bool:
    for key, value in MENU[request]['ingredients'].items():
        if key in resources:
            if resources[key] < value:
                print(f'Sorry there is not enough {key}')
                return False
            else:
                return True


# Scoring a coin
def calc_coins() -> int:
    amount = 0
    coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
    for key, value in coins.items():
        count = int(input(f'How many {key}: '))
        amount += value * count
    return round(amount, 2)


# Check transaction successful
def check_transaction(request: str):
    if check_resources(request):
        amount = calc_coins()
        if refund_check(request, amount):
            price = MENU[request]['cost']
            if 'money' not in resources:
                resources['money'] = price
            else:
                resources['money'] += price
            make_coffee(request)


# Refund
def refund_check(request: str, amount: int):
    price = MENU[request]['cost']
    if amount > price:
        change = amount - price
        print(f'Here is ${round(change, 2)} in change')
        return True
    elif amount == price:
        return True
    elif amount < price:
        print(f'Sorry that`s not enough money. Money refunded ${round(amount, 2)}.')
        return False


# 6 Making coffee
def make_coffee(request):
    for key, value in MENU[request]['ingredients'].items():
        if key in resources:
            resources[key] -= value
    print(f'Here is your {request} Enjoy!')


while True:
    choice = input('What would you like? (espresso / latte / cappuccino): ')

    if choice == 'report':
        print_report()
    elif choice == 'off':
        break
    else:
        check_transaction(choice)





