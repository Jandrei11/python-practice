#Name: Francis Jandrei E. Munoz
#Date: August 28, 2026
#Section: G-6L
"""
Description: This program asks for user inputs of name and hours of 
sleep they have. The stored values are then used to check various 
conditions such as their sleep status, the sleep score, and the sleep
quality of the user. It is then printed to show the results of each condition.
"""
print("==========Sleep Health Calculator=========")
name = input("Enter name: ") #Gets string input value for name 
sleep = float(input("Hours sleep: ")) #Gets float input value for name

#Checks conditions for sleep input and set quality values for sleep input
sleep_status = "tbd"
if (sleep < 7):
	sleep_status = "Sleep Deprived"
elif (sleep >= 7 and sleep <= 9):
	sleep_status = "Healthy Sleep"
elif (sleep > 9):
	sleep_status = "Oversleeping" 

#Uses input values from (sleep) to get new value stored in (SleepQ_score)
sleepQ_score = (sleep / 8) * 100

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

#Prints all stored values as results
print("-----RESULT-----")
print("Hours Slept:", sleep)
print("Sleep Status:", sleep_status)
print("Sleep Score:", sleepQ_score)
print("Sleep Quality:", sleepQ_value)
print("Sleep well", name, ":)")
