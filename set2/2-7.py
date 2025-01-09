# get user input
age = int(input("Enter your age: "))
fitness_level = input("Enter your fitness level (beginner, intermediate, advanced): ")
goal = input("Enter your goal (strength, cardio, weight loss): ")
has_health_conserns = False
health_conserns = input("Do you have any health conserns (yes, no): ").lower()
if health_conserns == "yes" or health_conserns == "y":
    has_health_conserns = True
# logic
if age < 18:
    if goal == "strength":
        print("Youth Strength Program")
    elif goal == "cardio":
        print("Youth Cardio Plan")
elif age <= 50:
    if fitness_level == "beginner":
        print("Beginner Strength and Cardio")
    elif fitness_level == "intermediate" or fitness_level == "advanced":
        if goal == "weight loss":
            print("HIIT and Strength Plan")
        elif goal == "strength":
            print("Advanced Strength Program")
else:
    if has_health_conserns:
        print("Gentle Mobility Program")
    else:
        print("Active Aging Plan")