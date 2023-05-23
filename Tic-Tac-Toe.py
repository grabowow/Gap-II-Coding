# Creating a basic tic-tac-toe game using lists. The computer plays randomly, finding a spot on the board which is empty.
import random
from time import sleep

# setting up the game board and printing initial message for the user
print("Let's play tic-tac-toe!")
game_board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
print(*game_board, sep = "\n")
print(['1','2','3'])
print("The way this works is that you have to enter coordinates. You as the player are going to mark X, and the computer will mark O. The playing board is a 3x3 grid, so enter 2 numbers from 1 - 3.")

# creating a function for human play
def human_play():
    correct_move = False
    while correct_move == False:
        row = int(input("Choose your row (num 1 - 3)")) - 1
        column = (int(input("Choose your column (num 1 -3)"))) - 1
        if game_board[row][column] == " ":
            game_board[row][column] = "X"
            correct_move = True
        else:
            print("You can't play there - someone already has!")
            print("This square has a value of {x}".format(x = game_board[row][column]))
    print(*game_board, sep = "\n")
    sleep(1)
    if check_winner() == False:
        sleep(1)
        print('---')
        print("Now it's the computer's turn.")
        sleep(.5)
        return False
    return True

# creating a function for the computer to play basically randomly - it will choose at random until it finds an open value
def computer_play():
    x = False
    while x == False:
        row = random.randint(0,2)
        column = random.randint(0,2)
        if game_board[row][column] == " ":
            game_board[row][column] = "O"
            x = True
        else:
            continue
    print(*game_board, sep = "\n") 
    if check_winner() == False:
        sleep(1)
        print("Now it's your turn again")
        sleep(.5)
        return False
    return True

# Creating a function to check for the winner, and eventually break out of the loop (which I still need to build) when this happens
def check_winner():
    winner_var = False
    # adding functionality to see who won - it's in there
    winner_player = ""
    for a in game_board:
        streak_sum = 0
        for b in a:
            if b == "X":
                streak_sum += 1
            elif b == "O":
                streak_sum -= 1
        if abs(streak_sum) == 3:
            winner_var = True
            print("We have a winner!")
            if streak_sum > 0:
                winner_player = "Human"
            else:
                winner_player = "Computer"
            print("The {x} won!".format(x = winner_player))
            return winner_var
    for a in range(3):
        streak_sum = 0
        for b in game_board:
            if b[a] == "X":
                streak_sum += 1
            elif b[a] == "O":
                streak_sum -= 1
        if abs(streak_sum) == 3:
            winner_var = True
            print("We have a winner!")
            if streak_sum > 0:
                winner_player = "Human"
            else:
                winner_player = "Computer"
            print("The {x} won!".format(x = winner_player))
            return winner_var
    streak_sum = 0
    for a in range(3):
        if game_board[a][a] == "X":
            streak_sum += 1
        elif game_board[a][a] == "O":
            streak_sum -= 1
        if abs(streak_sum) == 3:
            winner_var = True 
            print("We have a winner!")
            if streak_sum > 0:
                winner_player = "Human"
            else:
                winner_player = "Computer"
            print("The {x} won!".format(x = winner_player))
            return winner_var
    streak_sum = 0
    for a in range(3):
        if game_board[a][2-a] == "X":
            streak_sum += 1
        if game_board[a][2-a] == "O":
            streak_sum -= 1
        if abs(streak_sum) == 3:
            winner_var = True 
            print("We have a winner!")
            if streak_sum > 0:
                winner_player = "Human"
            else:
                winner_player = "Computer"
            print("The {x} won!".format(x = winner_player))
            return winner_var
    print("No winner yet... ")
    return winner_var
        
human_play()
computer_play()
human_play()
computer_play()    
if human_play() == False:
    if computer_play() == False:
        if human_play() == False:
            if computer_play() == False:
                human_play()