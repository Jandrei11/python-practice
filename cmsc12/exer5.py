#Name: Muñoz, Francis Jandrei E.
#Section: CMSC 12 G-6L
#Description: A program that gives the user the option to choose various encrypting methods such as Bacon and A1Z26. Both methods gives the user the option whether they want to encode or decode a message. 

def encode_using_bacon(code): #Function value with one parameter in encoding using bacon encryption
	ciphered_text = "" #Placeholder for the ciphered text value

	for letters in code: #Loops the program for encoding strings to convert to bacon
		if letters  == " ": #Checks the spaces of the input 
			ciphered_text = ciphered_text + " " #Adds a space
		else:
			number = ord(letters.upper()) - ord("A") #Turns input to number- "ord" to make it number and ".upper" to make everything uppercase
			binary = "" #Accumulator for the converted input to binary

			for x in range (5): #Loops 
				if number % 2 == 0: #Check if number is even
					binary = "A" + binary #Adds A to the binary if number is even 
				else: #Checks if number is odd
					binary = "B" + binary #Adds B to the binary if number is odd

				number = number // 2
			ciphered_text = ciphered_text + binary #Combines everything

	return ciphered_text #Returns function

def decode_using_bacon(code): #Function value with one parameter in decoding a bacon encryption
	deciphered_text = "" #Placeholder for the ciphered text value

	words = "" #Placeholder/accumulator for words 

	for letter in code: #Loops code deciphering   
		if letter == " ": #Checks for spaces
			for x in range(0, len(words), 5): #Loops through word
				block = words[x:x+5] #Splices word in 5

				number = 0 #Counter starting at 0

				for character in block: #Loops to go through character
					number = number * 2 #Multiplies counter to 2

					if character == "B": 
						number = number + 1 #Adds 1 if the character is a B 

				deciphered_text = deciphered_text + chr(number + ord("A")) #Converts the input to letter and adds it to decoded message
			words = ""

		else: 
			words = words + letter 
	for x in range(0, len(words), 5): 
		block = words[x:x+5]

		number = 0

		for character in block:
			number = number * 2

			if character == "B":
				number = number + 1
		deciphered_text	= deciphered_text + chr(number + ord("A"))
	return deciphered_text 

def encode_using_a1z26(code): #Function value for encoding A1Z26
	ciphered_text = "" #Placeholder/Accumulator for the ciphered text
 
	for letters in code: 
		if letters == " ": #Checks if there are spaces spaces
			ciphered_text	= ciphered_text[:-1]	+ " " #Adds the spaces
		else:
			number = ord(letters.upper()) - ord("A") + 1 #Converts string to number
			ciphered_text = ciphered_text + str(number) + "-" #Continues to add accumulated ciphered text + converted string to number
	ciphered_text = ciphered_text[:-1] 

	return ciphered_text	

def decode_using_a1z26(code): #Function value for decoding A1Z26
	deciphered_text = "" #Also accumulator
	number	= "" #Accumulator of current number

	for letters in code:
		if letters == "-": #Checks if last letter have - 
			deciphered_text	= deciphered_text + chr(int(number) + ord("A") - 1) #Converts letter to number
			number = "" #Stores digit of current number

		elif letters == " ": #Checks for spaces
			deciphered_text	= deciphered_text + chr(int(number) + ord("A")-1)  #Converts letter to number
			deciphered_text	= deciphered_text + " " #Adds spaces
			number = "" 
		else:
			number = number + letters 
	deciphered_text	= deciphered_text + chr(int(number) + ord("A") - 1)

	return deciphered_text

def show_history(history): #Function value to show history
	number = 0 #Counter for numbering
	print("Recent list of encoded and decoded words:")
	for stuffs in history:
		print(number, ":", stuffs) #Prints the current number and the stored data
		number = number + 1 #Increments numbering by 1

def main(): #Main function
	queue = [] #Becomes local variable that stores the history for the program below

	while True: #Loops the whole program
		print("Cipher Repository") #Prints the options
		print(" ", "(1) Encode using Bacon")
		print(" ", "(2) Encode using AIZ26")
		print(" ", "(3) Decode using Bacon")
		print(" ", "(4) Decode using AIZ26")
		print(" ", "(5) Show encoding and decoding history")
		print(" ", "(0) Exit")

		option = input("Enter choice: ") #Makes the user choose what program to do + used strings to still loop
		print() #Adds space hehe
		if option == "0": 
			break
	
		elif option == "1":
			string = input("Enter the string you wish to encode: ")

			ciphered_text = encode_using_bacon(string) #Returns the function 
 
			print("Encoded string: ", ciphered_text) #Prints the returned value
			queue.append(ciphered_text) #Stores the returned value to the queue variable
		elif option == "2":
			string = input("Enter the string you wish to encode: ")

			ciphered_text = encode_using_a1z26(string) #Returns the function 

			print("Encoded string: ", ciphered_text)#Prints the returned value
			queue.append(ciphered_text) #Stores the returned value to the queue variable

		elif option == "3":
			string = input("Enter the string you wish to decode: ")

			deciphered_text = decode_using_bacon(string) #Returns the function 

			print("Decoded string: ", deciphered_text)#Prints the returned value
			queue.append(deciphered_text)#Stores the returned value to the queue variable
		elif option == "4":
			string = input("Enter the string you wish to decode: ")

			deciphered_text	= decode_using_a1z26(string) #Returns the function 

			print("Decoded string: ", deciphered_text) #Prints the returned value
			queue.append(deciphered_text) #Stores the returned value to the queue variable
		elif option == "5":
			show_history(queue) #Returns the function 
		else:
			print("You have entered an invalid input") 
main()
