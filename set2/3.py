# Get info
total_amount = float(input("Enter the total amount: "))
total_items = int(input("Enter the total items: "))
is_member = input("Are you a member? (yes/no): ").lower()
if is_member == "yes" or is_member == "y":
    is_member = True
else:
    is_member = False
is_first_time_buyer = input("Is this your first time buying? (yes/no): ").lower()
if is_first_time_buyer == "yes" or is_first_time_buyer == "y":
    is_first_time_buyer = True
else:
    is_first_time_buyer = False
discount = 0

# logic
if total_amount > 200:
    if is_member:
        discount += 20
    else:
        discount += 10
elif total_amount >= 100:
    discount += 5
    if total_items > 5:
        total_amount -= 10
if total_amount < 100 and is_first_time_buyer:
    total_amount -= 5
total_amount -= (total_amount * discount) / 100
print(f"Total amount after discount: {total_amount}")