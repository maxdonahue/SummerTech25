

def sum (x,y):
    print(x+y)

def product (x,y):
    print(x*y)

def quotient (x,y):
    print(x/y)

def diffrence (x,y):
    print(x-y)

while(True):

    num1 = int(input("What wll be your first number? "))
    num2 = int(input("What will be your second number?"))
    operation =input("What will be your operation?")

    if operation == "-":
        diffrence(num1,num2)
    elif operation == "+":
        sum(num1,num2)
    elif operation == "*":
        product(num1,num2)
    elif operation == "/":
        quotient(num1,num2)
    else:
        print("not an option")


    answer = input("do you want to continue?")

    if answer == "yes":
        continue
    elif answer == "no":
        break
    else:
        print("not an option.\n ending program...")
        break
