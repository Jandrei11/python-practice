#Francis Jandrei E. Munoz
#CMSC 12 G-6L
while True:
	def odd_even (num): #Sets num as a function of odd_even
		if num % 2 == 0: #If-else statement to determine if odd or even
			return "Even" 
		else:
			return "Odd" 

	def pos_neg(num): #Sets num as a function of pos_neg
		if num > 0: #If-else statement; if n > 0 then positive
			return "Positive" 
		elif num < 0: 
			return "Negative"
		else:
			return "Zero"

	def squared(num): #Sets num as a squared function
		return num ** 2 #squares the num then returns it to function

	def summation(num):
		total = 0 #Initialization; sets total = 0

		for i in range(1, abs(num)+1): #Range of for-loop, starts at 1 ends at given int +1 
			
			total = total+i #summation of 1 to Nth value
			
		return total #return variable to function

	def arithmetic_progression(start, jump, count):
		print()
		print("==Arithmetic Progression==")
		result = "" #placeholder for the result 

		for i in range(count): #Executes the program in count amount of times
			current = start + (i*jump) #arithmetic formula (n (how many times) + (i (position; increments by 1) * difference))
			result = result + "[ " + str(current) + " ]" #turns current (int value) to a string 
					
		print(result)
		print()

	def drawing(size, character):
		print("[ 1 ] Square ")
		print("[ 2 ] Pyramid ")

		choice = int(input("Enter choice: "))
				
		if choice == 1:
			for x in range(size): #repeats the code size times
				for y in range(size): #repeats code size times each ROW
					print(character, end="") #prints character, size times, in the same line
				print() #prints next character, size times, to the next line

		if choice == 2:
			for x in range(size):  #repeats the code size times, one time for each ROW
				spaces = size - x - 1 #calculates how many spaces before the characters
				characters = 2 * x + 1 #calculates how many characters for the current row
				print(" " * spaces + character * characters) #prints the spaces and characters togetherto form the pyramid	
#Loops whole program as a whole while conditions (such as int) are satisfied
	print("===Magic Calculator===")
	print()
	print("[1] Number Game")
	print("[2] Arithmetic Progression")
	print("[3] Drawing")
	print("[4] Exit")
	print() #Adds space between input
	option = int(input("Enter your choice: ")) #Gets value for if-else conditions below
	if option == 4: #Exits the program; makes use of loop break function
		break
	elif option == 1: #Enters number game program
		print()
		print("==Number Game==")
		num = int(input("Enter a number: ")) #num is a variable to get num for functions below

		print("Odd or Even:", odd_even(num))
		print("Positive or Negative:", pos_neg(num))
		print("Squared: ", squared(num))
		print("Summation", summation(num))

	elif option == 2:
		start = int(input("Start: "))
		jump = int(input("Jump: "))
		count = int(input("Count: "))	
		arithmetic_progression(start, jump, count)
	if option == 3:
		size = int(input("Size: "))
		character = input("Character: ")
		drawing(size, character)

#CHANGES: 
#(10-10-26) Moved the functions above instead of inside conditions to ensure reusability and improve readability

