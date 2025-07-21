from random import randint


randomNumber = randint(1, 10)
guess=-1
attempts = 0




while(guess!=randomNumber and attempts < 7):

    guess = int(input("guess a number 1 through 10 "))
    attempts = attempts + 1

    if guess > randomNumber:
        print ("too high")
        

    elif guess < randomNumber:
        print ("too low")
      

    elif guess == randomNumber:
        print ("you guessed it")

if(attempts==7 and guess!=randomNumber):
    print("you ran out of tries")
    