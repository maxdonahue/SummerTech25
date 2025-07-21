while(True):
    num1 = int(input("enter the first number "))
    num2 = int(input("enter the second number "))
    operation = input("enter the operation ")


    if operation == '+':
        print(num1 + num2)

    elif operation == "*":
        print(num1*num2)
            
    elif operation == "/":
        print(num1 / num2)

    elif operation == "-":
        print(num1 - num2)
    else:
        print("not an option")

    print("would you like to continue?")
    answer = input("yes or no?")
    if answer == "yes":
        continue
    elif answer == "no":
        break
    else:
        print("not an option. stopping calculator")
        break