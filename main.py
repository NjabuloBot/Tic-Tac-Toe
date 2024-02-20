# Function to print Tic Tac Toe
def mytictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")
 
 
 # Function to print the score-board
def myscoreboard(scoreboard):
    print("\t--------------------------------")
    print("\t         SCORE BOARD       ")
    print("\t--------------------------------")
 
    listofplayers = list(scoreboard.keys())
    print("\t   ", listofplayers[0], "\t    ", scoreboard[listofplayers[0]])
    print("\t   ", listofplayers[1], "\t    ", scoreboard[listofplayers[1]])
 
    print("\t--------------------------------\n")
 
 
 # Function to check if any player has won
def check_Victory(playerpos, curplayer):
 
    # All possible winning combinations
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False 
