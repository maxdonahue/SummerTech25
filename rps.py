#Rock, Paper, Scissor

from random import randint


while (True):

    print("rock paper scissors shoot")

    computor = randint(0,2)

    user = input("press [r] for rock, [p] for paper, [s] for scissor. ")

    # win check
    if computor == 0:
        if user == "p":
            print("you win computor chose rock")
        elif user == "s":
            print("you lose computor played rock") 
        elif user == "r":
            print("it's a tie computor chose rock")
        else:
            print("not an option")

    elif computor == 1:
        if user == "r":
            print ("you lose computor chose paper")
        elif user == "p":
            print("you tied computor chose paper")
        elif user == "s":
            print("you won computor chose scissor")

    elif computor == 2:
        if user == "r":
            print("you won computor chose scissors")
        elif user == "p":
            print("you lost")
        elif user == "s":
            print("you tied computor chose scissor")

    answer = input("Do you want to play more? y/n ")
    
    if answer == "y":
        continue
    elif answer == "n":
        break
    else:
        print("Invalid, shutting down game")
        break