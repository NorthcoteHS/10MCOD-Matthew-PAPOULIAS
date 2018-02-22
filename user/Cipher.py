# Get the text
cleartext = input("Enter text: ")
# Get the amount to shift by
shift = int(input("Enter shift: "))
# Split the string into a list
cleartextList = cleartext.split()
# Create a list for the cipher
cipher = []

# Loop through each word in the list
for word in range(len(cleartextList)):
	# Split the word into letters
	cleartextLetters = list(cleartextList[word])
	# Loop through each letter
	for letter in cleartextLetters:
		# Turn the letter into ascii
		asciiNum = ord(letter)
		# Add the shift to the ascii code
		asciiNum = asciiNum + shift
		# Turn the ascii back into a letter
		cipherLetter = chr(asciiNum)
		# Add the letter to the list
		cipher.append(cipherLetter)
	# Add a space for the next word
	cipher.append(" ")

# Print the cipher
print("\n" + "Cipher: " + "".join(cipher))