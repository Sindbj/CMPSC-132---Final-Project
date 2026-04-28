# TIC TAC TOE
# 2 Player
#Input -> 0-2 etc

def input_Validation(row, col): 
    row = str(row) # making row and col a string let me use 'try' to test if it is an integer
    col = str(col)
    try:   
        if len(row) != 1 or len(col) != 1: # should only be 1 digit
            return False
        
        row = int(row)
        col = int(col)

        if 0 > row or row > 2 or 0 > col or col > 2: # between 0 and 2
            return False

        else:
            return True
    except ValueError: # was not an integer
        return False



def print_board(row, col, player_1, Board): # update board and return true / false  for if board updated
    if Board[row][col] == '.': # can update
        if player_1: # update to 'x'
            Board[row][col] = 'x' 
        else:
            Board[row][col] = 'o'     
        print(Board[0][0] + " | " + Board[0][1] + " | " + Board[0][2]) # display updated board
        print("---------")
        print(Board[1][0] + " | " + Board[1][1] + " | " + Board[1][2])
        print("---------")
        print(Board[2][0] + " | " + Board[2][1] + " | " + Board[2][2])
        return True
    else:
        return False # board was not updated

def win_Check(Board):
    possible_checks = [[[0,0],[0,1],[0,2]], # row 1
                       [[1,0],[1,1],[1,2]], # row 2
                       [[2,0],[2,1],[2,2]], # row 3
                       [[0,0],[1,0],[2,0]], # col 1 
                       [[0,1],[1,1],[2,1]], # col 2
                       [[0,2],[1,2],[2,2]], # col 3
                       [[0,0],[1,1],[2,2]], # diag 1
                       [[0,2],[1,1],[2,0]]] # diag 2
    for i in possible_checks: # check every win condition per round
        first_peice = Board[i[0][0]][i[0][1]]
        win = True
        for j in i:
            if Board[j[0]][j[1]] != first_peice or Board[j[0]][j[1]] == '.': # if the values are not the same or '.' then the player does not win
                win = False
        if win:
            return True



def play():

    Board = [['.','.','.'],
             ['.','.','.'],
             ['.','.','.']]
    round = 0
    player_1 = None
    while round <= 8 and win_Check(Board) == None: # if 9 rounds -> tie, otherwise check for a win every round
        round += 1      
        if round % 2 != 0: # odd and therefore player 1
            player_1 = True
            y = input('\nPlayer 1 please input a valid board row (0-2) ')
            x = input('Player 1 please input a valid board col (0-2) ')

            while not input_Validation(x,y):
                print("Player 1 - invalid input")
                y = input('\n Player 1 please input a valid board row (0-2) ')
                x = input('Player 1 please input a valid board col (0-2) ')
            x = int(x)  
            y = int(y) # input was a string before but list indexing needs an integer



        else:
            player_1 = False
            y = input('\n Player 2 please input a valid board row (0-2) ')
            x = input('Player 2 please input a valid board col (0-2) ')

            while not input_Validation(x,y):
                print("Player 2 - invalid input")
                y = input('\n Player 2 please input a valid board row (0-2) ')
                x = input('Player 2 please input a valid board row (0-2) ')
            x = int(x)  
            y = int(y)  # input was a string before but list indexing needs an integer       

        if not print_board(y, x, player_1, Board): # position is taken
            round -= 1 # go back a round
            print("\n Position has already been taken!")


    if win_Check(Board):
        if player_1:
            print("\n Player 1 wins !") 
            return True # used to add player scores
        else:
            print("\n Player 2 wins !")
            return False
                
    else: # tie
        print("\n The game was a tie.")
        return None



    



def main():
    print("WELCOME TO TIC TAC TOE")
    play_again = "y"
    games = 0
    score_1 = 0
    score_2 = 0

    while play_again == "y":
        played = play()
        if played: # add player scores
            score_1 += 1
        elif played == False:
            score_2 += 1
        games += 1

        print("End of round {}".format(games))
        print("\n Player 1: {}".format(score_1))
        print("Player 2: {}".format(score_2))
        print("Ties: {}".format(games-(score_1+score_2)))

        play_again = input("\n Do you want to play again? (y/n): ").strip().lower()
        while play_again != 'y' and play_again != 'n': # progress to another round or end program
            print("\n Input was not a 'y' or 'n'")
            play_again = input("\n Do you want to play again? (y/n): ").strip().lower()

    print("\nThanks for playing!")



main()