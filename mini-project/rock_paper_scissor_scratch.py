#Rock Paper Scissor From Scratch

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice  = {user_choice}, Computer Choice = {comp_choice}")
if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer Win")
    else:
        print("Paper covers Rock, You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scisor cuts Paper, You win")
    else:
        print("Rock smashes Scissor, Computer Win")
