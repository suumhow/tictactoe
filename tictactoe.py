"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """

    # Count the number of X's and O's on the board
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #get size of the board x and y  to be used in the loop to get all possible actions 
    x = len(board)
    y = len(board[0])

    # Create a set of all possible actions
    possible_actions = set()
    for i in range(x):
        for j in range(y):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

    raise NotImplementedError


def result(board, action):
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Action is not valid")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    # Check if the board is full
    for row in board:
        if EMPTY in row:
            return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
    raise NotImplementedError




def minimax(board):

    """
    Returns the optimal action for the current player on the board. Alpha-Beta Pruning edition ;)
    """
    if terminal(board):
        return None

    

    if player(board) == X:
        value, move = max((min_value(result(board, action), -math.inf, math.inf), action) for action in actions(board))
    else:
        value, move = min((max_value(result(board, action), -math.inf, math.inf), action) for action in actions(board))
    return move

    raise NotImplementedError

def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
