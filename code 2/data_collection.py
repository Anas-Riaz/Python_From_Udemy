
# Data collection 
# ---------------------------------------------------------------------------#
# 3 clients 
# harry , rohan , hammad
# 6 files
# write a function that when execute taken as input client name 
# def getdate ():
#      import datetime
#      return datetime.datetime.now()
# one more function to retrieve or food for any client
# ---------------------------------------------------------------------------#

def getdate ():
     import datetime
     return datetime.datetime.now()

def take (x) :
    if x == 1 :
        a =int (input("1 for food 2 for excersice : "))
        if a == 1 :
            add = str(input("your food :")) 
            with open("Anas_food.txt", "a") as e :
                e.write(str([str(getdate())]) + ":" + add +"\n")
                print("successfully written !")
                
        elif a == 2 :
            add = str(input("for exercise : "))
            with open("Anas_exercise.txt", "a") as e:
                e.write(str([str(getdate())]) + ":" + add + "\n")
                print("successfully written !")
    
    elif x == 2 :
        a = int(input("1 for food 2 for excersice : "))
        if a == 1:
            add = str(input("your food : "))
            with open("Arqam_food.txt", "a") as e:
                e.write(str([str(getdate())]) + ":" + add + "\n")
                print("successfully written ! ")

        elif a == 2:
            add = str(input("for exercise : "))
            with open("Arqam_exercise.txt", "a") as e:
                e.write(str([str(getdate())]) + ":" + add +"\n")
                print("successfully written !")
    elif x ==3 :
        a = int(input("1 for food 2 for excersice : "))
        if a == 1:
            add = str(input("your food : "))
            with open("Abdur_rehman_food.txt", "a") as e:
                e.write(str([str(getdate())]) + ":" + add + "\n")
                print("successfully written !")

        elif a == 2:
            add = str(input("for exercise : "))
            with open("Abdur_rehman_exercise.txt", "a") as e:
                e.write(str([str(getdate())]) + ":" + add +"\n")
                print("successfully written !")
    
    else :
        print ("invalid input \n please enter valid input : ")
        

def retrieve (x):
    if x == 1:
        a = int(input("1 for food 2 for excersice : "))
        if a == 1:
            with open("Anas_food.txt") as e:
                for i in e :
                    print(i , end="")
                
        elif a == 2:
            with open("Anas_exercise.txt") as e:
                for i in e:
                    print(i , end="")

    elif x == 2:
        a = int(input("1 for food 2 for excersice : "))
        if a == 1:
            with open("Arqam_food.txt") as e:
                for i in e:
                    print(i , end="")

        elif a == 2:
            with open("Arqam_exercise.txt") as e:
                for i in e:
                    print(i , end="")
                    
    elif x == 3:
        a = int(input("1 for food 2 for excersice : "))
        if a == 1:
            with open("Abdur_rehman_food.txt") as e:
                for i in e:
                    print(i , end="")

        elif a == 2:
            with open("Abdur_rehman_exercise.txt") as e:
                for i in e :
                    print(i , end="")

    else:
        print("invalid input \n please enter valid input : ")
# ---------------------------------------------------------------------------#

print ("Data collection \n")
h = int(input("1 for log or 2 for retrieve : "))
if h == 1 :
    n = int(input("1 for Anas ,2 for Arqam ,3 for Abdur_rehman : "))
    take(n)    

if h == 2:
    n = int(input("1 for Anas ,2 for Arqam ,3 for Abdur_rehman : "))
    retrieve(n)

# ---------------------------------------------------------------------------#      
