global board
board =[[" "," "," "],[" "," "," "],[" "," "," "]]
player = "X"

'''
printing board
'''
def printBoard(board):
  for line in board:
    print(line)

'''
input
'''
def makeMove():
    global player
    x = int(input("\nPlayer " + player + ":\nenter x cordinate: "))
    y = int(input("enter y cordinate: "))

    while board[y][x] != " ":
        print("\nplease choose an empty space!!! ")
        x = int(input("Player " + player + ": \nenter x cordinate: "))
        y = int(input("enter y cordinate: "))

    if player == "X":
        board[y][x] = "X"
        player ="O"
    else:
        board[y][x] = "O"
        player ="X"
        
def tictac():
    printBoard(board)
    makeMove()
    isWin()


'''
 win?
''' 
def isWin():
    global player
    if player == "X":
      p = "O"
    else:
      p = "X"


    #row 
    for c in range(len(board)):
        win = True
        for r in range(len(board)):
            if board[c][r] != p:
                win = False
                break
        if win:
            return True


    #column 
    for c in range(len(board)):
        win = True
        for r in range(len(board)):
            if board[r][c] != p:
                win = False
                break
        if win:
            return True


    #diagonals 
    win = True
    for c in range(3):
        if board[c][c] != p:
            win = False
            break
    if win:
        return True

    win = True
    for r in range(len(board)):
        if board[r][len(board)-1-r] != p:
            win = False
            break
    if win:
        return True

    return False



def main():
    gamewon = False
    while gamewon == False:
      printBoard(board)
      makeMove()
      gamewon = isWin()
    print("\nGAME OVER!")
    printBoard(board)


main()
    