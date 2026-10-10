#UPDATES:
#I have integrated exercise 1 & 2 together so that the new program can run both under one program. I also made it utilize functions and loops the whole thing even if the user inputs something that is not in the menu option. 
#Python elements used: Variables, Data Types (int, float, strings) and Casting, Operations, Conditions, Iterations, 
def main():
	while True:

		def coffee(caff_intake, consumed, sleep):
			intake1 = caff_intake * (0.5 ** (1/5)) 
			intake2 = caff_intake * (0.5 ** (3/5))
			intake3 = caff_intake * (0.5 ** (5/5))
			intake4 = caff_intake * (0.5 ** (8/5))
			intake5 = caff_intake * (0.5 ** (12/5))

			print()
			print("After", 1, "hour:", f'{intake1:.2f}',"mg remaining")
			print("After", 3, "hour:", f'{intake2:.2f}',"mg remaining")
			print("After", 5, "hour:", f'{intake3:.2f}',"mg remaining")
			print("After", 8, "hour:", f'{intake4:.2f}',"mg remaining")
			print("After", 12, "hour:", f'{intake5:.2f}',"mg remaining")
			print()
			
			caffeine_left = caff_intake * 0.5 ** ((sleep-consumed)/5)
			
			print("By your bedtime,", sleep, "you will still have", caffeine_left, "mg of caffeine in your system")
			
			print()

		def sleep(name, sleep_hours):
			sleep_status = "tbd"

			if (sleep_hours) < 7:
				sleep_status = "Sleep Deprived"
			elif (sleep_hours) >= 7 and sleep_hours <= 9:
				sleep_status = "Healthy Sleep"
			elif (sleep_hours > 9):
				sleep_status = "Oversleeping" 

			sleepQ_score = (sleep_hours / 8) * 100

		#Checks condition for values from sleepQ_score
			sleepQ_value = "tbd" 
			if (sleepQ_score < 75):
				sleepQ_value = "Poor"
			elif (sleepQ_score >= 75 and sleepQ_score <= 89.99):
				sleepQ_value = "Fair"
			elif (sleepQ_score >= 90 and sleepQ_score <= 109.99):
				sleepQ_value = "Good"
			elif (sleepQ_score >= 110):
				sleepQ_value = "Excellent"	

			print()
			print("-----RESULT-----")
			print("Hours Slept:", sleep_hours)
			print("Sleep Status:", sleep_status)
			print("Sleep Score:", sleepQ_score)
			print("Sleep Quality:", sleepQ_value)
			print("Sleep well", name, ":)") 
			print()

		print()
		print("==Welcome==")
		print("[1] Caffeine Left Calculator")
		print("[2] Sleep Schedule")
		print("[3] Exit")

		option = input("Choose option: ")

		print()

		if option == "3":
			break 

		elif option == "1":
			caff_intake = int(input("How much caffeine did you consumer (in mg)? ")) #takes variable for caffeine intake input
			consumed = int(input("What time did you consume it (24-hour format, e.g. 14 for 2 PM)? ")) #takes variable for time consumed input
			sleep = int(input("What time do you plan to sleep (24-hour format, e.g. 23 for 11 PM)? ")) #takes variable for time sleep input
			coffee(caff_intake, consumed, sleep)

		elif option == "2":
			name = input("Enter name: ") #Gets string input value for name 
			sleep_hours = float(input("Hours sleep: ")) #Gets float input value for name
			
			sleep(name, sleep_hours)
		else:
			print("Invalid Input!")
main()
