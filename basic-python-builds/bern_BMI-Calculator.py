# ----------------------------------------------------------
# Assessment 1: BMI Calculator
# ----------------------------------------------------------
# Write a program that asks the user for their weight in kilograms (e.g., 70) and height in meters (e.g., 1.75).
# Cast the inputs to floats, calculate the BMI, and print the result.
# Formula: BMI = weight in kg / (height in meters * height in meters)

weight = float(input("Enter your Weight (in Kg): ")) #asks for weight input in float value (decimals included)
height = float(input("Enter your Height (in Meters): ")) #asks for height input in float value (decimals included)

total_bmi = weight / (height * height) #calculates BMI with given formula (mathematically, weight divided by height^2)

if (weight >= 635 or weight < 0) or (height >= 3 or height < 0): #will use better function to limit inputs to only Kg and m soon
    print("Invalid Value")
elif total_bmi < 18.5: #value from total_value variable compared to set threshold
    print("Your BMI is: ",total_bmi, "Underweight") #print combination of BMI result, total_bmi variable stored value, string value for set threshold
elif 18.5 <= total_bmi <= 24.9: #value from total_value variable compared to set threshold
    print("Your BMI is: ",total_bmi, "Normal") #print combination of BMI result, total_bmi variable stored value, string value for set threshold
elif 25.0 <= total_bmi <= 29.9: #value from total_value variable compared to set threshold
    print("Your BMI is: ",total_bmi, "Overweight") #print combination of BMI result, total_bmi variable stored value, string value for set threshold
else: #value from what's left, >30 compared to set threshold
    print("Your BMI is: ",total_bmi, "Obese") #print combination of BMI result, total_bmi variable stored value, string value for set threshold
