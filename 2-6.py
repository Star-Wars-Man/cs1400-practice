distance = float(input("Enter the distance to travel in miles: "))
is_sunny = False
sunny = input("Is it sunny? (yes/no): ").lower()
if sunny == "yes" or sunny == "y":
    is_sunny = True
owns_bike = False
bike = input("Do you own a bike? (yes/no): ").lower()
if bike == "yes" or bike == "y":
    owns_bike = True
is_rush_hour = False
rush_hour = input("Is it rush hour? (yes/no): ").lower()
if rush_hour == "yes" or rush_hour == "y":
    is_rush_hour = True
if distance < 5:
    if is_sunny:
        print("Walk")
    else:
        print("Drive")
elif distance <= 20:
    if owns_bike:
        print("Bike")
    else:
        print("Bus")
else:
    if not is_rush_hour:
        print("Drive")
    else:
        print("Train")