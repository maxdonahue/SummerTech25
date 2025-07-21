
# for i in range(10):
#     for number in range(1, 11):
#         print(number, end="")
#     print()
# for i in range (10):
#     for j in range (1,11):
#         print("* ", end="")
#     print()



# for i in range (3):
#     for j in range(i+1):
#         print ("* ", end="")
#     print("")

for i in range (3):
    for j in range (3-i-1):
        print(" ", end="")
    for k in range (i +1):
        print ("* ", end="")
    print()


for i in range (3):
    for j in range (i+1):
        print(" ", end="")
    for k in range (3-i-1):
        print ("* ", end="")
    print()