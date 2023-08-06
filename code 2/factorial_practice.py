n = int(input("Enter number : "))
n_1 = int(n - 1) 
if n == 0 :
    print("The factorial of 0 is 1")
elif n < 0 :
    print("The factorial of numbers less than 0 (negative numers) doesnot exists")
else :        
    while n_1 > 0 :
        a = n
        n *= n_1
        n_1 -= 1
    print(n)    