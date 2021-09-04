import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = {0: {"name":"Rock", "illustration":rock}, 1: {"name":"Paper", "illustration":paper}, 2:{"name":"Scissors", "illustration":scissors}}

def makechoice(key, player="p1"):
    label = choices[key]["name"]
    picture = choices[key]["illustration"]
    if player =="p1":
        return f"You chose {label}\n\n {picture}"
    return f"The Computer chooses... {label}\n\n {picture}"

def checkInt(prompt):
    try:
        int(prompt)
        return True
    except ValueError:
        return False

def playerwins(player, cpu):
    '''
    Rock Beats Scissors
    Scissors Beats Paper
    Paper Beats Rock
    '''
    
    choice = ["rock", "paper", "scissors"]

    if choice[player] == choice[cpu]:
        return "tie"
    
    if choice[player] == "rock":
        if choice[cpu]  == "scissors":
            return "player"

    elif choice[player] == "paper":
        if choice[cpu]  == "rock":
            return "player"
    else: 
        if choice[cpu]  == "paper":
            return "player"
    return "cpu"

running = True

while running: 
    prompt = input("Ready to Roshambo! Which do you choose?\n1. Rock\n2. Paper\n3.Scissors\n\nType \"Quit \" to stop.\n\n>> ")

    if prompt.lower() == "quit":
        break

    if(checkInt(prompt)):
        prompt = int(prompt) - 1
        if prompt >= 0 and prompt < 3:
            print(makechoice(prompt))
            print("=============================================================\n\n")
            cpu_choice = random.randint(0,2)
            print(makechoice(cpu_choice,player="cpu"))
            print("=========================Results=============================\n\n")
            results = playerwins(prompt, cpu_choice) 
            if results == "player":
                print(f"{choices[prompt]['name']} beats {choices[cpu_choice]['name']} . Player Wins!\n\n\n\n")
            elif results == "cpu":
                print(f"Sorry, {choices[cpu_choice]['name']} beats {choices[prompt]['name']} . Computer Wins. Try again.\n\n\n\n")
            else:
                print(f"Jinx, you both chose {choices[prompt]['name']} . It's a tie! Try again.\n\n\n\n")

        else:
            print("Choice must be between 1 and 3. You chose {prompt}\n")
    else:
        print(f"Choice must be a number beteween 1 and 3. You chose {prompt}\n")

    












