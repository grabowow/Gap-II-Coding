# Trying to rebuild Tic Tac Toe with classes instead of just functions, this way I can practice. 
from random import randint
from time import sleep

class Gameplay:
    def __init__(self):
        self.gameboard = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]
        print("Welcome to Tic Tac Toe. Today you have to play against the computer")
        self.p1 = Player("X",1,"The Human")
        self.p2 = Player("O",2,"The Computer")
        self.print_grid()
        print("You will have to enter the value you want on a grid with values 1-3 for first rows, then columns. ")
        self.game_over = False
        self.game_play()
    
    def print_grid(self):
        print("  " + str(["1","2","3"]))
        for a in range(3):
            print(str(a + 1) + " " + str(self.gameboard[a]))
    
    def game_play(self):
        turn_count = 0
        while turn_count < 9 and self.game_over == False:
            if turn_count % 2 == 0:
                turn_count += 1
                player = self.p1
                self.human_play(player)
                self.check_winner(player)
            else:
                turn_count += 1
                player = self.p2
                self.computer_play(player)
                self.check_winner(player)
            
    def human_play(self,player):
        correct_move = False
        while correct_move == False:
            try:    
                player.row = int(input('Choose a row: 1 through 3:')) - 1
                player.column = int(input('Choose a column: 1 to 3:')) - 1
                if self.gameboard[player.row][player.column] == " ":
                    self.gameboard[player.row][player.column] = player.char
                    correct_move = True
                elif self.gameboard[player.row][player.column] != " ":
                    print("You can't play there - someone already has!")
                    print("The value here is {x}.".format(x = self.gameboard[player.row][player.column]))
            except:
                print("Please try again - the location doesn't exist")
        self.print_grid()

    def computer_play(self,player):
        correct_move = False
        while correct_move == False: 
            player.row = randint(0,2)
            player.column = randint(0,2)
            if self.gameboard[player.row][player.column] == " ":
                self.gameboard[player.row][player.column] = player.char
                sleep(1)
                print("The computer has made it's move:")
                sleep(.5)
                self.print_grid()
                correct_move = True
            else:
                continue

    def check_winner(self,pot_winner):
        # doing the rows check first, it's the easiest
        for a in range(3):
            if self.gameboard[a][0] == pot_winner.char and self.gameboard[a][0] == self.gameboard[a][1] and self.gameboard[a][1] == self.gameboard[a][2]:
                self.game_over = True
                print("We have a winner! {x} has won the game.".format(x = pot_winner.name))
                return self.game_over
        # ok so now the columns
        for a in range(3):
            if self.gameboard[0][a] == pot_winner.char and self.gameboard[0][a] == self.gameboard[1][a] and self.gameboard[1][a] == self.gameboard[2][a]:
                self.game_over = True
                print("We have a winner! {x} has won the game.".format(x = pot_winner.name))
                return self.game_over
        # upper right to lower left diagonal
        if self.gameboard[0][0] == pot_winner.char and self.gameboard[0][0] == self.gameboard[1][1] and self.gameboard[1][1] == self.gameboard[2][2]:
            self.game_over = True
            print("We have a winner! {x} has won the game.".format(x = pot_winner.name))
            return self.game_over
        # upper left to lower right diagonal
        if self.gameboard[0][2] == pot_winner.char and self.gameboard[0][2] == self.gameboard[1][1] and self.gameboard[1][1] == self.gameboard[2][0]:
            self.game_over = True
            print("We have a winner! {x} has won the game.".format(x = pot_winner.name))
            return self.game_over

class Player:
    def __init__(self, char, num, name):
        self.char = char
        self.num = num
        self.row = None
        self.column = None
        self.name = name

Gameplay()