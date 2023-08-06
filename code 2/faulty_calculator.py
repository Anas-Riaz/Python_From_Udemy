# faulty calculator which gives all correct answers except the following
#  45 * 3 = 555 , 56 + 9 = 77 , 56/6 = 4
#----------------------------------------------------------------------------#

inp_1 = int(input("Enter First Number : "))
inp_2 = input("Enter operator(+,-,*,/) : ")
inp_3 = int(input("Enter Second Number : ")) 
if inp_2 == "+" :
    if inp_1 == 56 and inp_3 == 9 :
        print(77)
    else :
        print("sum is", inp_1 + inp_3) 

elif inp_2 == "-" :
    print("difference is" , inp_1 - inp_3)

elif inp_2 == "*" :
    if inp_1 == 45 and inp_3 == 3 :
        print(555)
    else :
        print("Product is" , inp_1 * inp_3)

elif inp_2 == "/" :
    if inp_1 == 56 and inp_3 == 6 :
        print(4)
    else :
        print("your answer is ", inp_1 / inp_3)    
#----------------------------------------------------------------------------#            
    

# 45 * 3 = 555 , 56 + 9 = 77 , 56/6 = 4    