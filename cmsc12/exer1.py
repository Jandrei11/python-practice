#Name: Francis Jandrei E. Munoz
#Section: CMSC 12 G-6L
#Date: August 14, 2026

caff_intake = int(input("How much caffeine did you consumer (in mg)? ")) #takes variable for caffeine intake input
time_consumed = int(input("What time did you consume it (24-hour format, e.g. 14 for 2 PM)? ")) #takes variable for time consumed input
time_sleep = int(input("What time do you plan to sleep (24-hour format, e.g. 14 for 2 PM)? ")) #takes variable for time sleep input

print("Starting with", caff_intake, "mg of caffeine at", time_consumed) 

# formula for time elapsed with half time
intake1 = caff_intake * (0.5 ** (1/5)) 
intake2 = caff_intake * (0.5 ** (3/5))
intake3 = caff_intake * (0.5 ** (5/5))
intake4 = caff_intake * (0.5 ** (8/5))
intake5 = caff_intake * (0.5 ** (12/5))

print("After", 1, "hour:", intake1,"mg remaining")
print("After", 3, "hour:", intake2,"mg remaining")
print("After", 5, "hour:", intake3,"mg remaining")
print("After", 8, "hour:", intake4,"mg remaining")
print("After", 12, "hour:", intake5,"mg remaining")

# formula for caffeine left after time elapsed after x-time consumed
caffeine_left = caff_intake * 0.5 ** ((time_sleep-time_consumed)/5)
print("By your bedtime", (time_sleep), "you will still have", caffeine_left, "mg of caffeine in your system")
Displaying Munoz_ex1.py.
