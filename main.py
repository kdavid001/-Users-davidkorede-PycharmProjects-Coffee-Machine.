from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order_menu = Menu()
menu_items = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
coffee_machine = CoffeeMaker()
money = MoneyMachine()


is_on = True
while is_on:
    coffee_machine.report()
    money.report()

    drink = (order_menu.get_items())
    choice = input(f'what would you like? {drink} \n')
    drink = order_menu.find_drink(choice)
    coffee_machine.is_resource_sufficient(drink=drink)
    check_money = money.make_payment(cost=drink.cost)
    if not check_money:
        print('ERROR HERE')
    coffee_machine.make_coffee(order=drink)
    is_on = input(f"do you want to turn it off? ").lower()
    if is_on == 'yes':
        print("Goodbye, enjoy your day!")
        is_on = False
    elif is_on == 'no':
        is_on = True
