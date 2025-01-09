# get student information
score = int(input("Enter student's score: "))
participation = int(input("Enter student's participation level (excellent, above average, average, poor): "))
homework_completed = False
homework = input("Did student complete your homework? (yes/no): ")
if homework == "yes":
    homework_completed = True
# determine grade
grade = "F"
if score >= 90:
    if participation == "excellent":
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    if participation == "excellent" or participation == "above average":
        grade = "B+"
    else:
        grade = "B"
elif score >= 70:
    if homework_completed:
        grade = "C+"
    else:
        grade = "C"
else:
    if participation == "poor":
        grade = "F"
    else:
        grade = "D"
