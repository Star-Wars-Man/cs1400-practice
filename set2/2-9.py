# get input from user
nights = int(input("Enter the number of nights staying: "))
is_weekend = False
weekend = input("Is it a weekend? (yes/no): ").lower()
if weekend == "yes" or weekend == "y":
    is_weekend = True
room_type = input("Enter the room type (standard, deluxe, suite): ").lower()
has_memership = False
membership = input("Do you have a membership? (yes/no): ").lower()
if membership == "yes" or membership == "y":
    has_memership = True
# calculate rate and discount
discount = 0
price = 0
if room_type == "standard":
    price = 100
elif room_type == "deluxe":
    price = 150
else:
    price = 200
if is_weekend:
    price += 20
    if room_type == "suite":
        price += 30
if has_memership:
    discount+= 10
if nights > 5:
    discount += 5
# calculate total
toatal = price * nights
toatal -= toatal * (discount / 100)
print(f"Total cost: {toatal}")