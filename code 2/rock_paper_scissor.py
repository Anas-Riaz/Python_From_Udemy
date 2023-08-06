# rock , paper , scissor
# while loops
# 10 rounds
# print how many rounds user or computer win or lose
#--------------------------------------------------------------------------#

import random
print("\nMini game \nrock, paper, scissor \n")
print("total attempts 10 \n")
print("Use (r) for rock, (p) for paper, (s) for scissor\n")

i = 0
win = 0
lost = 0
draw = 0
attempt = 1

while i < 10 :
    user = input("Enter r , p ,s : ")
    
    val = ["rock" , "paper", "scissor"]
    choice = random.choice(val)
    
    if  choice == "rock" :
        print("\ncomputer choice", choice)
        
        if user == "r" :
            print("\nIt's a draw \n ")
            draw += 1
        elif user == "p" : 
            print("\nyou win \n ") 
            win += 1
        elif user == "s" :
            print("\nyou lose \n")
            lost += 1
        else:
            print("you have entered wrong input \n")
    
    elif choice == "paper" :
        print("\ncomputer choice", choice)
        
        if user == "r" :
            print("\nyou lose \n")
            lost += 1
        elif user == "p" :
            print("\nIt's a draw \n")
            draw += 1
        elif user == "s" :
            print("\nyou win \n")
            win += 1
        else : 
            print("you have entered wrong input \n")    
    
    else :
        print("\ncomputer choice", choice)
        
        if  user == "r" :
            print("you win \n")
            win += 1
        elif user == "p":
            print("you lose \n")
            lost += 1
        elif user == "s":
            print("It's a draw \n")
            draw += 1
        else:
            print("you have entered wrong input \n")        
            
    print("total attempts",attempt)
    attempt += 1
    if attempt == 11 :
        print("Finished \n")
        
    i += 1
    if i == 10 :
        if win > lost :
            print("Winner \nYou Won",win,"rounds\n","You lost",lost,"rounds\n","draw", draw,"rounds")
        elif lost > win :
            print("loser ,\nYou Lose",lost,"rounds\n","You Won",win,"rounds\n","draws",draw,"rounds")
        else : 
            print("game tie \ndraws",draw,"rounds\n","You Lose",lost,"rounds\n","You Won",win,"rounds")    
    
                
