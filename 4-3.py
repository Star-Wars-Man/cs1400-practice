age = int(input("Enter your age: "))
smoker = input("Are you a smoker? (yes/no): ").lower()
bmi = float(input("Enter your BMI: "))
exercise = input("Do you exercise regularly? (yes/no): ").lower()

if age > 50:
    if smoker == "yes":
        if bmi > 30:
            if exercise == "no":
                    print("Your insurance premium is high.")
    
elif age > 40 and exercise == "no":
    if smoker == "yes":
        if bmi > 25:
            print("Your insurance premium is high.")
    
elif age > 30:
    if smoker == "no":
        if bmi < 25:
            if exercise == "yes":
                print("Your insurance premium is high.")

elif age < 30:
    if smoker == "no":
        if bmi < 20:
            if exercise == "yes":
                print("Your insurance premium is high.")

else:
    print("Your insurance premium is low.")