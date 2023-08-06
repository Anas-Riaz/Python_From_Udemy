# fibonacci method
# index     1 2 3 4 5 6 7 8  ........ 
#           | | | | | | | |
# Example   0 1 1 2 3 5 8 13 ........ nth
# sum of last 2 numbers.

# a = int(input("Enter number : "))
# def fibonacci (x) :
#     if x == 1 :
#        return 0
#     elif x == 2:
#        return 1 
#     else : 
#         return fibonacci(x - 1) + fibonacci(x - 2)
    
# print(fibonacci(a))    

def factorial(num):
   if num == 0 :
      return 1
   elif num == 1 :
      return 1 
   else :
     return num * factorial(num -1)
  
a = int(input("enter number : ")) 
print(factorial(a))