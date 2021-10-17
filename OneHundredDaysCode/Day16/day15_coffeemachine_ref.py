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
    "money": 0.0
}

units = {"water": "ml", "milk": "ml", "coffee": "g", "money": "$"}

def report():
    result = '\n\nCurrent Resources:\n\n'
    for key in resources.keys():       
        if key == "money":
            result += f"{key.title()} : {units[key]}{resources[key]}\n"
        else:
            result += f"{key.title()} : {resources[key]}{units[key]}\n"
    return result

def checkresources(selection):
    request = MENU[selection]["ingredients"]

    missing_ingredients = ''

    for ingredient in request.keys():
        available = resources[ingredient]
        requested = request[ingredient]

        if available < requested:
            missing_ingredients += f"Sorry there is not enough {ingredient} to make a {selection.title()}.\n\n"

        #print(f"{available}{units[ingredient]} {ingredient} available.")
        #print(f"{requested}{units[ingredient]} {ingredient} requested.")
    return missing_ingredients

def processpayment():
    coins = [
        {'coin': "Quarter", "qty": 0, "value": 25},
        {'coin': "Dime", "qty": 0, "value": 10},
        {'coin': "Nickel", "qty": 0, "value": 5},
        {'coin': "Penny", "qty": 0, "value": 1}
    ]
    print ("Please insert coins now. >>\n")

    while True:
        try:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            break
        except ValueError:
            print("All quantities entered must be numeric (integers).")


    coins[0]["qty"] = quarters
    coins[1]["qty"]  = dimes
    coins[2]["qty"]  = nickels
    coins[3]["qty"]  = pennies

    total = sum(list(map(lambda x: x["qty"] * x["value"], coins)))/100

    return total

def makebeverage(selection):
    cashinserted = processpayment()

    if MENU[selection]["cost"] > cashinserted:
        print("Sorry, that's not enough money. Money refunded.")
    elif MENU[selection]["cost"] < cashinserted:
        change = cashinserted - MENU[selection]["cost"]
        change = "{0:.2f}".format(change)
        print(f"\n\nThank you. Beverage cost: {MENU[selection]['cost']}. Money inserted {cashinserted}. Dispensing Change ({change})...")
    else:
        print("Thank You")

    print("Making Beverage")

    resources["money"] += MENU[selection]["cost"]

    for ingredient in MENU[selection]["ingredients"].keys():
        resources[ingredient] -= MENU[selection]["ingredients"][ingredient]
    
    print(f"Here is your {selection.title()}. Enjoy!\n\n")






while True:
    bevchoice = input("What would  you like? (espresso/latte/cappucccino):\n>> ").strip()

    
    

    if bevchoice.lower() == "off":
        print("Powering down shzzzzzzzm...")
        break
    
    elif bevchoice.lower() == "report":
        print(report())

    else:
        if not MENU.get(bevchoice): 
            print(f"{bevchoice.title()} is not a valid choice. Please try again.\n\n")
            continue

        insufficient_resources = checkresources(bevchoice)

        if insufficient_resources:
            print(insufficient_resources)
        else:
            makebeverage(bevchoice)








