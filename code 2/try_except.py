a = input("ENTER NUMBER : ")
b = input("ENTER NUMBER : ")
try :
    print("the sum of the numbers is" ,
          int(a)+int(b))

except Exception as e:
    print(e)
else:
    print("this msg is else ")
finally:
    print("this msg is final")
print("this line is very important")