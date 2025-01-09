num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 == num2 == num3:
    print("All numbers are equal")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("Two numbers are equal")
elif num1 > num2 > num3:
    print("numbers are in descending order")
elif num1 < num2 < num3:
    print("numbers are in ascending order")
else:
    print("No specific pattern found.")