# get user input
income = float(input("Enter the annual income: "))
credit_score = int(input("Enter the credit score: "))
callateral = input("do you have a callateral? (yes/no): ").lower()
has_callateral = False
if callateral == "yes":
    has_callateral = True
loan_amount = float(input("Enter the loan amount: "))
# check loan eligibility
eligible = False
interest_rate = 0
if credit_score > 750:
    if income > 50000:
        eligible = True
        interest_rate = 5
    else:
        eligible = True
        interest_rate = 7
elif credit_score >= 600:
    if has_callateral:
        eligible = True
        interest_rate = 10
if eligible:
    print("Loan is approved with interest rate of: ", interest_rate, "%")
else:
    print("Loan is not approved")