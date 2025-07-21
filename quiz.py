score = 0
numberOfQuestions=3

print("What is 4 + 4 ")
print("6")
print("7")
print("2")
print("8")


answer = int(input("type your answer "))
if answer == 8:
    print("you are correct")
    score = score+1
elif answer== 6:
    print("You are incorrect")
elif answer == 7:
    print ("you are incorrect")
elif answer == 2 :
    print ("you are incorrect")
else:
    print ("not an option")


print ("what is 12 x 12")
print ("112")
print ("122")
print ("162")
print ("144")

answer = int(input("type your answer "))
if answer == 122:
    print ("you are incorrect")
elif answer == 112:
    print ("you are incorrect")
elif answer == 162:
    print ("you are incorrect")
elif answer == 144:
    print ("you are correct")
    score = score+1
else:
    print("that is not an option")


print ("what is 48 + 52")
print ("100")
print ("92")
print ("90")
print ("102")

answer = int(input("type you answer "))
if answer == 100:
    print ("you are correct")
    score = score+1
elif answer == 92:
    print ("you are incorrect")
elif answer == 90:
    print ("you are incorrect")
elif answer == 102:
    print ("you are incorrect")
else:
    print ("that is not an option")




print (" ")
print ("your score is",score, "out of", numberOfQuestions)
print (" ")
 
