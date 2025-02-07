team_size = int(input("Enter the size of your gaming team: "))
game_genre = input("Enter the game genre for the event (MOBA, FPS, RTS, Battle Royale): ").lower()
experience_level = input("Enter your experience level (beginner, intermediate, expert): ").lower()
location = input("Is the event local or online? (local/online): ").lower()

if (team_size >= 5 and game_genre == "moba" and experience_level == "expert" and location == "local") or \
   (team_size >= 3 and game_genre == "rts" and experience_level == "intermediate" and location == "local") or \
   (team_size <= 2 and game_genre == "battle royale" and experience_level == "expert" and location == "online"):
    print("You are eligible to participate in the event.")

elif (team_size == 1 and game_genre == "fps" and experience_level == "beginner" and location == "online"):
    print("You are eligible to participate in the event.")

else:
    print("You do not meet the criteria for the event.")