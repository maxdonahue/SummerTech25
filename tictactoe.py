#list for board
board = []
for i in range (3):
    slot = []
    for j in range (3):
        slot.append("")
    board.append(slot)
    

move = 0

player = "X"
print(" " + board[0][0], "|", board[0][1] +  " | " , board[0][2])
print("---------")
print(" "+ board[1][0] + " | " + board[1][1] + " | " ,board[1][2])
print("---------")
print(" " + board[2][0] + " | " + board [2][1], "|", board[2][2])

print("lets start playing!!!!!!!")

while (move<9):
    
    row = int(input("Which row would you like to place your piece in? "))
    col = int(input ("Which column would you like to place your piece in? "))

    board[row][col]=player
    move = move+1
    

    #check horizontly
    if board[0][0]==player and board[0][1] == player and board [0][2] == player:
        print (player, "wins")
        break
    elif board[1][0]==player and board[1][1] == player and board [1][2] == player:
        print (player, "wins")
        break
    elif board[2][0] == player and board [2][1] == player and board [2][2] == player:
        print (player, "wins")
        break

    #check vertically
    elif board[0][0] == player and board [1][0] == player and board [2][0] == player:
        print (player, "wins")
        break
    elif board[0][1] == player and board [1][1] == player and board [2][1] == player:
        print (player, "wins")
        break
    elif board [0][2] == player and board [1][2] == player and board [2][2] == player:
        print (player, "wins")
        break

    #check diagonaly
    elif board [0][0] == player and board [1][1] == player and board [2][2] == player:
        print(player, "wins")
        break
    elif board [0][2] == player and board [1][1] == player and board [2][0] == player:
        print (player, "wins")
        break

    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    
    print(" " + board[0][0], "|", board[0][1] +  " | " , board[0][2])
    print("---------")
    print(" "+ board[1][0] + " | " + board[1][1] + " | " ,board[1][2])
    print("---------")
    print(" " + board[2][0] + " | " + board [2][1], "|", board[2][2])


if move == 9:
    print("Its a tie!")