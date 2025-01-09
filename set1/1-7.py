import random
import os
    
# Store result of each round:
score = {"Bot": 0}

# Player name
acepted = False
while acepted == False:
    player = input("Name: ")
    if player != "Bot":
        print("Ok")
        acepted = True
    else:
        print("Can't use name try again")

# Add player:
score[player] = 0

# Game:
another = True
while another:
    # Player choice:
    x = int(input("Rock = 1 Paper = 2 Scissors = 3. 1 2 or 3: "))
    
    # Bot choice:
    bx = random.randint(1, 3)
    
    # Logic stuff:
    if x == 3 and bx == 1:
        print("Bot Wins")
        score["Bot"] += 1
    elif bx == 3 and x == 1:
        print(player + " wins")
        score[player] += 1
    elif bx == x:
        print("Tie")
    elif bx > x:
        print("Bot wins")
        score["Bot"] += 1
    elif x > bx:
        print(player + " wins")
        score[player] += 1
    # Ask if they want to play again
    again = int(input("1 to play again: "))
    if again != 1:
        another = False
os.system("clear")
# Store bot score
botscore = score["Bot"]
# Print score
if botscore == score[player]:
    print(f"Bot and {player} tied with {botscore} points each")
elif score["Bot"] > score[player]:
    print(f"Bot won {botscore} to {score[player]}")
elif score["Bot"] < score[player]:
    print(f"{player} won {score[player]} to {botscore}")