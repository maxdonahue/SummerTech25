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
row = int(input("Which row would you like to place your piece in? "))
col = int(input ("Which column would you like to place your piece in? "))

board[row][col]=player


print(" " + board[0][0], "|", board[0][1] +  " | " , board[0][2])
print("---------")
print(" "+ board[1][0] + " | " + board[1][1] + " | " ,board[1][2])
print("---------")
print(" " + board[2][0] + " | " + board [2][1], "|", board[2][2])

