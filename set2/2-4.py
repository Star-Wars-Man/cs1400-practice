# get input from user
income = float(input("Enter the annual income: "))
married = input("Are you married? (yes/no): ").lower()
is_married = False
if married == "yes" or married == "y":
    is_married = True
has_dependents = False
dependents = input("Do you have dependents? (yes/no): ").lower()
if dependents == "yes" or dependents == "y":
    has_dependents = True
owns_business = False
business = input("Do you own a business? (yes/no): ").lower()
if business == "yes" or business == "y":
    owns_business = True
# calculate tax
tax = 0
if income < 30000:
    if is_married:
        tax = 8
    else:
        tax = 10
elif income <= 100000:
    if has_dependents:
        if is_married:
            tax = 12
        else:
            tax = 15
    else:
        tax = 18
else:
    if owns_business:
        tax = 25
    else:
        tax = 28
# print the result
print("Yor tax is: ", tax, "%")