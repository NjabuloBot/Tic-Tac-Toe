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
    
    
# Function to check if the game is drawn
def check_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False 
    
    
# Function for a single game of Tic Tac Toe
def singlegame(curplayer):
 
    # Represents the Tic Tac Toe
    val = [' ' for i in range(9)]
     
    # Stores the positions occupied by X and O
    playerpos = {'X' : [], 'O' : []}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        mytictactoe(val)
         
        # Try-Exception block for CHANCE input
        try:
            print("Player ", curplayer, " turn. Choose your Block : ", end="")
            chance = int(input()) 
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue
 
        # Sanity check for CHANCE input
        if chance < 1 or chance > 9:
            print("Invalid Input!!! Try Again")
            continue
 
        # Checking if the block is not occupied already
        if val[chance - 1] != ' ':
            print("Oops! The Place is already occupied. Try again!!")
            continue
 
        # Updating game information
 
        # Update the status of the grid 
        val[chance - 1] = curplayer
 
        # Update the positions of the player
        playerpos[curplayer].append(chance)
 
        # Calling Function to check Victory
        if check_Victory(playerpos, curplayer):
            mytictactoe(val)
            print("Congratulations! Player ", curplayer, " has won the game!!")     
            print("\n")
            return curplayer
 
        # Calling Function to check Tie
        if check_Tie(playerpos):
            mytictactoe(val)
            print("Game Tied")
            print("\n")
            return 'D'
 
        # Switching moves of the player
        if curplayer == 'X':
            curplayer = 'O'
        else:
            curplayer = 'X'
 
