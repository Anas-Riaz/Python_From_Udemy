a = int(input("enter number of rows you want to print : ")) 
b = int(input("enter value 0 or 1 : "))
if b == 1 :
    for i in range (0, a+1):
        print ("*" *i)
 
if b == 0 :
    for i in range(a , 0,-1) : 
        print("*" *i) 

# a = int(input())
# n = 1

# while n <= a:
#     print("*"*n)
#     n += 1

# print(" thanks")
