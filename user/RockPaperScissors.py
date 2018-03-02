import random
import sys

def again():
	again = input("Play again (y/n): ")
	if again == "y":
		return True
	else:
		return False

def game():
	print("Choices: ")
	print("1) Rock")
	print("2) Paper")
	print("3) Scissors")
	user_choice = input("Choice: ")
	com_choiceNum = random.randint(1, 3)
	com_choice = ""

	if com_choiceNum == 1:
		com_choice = "rock"
	elif com_choiceNum == 2:
		com_choice == "paper"
	elif com_choiceNum == 3:
		com_choice == "scissors"
	else:
		print("An error occured.")
		sys.exit()

	if com_choice.lower() == user_choice.lower():
		print("The computer chose {}").format(com_choice)
		print("Tie")
		if again():
			game()
		else:
			sys.exit()

	if com_choice.lower() == "rock" and user_choice.lower() != "paper":
		print("The computer chose " + com_choice)
		print("You lost")
		if again():
			game()
		else:
			sys.exit()
	elif com_choice.lower() == "rock" and user_choice.lower() == "paper":
		print("The computer chose " + com_choice)
		print("You won")
		if again():
			game()
		else:
			sys.exit()
	else:
		print("The computer chose " + com_choice)
		print("You lost")
		if again():
			game()
		else:
			sys.exit()

	if com_choice.lower() == "paper" and user_choice.lower() != "scissors":
		print("The computer chose " + com_choice)
		print("You lost")
		if again():
			game()
		else:
			sys.exit()
	elif com_choice.lower() == "paper" and user_choice.lower() == "scissors":
		print("The computer chose " + com_choice)
		print("You won")
		if again():
			game()
		else:
			sys.exit()
	else:
		print("The computer chose " + com_choice)
		print("You lost")
		if again():
			game()
		else:
			sys.exit()

	if com_choice.lower() == "scissors" and user_choice.lower() != "rock":
		print("The computer chose " + com_choice)
		print("You lost")
		if again():
			game()
		else:
			sys.exit()
	elif com_choice.lower() == "scissors" and user_choice.lower() == "rock":
		print("The computer chose " + com_choice)
		print("You won")
		if again():
			game()
		else:
			sys.exit()
	else:
		print("The computer chose " + com_choice)
		print("You lost")
		if again():
			game()
		else:
			sys.exit()

game()