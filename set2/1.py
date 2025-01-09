age = int(input("Enter your age: "))
weekend = input("Is it weekend? (yes/no): ").lower()
is_weekend = weekend == "yes" or weekend == "y"
student = input("Are you a student? (yes/no): ").lower()
is_student = student == "yes" or student == "y"
price = 0
if age < 12:
    price = 8
elif age >= 12 and age < 18:
    if is_weekend:
        price = 12
    else:
        price = 10
elif age >= 18 and age < 65:
    if not is_weekend and is_student:
        price = 12
    else:
        price = 15
else:
    price = 10
print(f"Your ticket price is {price}$.")