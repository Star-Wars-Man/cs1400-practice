# get input from user
temperature = int(input("Enter the temperature in Fahrenheit: "))
is_raining = False
raining = input("Is it raining? (yes/no): ").lower()
if raining == "yes" or raining == "y":
    is_raining = True
is_windy = False
windy = input("Is it windy? (yes/no): ").lower()
if windy == "yes" or windy == "y":
    is_windy = True
time_of_day = input("What time of day is it? (morning, afternoon, evening): ").lower()
# determine what to wear
if temperature < 50:
    if is_raining:
        print("heavy coat and umbrella")
    elif is_windy:
        print("windbreaker and gloves")
    else:
        print("jacket and scarf")
elif temperature <= 70:
    if time_of_day == "morning":
        print("light jacket")
    elif time_of_day == "afternoon":
        print("long-sleeve shirt")
    elif time_of_day == "evening" and is_windy:
        print("sweater and scarf")
    else:
        if is_raining:
            print("raincoat and breathable clothes")
        else:
            print("t-shirt and shorts")