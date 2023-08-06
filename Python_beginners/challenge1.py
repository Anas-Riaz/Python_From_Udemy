list1 = ["exit", "learn python", "learn java", "go swimming", "have dinner"]
choose_exit = ""
print("please choose your option from the list below.")
for i in range(len(list1)):
    print("{}. ".format(i) + list1[i])

while choose_exit not in list1:
    choose_exit = input("Enter the option. \n")
    if choose_exit == 0:
        print(choose_exit)
        break

    print(choose_exit)
