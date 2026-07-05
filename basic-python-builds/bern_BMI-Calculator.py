# ----------------------------------------------------------
# Assessment 1: BMI Calculator
# ----------------------------------------------------------
# Write a program that asks the user for their weight in kilograms (e.g., 70) and height in meters (e.g., 1.75).
# Cast the inputs to floats, calculate the BMI, and print the result.
# Formula: BMI = weight in kg / (height in meters * height in meters)

weight = float(input("Enter your Weight (in Kg): "))
height = float(input("Enter your Height (in Meters): "))

total_bmi = weight / (height * height)

## will use better function to limit inputs to only Kg and m soon
if weight >= 635 or height >= 3: 
    print("Invalid Value")
elif weight <= 635 or height <= 3:
    print("Your BMI is: ", total_bmi)
    if total_bmi < 18.5:
        print("Underweight")
    elif 18.5 <= total_bmi <= 24.9:
        print("Normal")
    elif 25.0 <= total_bmi <= 29.9:
        print("Overweight")
    else:
        print("Obese")
