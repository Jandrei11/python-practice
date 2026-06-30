# basic two-value arithmetic calculator
print("1 -> Addition")
print("2 -> Subtraction")
print("3 -> Multiplication")
print("4 -> Division")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
perf1 = int(input("Enter mathematical operation: "))

if perf1 == 1:
    print(number1 + number2)
elif perf1 == 2:
    print(number1 - number2)
elif perf1 == 3:
    print(number1 * number2)
elif perf1 == 4:
    print(float(number1 / number2))
else:
    print("Invalid operation.")
