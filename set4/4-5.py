age = int(input("Enter your age: "))
book_type = input("Enter your favorite book type (fiction, non-fiction, graphic novel, poetry): ").lower()
reading_speed = int(input("How many pages can you read in an hour? "))
author_preference = input("Do you have a favorite author? (yes/no): ").lower()
if age < 18:
    if author_preference == "yes":
        if reading_speed > 30:
            if book_type == "graphic novel":
                print("You belong in the Graphic Novel Enthusiasts group.")
elif age >= 18:
    if book_type == "fiction":
        if reading_speed > 50:
            if author_preference == "no":
                print("You belong in the Fiction Readers group.")
elif age >= 25:
    if book_type == "non-fiction":
        if reading_speed <= 30:
            if author_preference == "yes":
                print("You belong in the Non-Fiction Specialists group.")
elif age < 25:
    if book_type == "poetry":
        if reading_speed <= 20:
            if author_preference == "no":
                print("You belong in the Poetry Beginners group.")
else:
    print("We recommend joining the General Book Club.")