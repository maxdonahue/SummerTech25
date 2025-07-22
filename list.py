cart = []







print(cart)


while (True):
    userinput = input("Would you like [a] to add an item in your cart or [r] to remove.")



    if userinput == "a":
        item = input("What would you like to add?")
        cart.append(item)
        print(cart)
        
    elif userinput == "n":
        print("printing receipt")
        break
    elif userinput == "r":
        item = input("What item would you like to remove")
        cart.remove(item)
        print(cart)
    else:
        print("not an option")
        continue

    