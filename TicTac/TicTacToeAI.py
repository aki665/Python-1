import random


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    #print(board[move]==' ')
    #print(move)

    if board[move] == ' ':
        return True
    else:
        return False


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i) is True:
            possibleMoves.append(i)
    #print(possibleMoves)
    if len(possibleMoves) != 0:

        return random.choice(possibleMoves)
    else:
        return None


def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.

    # We use bo instead of board and le instead of letter so we don’t have to type as much.

    if ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
            (bo[0] == le and bo[1] == le and bo[2] == le) or  # across the bottom
            (bo[6] == le and bo[3] == le and bo[0] == le) or  # down the left side
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the middle
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the right side
            (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal
            (bo[8] == le and bo[4] == le and bo[0] == le)): # diagonal
        return True


def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def makeMove(board, move, letter):
    print(board)
    board[move] = letter
    print(board)

def getComputerMove(board):
    # Here is our algorithm for our Tic Tac Toe AI:

    # First, check if we can win in the next move
    for i in range(9):
        copy = getBoardCopy(board)

        if isSpaceFree(copy, i) is True:

            makeMove(copy, i, 'O')

            if isWinner(copy, 'O'):
                return i+1

    # Check if the player could win on their next move, and block them.

    for i in range(9):

        copy = getBoardCopy(board)

        if isSpaceFree(copy, i) is True:
            makeMove(copy, i, 'X')
            print("This is i: ", i)
            print("This is the copy of the board: ", copy)
            if isWinner(copy, 'X'):
                print("X will win, so block: ", i)
                return i+1

    print(board)

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])

    if move != None:
        return move+1

    #Take middle if its free
    if isSpaceFree(board, 4):
        return 5

    # Move on one of the sides.

    return chooseRandomMoveFromList(board, [1, 3, 5, 7]) + 1
