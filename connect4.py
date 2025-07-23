board = []
for i in range(6):
    slot = []
    for j in range(7):
        slot.append("[ ]")
    board.append(slot)

move = 0
player = ("[X]")
tracker = [5,5,5,5,5,5,5]

while (move<42):


    for i in range(6):
        for j in range(7):
            print(board[i][j], end="")
        print()

    col = int(input("What column would you like to put your peice in? "))
    row = tracker[col]
    board[row][col]=player
    tracker[col]=tracker[col]-1

    #check horizontaly
    for i in range(6):
        for j in range(4):
            if board[i][j] == player and board [i][j+1]==player and board [i][j+2]== player and board [i][j+3]== player :
                print(player,"wins")
                move=43
    
    #check vertically
    for i in range(6):
        for j in range(4):
            if board[j][i] == player and board [j+1][i] == player and board [j+2][i] == player and board [j+3][i] == player:
                print(player,"wins")
                move=43

