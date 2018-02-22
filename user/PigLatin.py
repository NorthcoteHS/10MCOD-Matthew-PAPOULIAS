# Create list of all vowels
vowels = ["a", "e", "i", "o", "u"]

# Encode method
def encode(word):
	# Split users text into a list of all words
	word = word.split()
	# Get the amount of words
	wordcount = len(word)
	# If there is only one word
	if wordcount == 1:
		loop = 0
		# Get the word and put into a variable called latin
		latin = word[0]
		# Split the word into letters
		latin = list(latin)
		# Get the amount of letters
		letters = len(latin)
		# If there is more than one letter
		if letters != 1:
			# Loop through the letters
			while loop < letters:
				# Check if they are vowels
				if latin[loop] in vowels:
					# If its a vowel break out of the loop
					break
				# Otherwise
				else:
					# Add the letter to the end
					latin.append(latin[loop])
					# Delete its original position
					del latin[loop]
					# Fix the loop variable to work with the lost letter
					loop = loop - 1
				loop = loop + 1
			# Add ay to the end
			latin.append("a")
			latin.append("y")
			# Join the letters back up
			encoded = "".join(latin)
			# Print the encoded
			print(encoded)
	# Otherwise
	else:
		loopWords = 0
		loop = 0
		encoded = []
		# While the amount of loop amount is smaller than the words
		while loopWords < wordcount:
			# Set latin to the first word in the string
			latin = word[loopWords]
			# Split the word into letters
			latin = list(latin)
			# Get the amount of letters
			letters = len(latin)
			# While the loop is smaller than the amount of letters
			while loop < letters:
				# If its a vowel exit the loop
				if latin[loop] in vowels:	
					break
				# Otherwise
				else:
					# Add the letter to the end
					latin.append(latin[loop])
					# Delete its original position
					del latin[loop]
					# Fix the loop variable to work with the lost letter
					loop = loop - 1
				loop = loop + 1
			loopWords = loopWords + 1
			# Add ay to the end
			latin.append("a")
			latin.append("y")
			# Join the letters up	
			encoded.append("".join(latin))
		# Join and print the string up
		print("\n" + " ".join(encoded))

# Get the text
cleartext = input("Enter text: ")

# Encode it
encode(cleartext)