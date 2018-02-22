import random
import sys

# Put all possible answers in list
answers = ["It is certain", "It is certain", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

# Def again method
def again():
	again = input("Ask another question (y/n): ")
	if again == "y" or again == "Y":
		# Returns true if the the user want to ask another question
		return True
	else:
		return False

# Define main methods
def main():
	# Get the users question
	question = input("Question: ")
	# Get a random number between 1 and 20
	ranNum = random.randint(1, 20)
	# Get the answer by using the random number
	answer = answers[ranNum]
	# Print the answer
	print("\n" + answer + "\n")
	# See if user wants to ask another question
	if not again():
		sys.exit(0)
	else:
		main()

# Call Main method
main()