import random 

usr_choice = input("what is your choice [rock, paper, or scissor]: ")
possible_choices = ["rock", "paper", "scissor"]
comp_choice = random.choice(possible_choices)
print(f" You chose {usr_choice}, and the computer chose {comp_choice}")
if usr_choice == comp_choice:
	print("ITS A TIE!")
elif usr_choice == "rock" and comp_choice == "scissor":
	print("YOU WON!!!")
elif usr_choice == "scissor" and comp_choice == "paper":
	print("YOU WON!!!")
elif usr_choice == "paper" and comp_choice == "rock":
	print("YOU WON!!!")
else:
	print("WOMP WOMP YOU LOST!!!! :(")
