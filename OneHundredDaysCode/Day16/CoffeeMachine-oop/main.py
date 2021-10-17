from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_maker = MoneyMachine()


while True:
    bevchoice = input(f"What would  you like? ({coffee_menu.get_items()})" +
                        ":\n>> ").strip()
       
    if bevchoice.lower() == "off":
        print("Powering down shzzzzzzzm...")
        break
    
    elif bevchoice.lower() == "report":
        coffee_machine.report()
        money_maker.report()

    else:
        beverage = coffee_menu.find_drink(bevchoice)
        if not beverage:
            print(f"{bevchoice.title()} is not a valid choice. Please try again.\n\n")
            continue
       
        sufficient_resources = coffee_machine.is_resource_sufficient(beverage)
        
        if sufficient_resources and money_maker.make_payment(beverage.cost):
                coffee_machine.make_coffee(beverage)
        

