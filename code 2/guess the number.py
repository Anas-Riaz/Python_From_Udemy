# =========================================================================================== #
                                                                                               
# no. of attempt 9                                                                             
# print no. of guessess left                                                                   
# print no. of guessess he took to finish                                                      
# print "game over" if he did not guess the no. in given attempt                               
                                                                                               
# =========================================================================================== #

n = 23 
print ("you have 9 attemts \n\n your number is between 0- 30")
i = 0
a = 9
while i < 9 :
    num = int(input("Enter number : \n"))
    if num < n :
        print("Your guessed number is less than the hidden number \n")
    elif num > n :
        print("your guessed number is greater than the hidden number \n")   
    else :
        print("Congrats. Your hidden number is 15")      
    if num == n :
         print("You attempt the game in " , b)
         break
    b = a - 1
    print("Attempts left are " ,b )
    if b == 0 :
      print("Game over")
    a -= 1
    i += 1     

# ============================================================================================ #