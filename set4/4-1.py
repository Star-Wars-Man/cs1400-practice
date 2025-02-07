starting_city = input("Enter the starting city: ")
destination_city = input("Enter the destination city: ")
travel_method = input("Enter the preferred travel method (car, train, plane): ").lower()


if travel_method == "car":
    if starting_city != destination_city:
        print("Suggestion: Take a road trip!")

elif travel_method == "train":
    if starting_city != destination_city:
        print("Suggestion: Book a train ticket.")

elif travel_method == "plane":
    if starting_city != destination_city:
        print("Suggestion: Book a flight.")

else:
    print("Invalid or unnecessary travel details.")