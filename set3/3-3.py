age = int(input("Enter your age: "))
income = int(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))

if age >= 18 and income >= 30000 and credit_score >= 700:
    print("Loan approved.")
elif age >= 18 and income >= 30000 and credit_score >= 600:
    print("Loan approved with higher interest.")
