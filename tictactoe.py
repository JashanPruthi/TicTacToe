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
    if board == initial_state():
        return X
    else:
        countx = 0
        counto = 0
        for i in board:
            for j in i:
                if j == X:
                    countx += 1
                if j == O:
                    counto += 1
        if countx > counto:
            return O
        elif countx == counto:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                list.append((i,j))
    return list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    cell = boardCopy[action[0]] [action[1]]
    if cell == X or cell == O:
        raise Exception("This cell is already filled")
    else:
        boardCopy[action[0]] [action[1]] = player(board)
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for horizontal in board:
        countx =0
        counto =0
        for cell in horizontal:
            if cell==X:
                countx+=1
            if cell==O:
                counto+=1
        if countx==3:
            return X
            break
        if counto==3:
            return O
            break

    for i in range(len(board)):
        cntx = 0
        cnto = 0
        for cell in board:
            if cell[i]==X:
                cntx+=1
            if cell[i]==O:
                cnto+=1
        if cntx==3:
            return X
            break
        if cnto==3:
            return O
            break
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    else:
        None
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        for i in board:
            for j in i:
                if j == EMPTY:
                    return False
        return True
            


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

def boardResultsMethod(board):
    lst = []
    for action in actions(board):
        actionOnBoard = result(board, action)
        #print(actionOnBoard,end ="\n")
        if terminal(actionOnBoard):
            possibleWinner = utility(actionOnBoard)
            #print(possibleWinner)
        else:
            possibleWinner = minimax(actionOnBoard)[0]
        lst.append( (possibleWinner, action) )
    #print(lst)
    return lst


def minimax(board):
    
    #Returns the optimal action for the current player on the board.
    """
    """
    if terminal(board) == True:
        return None

    # boardResults[] consists pairs of (result, action) for the possible results of current board
    #print(board,"from minimax")
    boardResults = boardResultsMethod(board)
    #print(player(board) == X)
    if player(board) == X:
        #print(player(board) == X)
        bestMove = ( -math.inf, (0,0) )
        #(boardResults[0])
        for tpl in boardResults:
            if tpl[0] > bestMove[0]:
                bestMove =( max(tpl[0], bestMove[0]), tpl[1])
    elif player(board) == O:
        bestMove = ( math.inf, (0,0) )
        for tpl in boardResults:
            if tpl[0] < bestMove[0]:
                bestMove =( min(tpl[0], bestMove[0]), tpl[1])  
    #print(bestMove[0], "calculated bestMove")
    return bestMove
    
"""
    counto = 0
    for i in board:
        for j in i:
            if j == O:
                counto +=1
                
    list = [ (0,1), (1,0), (1,2), (2,1) ]
    return (list[counto])
"""
    
    
