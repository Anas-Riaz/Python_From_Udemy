
import time 

initial = time.time()

for i in range (10) :
    print ("executed")

print("time after for loop" , time.time() - initial)

initial2 = time.time()  

x = 0 
while (x < 10) :
    print("executed")
    x += 1

print("time after while loop",time.time() - initial2)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

d = 0
while d<1000 :
    a = time.time()
    print(a)
    d+=1


