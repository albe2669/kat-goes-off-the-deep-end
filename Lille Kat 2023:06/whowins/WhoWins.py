import functools

def checkBoard(player, board):
    return horizontal(player, board) or vertical(player, board) or diagonalWin(player, board)

def horizontal(player, board):
    for i in range(3):
        hasWon = board[0+(3*i)] == player and board[1+(3*i)] == player and board[2+(3*i)] == player 
        if hasWon: 
            return hasWon
    return False

def vertical(player, board):
    for i in range(3):
        hasWon = board[i] == player and board[3+i] == player and board[6+i] == player 
        if hasWon: 
            return hasWon
    return False
        
def diagonalWin(player, board):
    hasWon = board[0] == player and board[4] == player and board[8] == player
    return board[2] == player and board[4] == player and board[6] == player or hasWon

board = list(functools.reduce(lambda a, b: a + b, [input().split() for _ in range(3)])) 

johan = checkBoard('X',board)
if(johan):
    print("Johan har vunnit")
else:
    abdullah = checkBoard('O',board)
    if (abdullah):
        print("Abdullah har vunnit")
    else:
        print("ingen har vunnit")
