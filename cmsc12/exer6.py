#Name: Francis Jandrei E. Munoz
#Section: CMSC 12 G-6L
#Description: Updated exer 6 program that imports program created from exer 7 which adds two new features: Save and Load medicine. Still uses functions, lists, and files and import

import Munoz_exer7 #Imports local file
#1 Add Meds
def AddMeds(meds): #Function for adding medicine menu
	med_id = input("Enter Medicine ID: ") #Variable for key in dictionary
	med_name = input("Enter Medicine Name: ") #Variable for medicine name
	med_desc = input("Enter Medicine Description: ") #Variable for the description
	med_quant = int(input("Enter Medicine Quantity: ")) #Variable that only takes integer values

	meds[med_id] = [med_name, med_desc, med_quant]  #Dictionary for meds info inside the meds dictionary->storage of inputs from above with med_id as the key
		
	print("Medicine added successfully")

# 2 def ViewMeds(meds):
def ViewMeds(meds, med_id): #Function for the view menu, takes the values from the dictionary above
	if med_id in meds: #Checks if the medicine id input is in the med info dictionary
		print("Medicine ID: " + med_id) #Prints the stored Medicine ID from the main dictionary
		print("Medicine Name: " + meds[med_id][0]) #Prints the stored medicine name taken from the meds info dictionary
		print("Medicine Description: " + meds[med_id][1]) #Prints the stored description taken from the meds info dictionary
		print("Medicine Quantity: " + str(meds[med_id][2])) #Prints the quantity stored taken from the meds info dictionary
	else: #If the Med ID is not stored
		print("Medicine does not exist")
 
def DeleteMeds(meds, med_id): #Function for the delete medicine menu
	if med_id in meds: #Checks if the med id given is in the main dictionary
		del meds[med_id] #Deletes the specific medicine using the medicine ID from the main dictionary
		print("Medicine deleted")
	else: 
		print("Medicine does not exist")

#4 Delete all meds
def DeleteAllMeds(meds): #Function for the delete all option
	meds.clear() #Clears the whole dictionary
	print("All medicine deleted")

#5 Restock Meds
def RestockMeds(meds, med_id): #Function for the restock option
	if med_id in meds: #Checks if the medicine is in the main dictionary
		restock_amount = int(input("Enter amount to restock: ")) #Gets the amount of medicine to be restocked
		meds[med_id][2] += restock_amount #Takes the specific medicine from the main dictionary using its ID, takes the quantity value from the info dictionary
		print("Medicine restocked successfully")
	else:
		print("Medicine does not exist")
#6 Sell Meds

def SellMeds(meds, med_id): #Function for the sell option
	if med_id in meds: #Checks if the medicine ID input is in the main dictionary
		sell_amount = int(input("Enter amount to sell: ")) #Gets amount of medicine to be sold

		if sell_amount <= int(meds[med_id][2]): #Ensures that the amount to be sold is less than or equal to the quantity inside the med info dictionary
			meds[med_id][2]-= sell_amount #Decrements the quantity taken from the med info dictionary
			print("Medicine sold successfully!")
		else:
			print("Not enough stocks in inventory")
	else:
		print("Medicine does not exist")

def main(): #Updated function that puts everything in a main function

	meds = {} #The main dictionary where the med ID is stored

	while True:	#Loops the whole program
		print()
		print("=== Medicine Inventory System===")
		print("1. Add Medicine")
		print("2. View Medicines")
		print("3. Delete Medicine")
		print("4. Delete All Medicine")
		print("5. Restock Medicine")
		print("6. Sell Medicine")
		print("7. Save Medicine")
		print("8. Load Medicine")
		print("9. Exit")
		print()
		menu = input("Enter your choice: ") #Takes an input for the options
		if menu == "1": #Enters add medicine program
			print()
			AddMeds(meds) #Runs the add meds function
		
		elif menu == "2": #Enters view medicine program
			print()
			print("Medicine Inventory")
			print("-----------------------------------------------------------------------")
			med_id = input("Enter Medicine ID to view: ") #Takes the med_id input for the view meds function
			ViewMeds(meds, med_id)
			print("-----------------------------------------------------------------------")

		elif menu == "3":
			med_id = input("Enter Medicine ID to delete: ") #Takes the med_id input for the delete meds function
			DeleteMeds(meds, med_id)

		elif menu == "4":
			DeleteAllMeds(meds) #Runs the delete all meds function

		elif menu == "5":
			med_id = input("Enter medicine ID to restock: ")
			RestockMeds(meds, med_id)

		elif menu == "6":
			med_id = input("Enter medicine ID to sell: ") #Takes med_id input for the sell med function
			SellMeds(meds, med_id)

		elif menu == "7":
			Munoz_exer7.saveMeds(meds)

		elif menu == "8":
			Munoz_exer7.loadMeds(meds)

		elif menu == "9": #End the program option
			print("Thank you!")
			break
		else: 
			print("Invalid input") #Checks if the input is only from the str(1-6)
main()

#Placed program into main function
#Changed dictionary to list
#Changed global variable "meds" to local in function main

#10-06-26
#Added the exer7 data persistence write and read functions to add new feature save and load medicines during CMSC 12 Lab session 10-09-26 
