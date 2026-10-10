#Name: Francis Jandrei E. Munoz
#Section: G-6L
#Description: A program that utilizes files and import to be added to exer 6. Uses functions and data persistence in python

#Save Meds function
def saveMeds(meds): #Function for saving medicine inputs in the main program
	save_from_file_handle = open("medicine.dat", "w") #Opens a new file, medicine.dat, and saves what is written in the meds dictionary
	for med_id in meds: #Loop to go through every input
		name = meds[med_id][0] #Sets name and access index 0 in meds dictionary
		desc = meds[med_id][1] #Sets desc and acess index 1 in meds dictionary
		quant = str(meds[med_id][2]) #Sets quant and access index 2 in meds dictionary
		save_from_file_handle.write(med_id + "," + name + "," + desc + "," + str(quant) + "\n") #Writes variables taken from meds dictionary to medicine.dat file
	save_from_file_handle.close() #Closes the medicine.dat file after looping through all inputs in meds dictionary
	print("Medicine saved!") 

#Load Meds function
def loadMeds(meds): #Function for loading medicine inputs in the main program
	view_from_file_handle = open("medicine.dat", "r") #Sets view_handle that opens medicine.dat file and reads the content
	for line in view_from_file_handle: #Loops through every line in view_handle 
		val = line.split(",") #Sets val as line that is split using ,
		meds[val[0]] = [val[1], val[2], int(val[3])] #Gets index per line that is split by ,
		print("Medicine loaded!")
	return meds #Returns the whole function
    	  
