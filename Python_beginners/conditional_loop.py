available_List = ["north", "south", "east", "west"]

ChosenExit = ""
while ChosenExit not in available_List:
    ChosenExit = input("please choose a direction : ")
    if ChosenExit.casefold() == "quit":
        print("Game over")
        break

else:
    print("I am glad to made out form there. ")
