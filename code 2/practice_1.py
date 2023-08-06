# ========================================================================#

a = int(input("Enter no. of rows : "))
b = int(input("Enter 0 or 1 : "))
if b == 0:
     c = 0
     while c <a : 
        for i in range(0, a+1) :
            print(i*str(c))
            c += 1
           
if b == 1:
     v = 0
     while v < a : 
        for i in range(a,0, -1) :
            print(i*str(a))
            a -= 1
            v += 1 
            
            
# ======================================================================= #