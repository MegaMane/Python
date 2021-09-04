def tipCalculator(total, tip_percentage, patrons):
    total_including_tip = total * (1 + (tip_percentage/100))
    cost_per_person = round((total_including_tip / patrons),2)
    cost_per_person = "{:.2f}".format(cost_per_person)
    return f"Each person should pay: ${cost_per_person}"

print("Welcome to the tip calculator.\n")
total = float(input("What was the total bill? ").strip("$"))
tip_percentage = int(input("What percentage tip would you like to give? 10,12, or 15? "))
patrons = int(input("How many people split the bill? "))

print(tipCalculator(total, tip_percentage, patrons))
