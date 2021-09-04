days_in_year = 365
weeks_in_year = 52
months_in_year = 12
max_years = 90

current_age = input("How old are you today?\n>> ")

years_left = max_years - int(current_age)

print (f"{years_left} years left.")

months_left = years_left * months_in_year
weeks_left = years_left * weeks_in_year
days_left = years_left * days_in_year

print(f"Assuming you are lucky enough to make it to 90 years old... You have {months_left} months left, or {weeks_left} weeks, or {days_left} days.")

