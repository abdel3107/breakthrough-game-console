"""
import sys
sys.path.append("..")

"""
import partie1
import os
import random

def init_board(file_path: str or None) -> list[list[int]]:
    """ This function initialises a new baord from the given file. If a file
    is not given as argument then it creates a table of dimension 7x7. We'll be using relative paths 
    to the file"""
    #relative path::: Desktop/Projet BreakThrough Python/board.txt
    #Absolute path::: C:/Users/Abdel/Desktop/Projet BreakThrough Python/board.txt
    if os.path.isfile(file_path): #Test if the given path is a file_path
        file = open(file_path, "r")
        list_of_lines = list(file) #Creates a list containing each line of the file
        dimension = list_of_lines[0].split() #Extract the dimension of the board from the list. The first line
        (rows, columns) = (int(dimension[0]), int(dimension[1]))
        #file.close()
        
        board = []
        board1 = [["B" for j in range(columns)] for k in range(2)]
        board2 = [["." for j in range(columns)] for k in range(rows-4)]
        board3 = [["W" for j in range(columns)] for k in range(2)]
        
        board.extend(board1)
        board.extend(board2)
        board.extend(board3)
        
        return board
    
    else: 
        return partie1.init_board(7)
        
"""Example of a call to the function init_board, Uncomment the code below to test """ 
board = init_board("Desktop/Projet BreakThrough Python/board.txt")


def is_playable(board, player, initial):
    """ This function takes initial """
    (a, b) = initial
    answer = False
    for index1 in range(len(board)):
        for index2 in range(len(board[0])):
            (x, y) = (index1, index2)
            if player == 1:
                if (((a - x) == 1) and (abs(b - y) == 1) and (board[a][b] == "W") and (board[x][y] != "W")) or (((a - x) == 1) and (abs(b - y) == 0) and (board[a][b] == "W") and (board[x][y] != "W") and (board[x][y] != "B")):
                    answer = True
            elif player == 2:
                if (((x - a) == 1)and (abs(b - y) == 1) and (board[a][b] == "B") and (board[x][y] != "B")) or (((x - a) == 1)and (abs(b - y) == 0) and (board[a][b] == "B") and (board[x][y] != "B") and (board[x][y] != "W")):
                    answer = True
    return answer

def ai_select_peg(board: list[list[int]], player: int) -> tuple :
    playable_list = []
    minimum_distance = len(board)
    if player == 1:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "W" and abs(i - 0) < minimum_distance:
                    minimum_distance = abs(i - 0)
        for index in range(len(board[minimum_distance])):
            if board[minimum_distance][index] == 'W' and is_playable(board, 1, (minimum_distance, index)):
                playable_list.append((minimum_distance, index))
        choice = random.choice(playable_list)
        return choice
    elif player == 2:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "B" and abs(len(board) - i) < minimum_distance:
                    minimum_distance = abs(i - 0)
        for index in range(len(board[minimum_distance])):
            if board[minimum_distance][index] == 'B' and is_playable(board, 2, (minimum_distance, index)):
                playable_list.append((minimum_distance, index))
        choice = random.choice(playable_list)
        return choice
    
def ai_move(board, pos, player):
    (a, b) = pos
    List = []
    for index1 in range(len(board)):
        for index2 in range(len(board[0])):
            (x, y) = (index1, index2)
            if player == 1:
                if (((a - x) == 1) and (abs(b - y) == 1) and (board[a][b] == "W") and (board[x][y] != "W")) or (((a - x) == 1) and (abs(b - y) == 0) and (board[a][b] == "W") and (board[x][y] != "W") and (board[x][y] != "B")):
                    answer = ((a, b),(x, y))
                    List.append(answer)
            elif player == 2:
                if (((x - a) == 1)and (abs(b - y) == 1) and (board[a][b] == "B") and (board[x][y] != "B")) or (((x - a) == 1)and (abs(b - y) == 0) and (board[a][b] == "B") and (board[x][y] != "B") and (board[x][y] != "W")):
                    answer = ((a, b),(x, y))
                    List.append(answer)
    choice = random.choice(List)
    return choice

print(board)    
#print(is_playable(board, 1, (5, 1))
pos = ai_select_peg(board, 1)
play = ai_move(board, pos, 1)
print(play)