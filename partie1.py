


dic_alphabet ={0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l",
                   12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w",
                   23:"x", 24:"y", 25:"z"}

dic_alpha_to_letter = {} #For conversion

for key in dic_alphabet:
    dic_alpha_to_letter[dic_alphabet[key]] = key
    


def init_board(n : int) -> list[list[int]]:  #Already tested
    board = []
    
    board1 = [["B" for j in range(n)] for k in range(2)]
    board2 = [["." for j in range(n)] for k in range(n-4)]
    board3 = [["W" for j in range(n)] for k in range(2)]
    
    board.extend(board1)
    board.extend(board2)
    board.extend(board3)
    
    return board


def print_board(board : list[list[int]]) -> None:  #Already tested
    """dic_alphabet ={0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l",
                   12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w",
                   23:"x", 24:"y", 25:"z"}"""
    L = []
    
    
    item1 = []
    value1 = "  "
    value2 = ["_" for j in range(len(board))]
    value3 = " "
    item1.append(value1)
    item1.append(" ")
    item1.extend(value2)
    item1.append(value3)
    
    space = []
    va = " "
    va = [" " for j in range(len(board))]
    va = " "
    item1.append(va)
    item1.append(va)
    item1.extend(va)
    item1.append(va)
    
    item2 = [[i] for i in range(len(board), 0, -1)]
    
    for i in range(len(item2)):
        if len(str(item2[i][0])) == 1:
            item2[i][0] = " " + str(item2[i][0])
        elif len(str(item2[i][0])) == 2:
            item2[i][0] = str(item2[i][0])
    
            
    for j in range(len(item2)):
        item2[j].extend(["|"])
        item2[j].extend(board[j])
        item2[j].extend(["|"])
     
    item3 = []
    val1 = "  "
    val2 = [dic_alphabet[j] for j in range(len(board))]
    val3 = " "
    item3.append(val1)
    item3.append(" ")
    item3.extend(val2)
    item3.append(val3)
    
    L.append(item1)
    L.append(space)
    L.extend(item2)
    L.append(item1)
    L.append(space)
    L.append(item3)
    
    #The part to print the obtained list:
    for i in range(len(L)):
        for j in range(len(L[i])):
            L[i][j] = str(L[i][j])
     
    #return L
    for i in range(len(L)):
        out = " "
        for j in range(len(L[i])):
            out = out + " " + L[i][j] + " "
        print(out)

def winner(board : list[list[int]]) -> int or None: #Already tested
    if "W" in board[0]:
        return 1
    elif "B" in board[len(board)-1]:
        return 2
    else:
        return None

def is_in_board(n : int, pos : tuple[int, int]) -> bool: #Tested
    (a, b) = pos
    if (a < n) and (b < n):
        return True
    else:
        return False

def input_move() -> str: #Tested
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    move = input("Entrez un coup  ")
    if ">" in move:
        L = move.split(">")
        if (len(L[0]) == 2 or len(L[0]) == 3) and (len(L[1]) == 2 or len(L[1]) == 3):
            first_part = list(L[0])
            second_part = list(L[1])
            if (first_part[0] in letters) and (second_part[0] in letters):
                a = True
                b = True
                for i in range(1, len(first_part)):
                    if first_part[i] not in numbers:
                        a = False
                for j in range(1, len(second_part)):
                    if second_part[j] not in numbers:
                        b = False
                if (a == True) and (b == True):
                    return move
                else:
                    return input_move() #Added the returns here after debugging
            else:
                return input_move()
        else:
            return input_move()  
    else:
        return input_move()


def extract_pos(n : int, str_pos : str) -> tuple[int, int] or None: #Tested
    j = dic_alpha_to_letter[str_pos[0]]
    i = n - int(str_pos[1:len(str_pos)])
    return (i,j)

def check_move(board : list[list[int]], player : int, str_move : str) -> bool: #Tested
    """Here I suppose that the first player, 1, is White and that 2 = Black"""
    n = len(board)
    if ">" in str_move:
        L = str_move.split(">")
        (a, b) = extract_pos(n, L[0]) #Initial position
        (x, y) = extract_pos(n, L[1]) #Final position
        
        if is_in_board(n , (a, b)) and is_in_board(n , (x, y)):
            if player == 1:
                if ((a - x) == 1) and (abs(b - y) <= 1) and (board[a][b] == "W") and (board[x][y] != "W"):
                    return True
                else:
                    return False
            elif player == 2:
                if ((x - a) == 1)and (abs(b - y) <= 1) and (board[a][b] == "B") and (board[x][y] != "B"):
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

    
def play_move(board : list[list[int]], move : tuple[tuple[int, int], tuple[int, int]], player : int) -> None: #Tested
    (initial, final) = move
    (a, b) = initial
    (x , y) = final
    if ((player == 1) and (board[a][b] == "W") and (board[x][y] != "W")) or ((player == 2) and (board[a][b] == "B") and (board[x][y] != "B")):
        board[x][y] = board[a][b]
        board[a][b] = "."

def main(n : int) -> None :
    board = init_board(n)
    player1 = 1
    player2 = 2
    round1 = 1
    round2 = 0
    player = 0
    while winner(board) == None:
        if round1 == 1:
            player = player1
            print_board(board)
            print(" ")
            print("Jouer 1, Blanc")
            str_move = input_move()
            while check_move(board, player, str_move) == False:
                print("Jouer 1, Blanc")
                str_move = input_move()
            L = str_move.split(">")
            part1 = L[0]
            part2 = L[1]
            move = (extract_pos(n, part1), extract_pos(n, part2))
            play_move(board, move, player)
            round1 = 0
            round2 = 1
        elif round2 == 1:
            player = player2
            print_board(board)
            print(" ")
            print("Jouer 2, Noir")
            str_move = input_move()
            while check_move(board, player, str_move) == False:
                print("Jouer 2, Noir")
                str_move = input_move()
            L = str_move.split(">")
            part1 = L[0]
            part2 = L[1]
            move = (extract_pos(n, part1), extract_pos(n, part2))
            play_move(board, move, player)
            round1 = 1
            round2 = 0
    if winner(board) == 1:
        print("Le jouer 1 (Blanc) a gagne")
    elif winner(board) == 2:
        print("Le jouer 2 (Noir) a gagne")
            
if __name__ == '__main__':
    n = int(input("Entrez la taille du tableau "))
    main(n)