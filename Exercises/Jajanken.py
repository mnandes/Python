import random

# Input Options
moves = ["Rock", "Paper", "Scissor"]

# Score Keeper
score = [0,0]

# Exit Variable
flag = 1

# Return value 1 for Player Win, 0 for Draw, -1 for Computer Win and -2 for Program Exit
def get_moves():

    p_value = int(input("Please choose your move (1 - Rock, 2 - Paper, 3 - Scissor, Any other number to end game):\n"))
    
    # Check exit input
    if(p_value > 3 or p_value < 1):
        return -2

    cp_value = random.choice(moves)

    # Instantly detect Draw
    if(moves[p_value - 1] == cp_value):
        return 0

    # Checking every possible combination aside from Draw
    if(cp_value	== moves[0]):
        if(moves[p_value - 1] == "Paper"):
            return 1
        if(moves[p_value - 1] == "Scissor"):
            return -1

    if(cp_value	== moves[1]):
        if(moves[p_value - 1] == "Rock"):
            return -1
        if(moves[p_value - 1] == "Scissor"):
            return 1

    if(cp_value	== moves[2]):
        if(moves[p_value - 1] == "Rock"):
            return 1
        if(moves[p_value - 1] == "Paper"):
            return -1

# Loop game infinitely (until exit input)
while(flag):

    result = get_moves()

    if(result == 1):
        score[0] += 1
        print("Player Wins")

    if(result == 0):
        print("Draw")

    if(result == -1):
        score[1] += 1
        print("PC Wins")

    # Print Score
    print("Player - " + str(score[0]) + "    PC - " + str(score[1]) + "\n")

    if(result == -2):
        print("Game is Over, thanks for playing!")
        break
