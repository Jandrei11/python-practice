#Name: Francis Jandrei E. Munoz
#Section: CMSC 12 G-6L
#Description: Exercise on the use of functions in python integrated with for and while-loops statements 

print("===Magic Calculator===") #Home Page Display
print("[1] Number Game") #Home Page Display
print("[2] Arithmetic Progression") #Home Page Display
print("[3] Drawing") #Home Page Display
print("[4] Exit") #Home Page Display
print()
while True: #While loop for the whole block of program
	opt = input("Enter choice: ") #Gets value to select option
	if opt == "4": #Exit function
		break
	#NUMBER GAME
	elif opt == "1": #Executes program for Number Game
		print()
		print("==Number Game==")
		num = int(input("Enter a number: ")) #Stores value to execute below

		def odd_even(num): #Function for odd-even 
			if num % 2 == 0: #Modulo for odd-even function
				return "Even"
			else:
				return "Odd"
		def pos_neg(num): #Function for positive or negative
			if num > 0: 
				return "Positive"
			elif num < 0:
				return "Negative"
			else:
				return "Zero" 
		def squared(num): #Function to square num value
			return num ** 2
		def summation(num): #Function to sum given num
			total = 0 #Initialization; sets count at = 0
			for i in range(1, num+1): #Range from 1 to given num to add to num
 				total= total + i #Sums range from 1 to given num to add to initial num
			return total #Returns total
		print("Odd or Even:", odd_even(num)) #Prints the returned function value
		print("Positive or Negative:", pos_neg(num)) #Prints the returned function value
		print("Squared:", squared(num)) #Prints the returned function value
		print("Summation:", summation(num)) #Prints the returned function value

	#ARITHMETIC PROGRESSION
	elif opt == "2": 
		print()
		print("==Arithmetic Progression==")

		start = int(input("Start: "))
		jump = int(input("Jump: "))
		count = int(input("Count: "))

		def arithmetic_progression(start, jump, count):
			result = "" #placeholder for the result 
			for i in range(count): #Executes the program in count amount of times
				current = start + (i*jump) #arithmetic formula (n (how many times) + (i (position; increments by 1) * difference))
				result = result + "[ " + str(current) + " ]" #turns current (int value) to a string 
			print(result)
		arithmetic_progression(start, jump, count)
	
	#DRAWING
	elif opt == "3":
		print()
		print("==Drawing==")	
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
 
		size = int(input("Size: "))
		character = input("Character: ")

		drawing(size, character)
	else:
		print("You have entered an invalid input")		

	print()
	print("===========================")
	print("===Magic Calculator===")
	print("[1] Number Game")
	print("[2] Arithmetic Progression")
	print("[3] Drawing")
	print("[4] Exit")
	print()
