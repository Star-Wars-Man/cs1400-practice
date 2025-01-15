customer_type = input("Are you a 'member' or 'guest'? ").lower()
years = int(input("How many years have you been a member? ")) if customer_type == "member" else 0
first_time = input("Is this your first visit? (yes/no): ").lower() if customer_type == "guest" else ""

if customer_type == "member" and years >= 5:
    print("You get a 20% discount.")
elif customer_type == "member" and years >= 2:
    print("You get a 10% discount.")
elif customer_type == "member" and years < 2:  
    print("You get a 5% discount.")

elif customer_type == "guest" and first_time == "yes":
    print("You get a 5% discount.")

elif customer_type == "guest" and first_time == "no":
    print("No discount for repeat guests.")
else:
    print("Invalid customer type.")