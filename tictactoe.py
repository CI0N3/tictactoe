
"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():

    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x = 0
    o = 0

    for letter in str(board):
        if letter == X:
            x += 1
        if letter == O:
            o += 1

    if x < o or (x == o):
        return X

    elif o < x:
        return O

    """
    Returns player who has the next turn on a board.
    """

    raise NotImplementedError

def actions(board):
    list = []

    for i in range (3):
        for j in range (3):
            if board[i][j] == EMPTY:
                list += {(i, j)}

    return list

    """
    Returns set of all possible actions (i, j) available on the board.
    """

    raise NotImplementedError


def result(board, action):
    ij = ""
    action = str(str(action).split())

    for number in action:
        if number == "0" or number == "1" or number == "2":
            ij += number

    i = int(ij[0])
    j = int(ij[1])

    score_1 = board[0][0]
    score_2 = board[0][1]
    score_3 = board[0][2]
    score_4 = board[1][0]
    score_5 = board[1][1]
    score_6 = board[1][2]
    score_7 = board[2][0]
    score_8 = board[2][1]
    score_9 = board[2][2]

    if i == 0 and j == 0:
        score_1 = player(board)
    if i == 0 and j == 1:
        score_2 = player(board)
    if i == 0 and j == 2:
        score_3 = player(board)
    if i == 1 and j == 0:
        score_4 = player(board)
    if i == 1 and j == 1:
        score_5 = player(board)
    if i == 1 and j == 2:
        score_6 = player(board)
    if i == 2 and j == 0:
        score_7 = player(board)
    if i == 2 and j == 1:
        score_8 = player(board)
    if i == 2 and j == 2:
        score_9 = player(board)

    return [[score_1, score_2, score_3],
            [score_4, score_5, score_6],
            [score_7, score_8, score_9]]

    """
    Returns the board that results from making move (i, j) on the board.
    """

    raise NotImplementedError

def winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == X:  # Checks horizontally
            return X
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == O:  # Checks horizontally
            return O

    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == X:  # Checks vertically
            return X
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == O:  # Checks vertically
            return O

    if (board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == board[1][1] and board[0][2] == board[2][0]) and board[1][1] == X:  # Checks diagonally
        return X

    if (board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == board[1][1] and board[0][2] == board[2][0]) and board[1][1] == O:  # Checks diagonally
        return O

    return None

    """
    Returns the winner of the game, if there is one.
    """

    raise NotImplementedError


def terminal(board):

    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != None:   #Checks horizontally
            return True

    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != None:   #Checks vertically
            return True

    if (board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == board[1][1] and board[0][2] == board[2][0]) and board[1][1] != None:  #Checks diagonally
        return True

    if board[0][0] != EMPTY and board[0][1] != EMPTY and board[0][2] != EMPTY and board[1][0] != EMPTY and board[1][1] != EMPTY and board[1][2] != EMPTY and board[2][0] != EMPTY and board[2][1] != EMPTY and board[2][2] != EMPTY:
        return True

    return False

    """
    Returns True if game is over, False otherwise.
    """

    raise NotImplementedError


def utility(board):

    if winner(board) == X:
        return 1

    elif winner(board) == O:
        return -1

    else:
        return 0

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    raise NotImplementedError


def minimax(board):


    def maxvalue(board):
        if terminal(board):
            return utility(board)
        value = -math.inf
        for action in actions(board):
            value = max(value, minvalue(result(board, action)))
        return value


    def minvalue(board):
        if terminal(board):
            return utility(board)
        value = math.inf
        for action in actions(board):
            value = min(value, maxvalue(result(board, action)))
        return value


    if terminal(board):
        return None

    if player(board) == X:
        for action in actions(board):
            if minvalue(result(board, action)) == maxvalue(board):
                return action

    if player(board) == O:
        for action in actions(board):
            if maxvalue(result(board, action)) == minvalue(board):
                return action

    """
    Returns the optimal action for the current player on the board.
    """

    raise NotImplementedError
