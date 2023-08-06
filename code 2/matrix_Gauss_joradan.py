def matrix(nR ,nC) : 
    m = []
    for i in range(nR) :
        k = []
        for j in range(nC) :
            a = int(input("\nEnter number : "))
            k.append(a)
        m.append(k)
    return(m)        

def inter_change (a, b, m) :
    m[a] , m[b] = m[b] , m[a]
    return m      

def adding(a, b, m) :
    for i in range(len(m[a])) :
        m[a][i] += m[b][i]
    return m


def subtracting(a, b, m):
    for i in range(len(m[a])):
        m[a][i] -= m[b][i]
    return m

def multiply (a, b, m) :
    for i in range (len(m[a])):
        m[a][i] *= b
    return m

if __name__ == '__main__' :
    nc = int(input("Enter number of columns : "))
    nr = int(input("Enter number of rows : "))
    mat = matrix(nr, nc)
    print(mat)
    
    for i in range(len(mat)):
         
        if mat[i][0] == 1:
            if mat[0][0] == 1:
                break
            else :
                row_1 = int(input("\nEnter number for 1st Row (For swaping) : "))
                row_2 = int(input("\nEnter number for 2nd Row (For swaping) : "))
                
                changing = inter_change(row_1,row_2,mat)
                print(changing)
                break

    while (True):
        list1 = ["a", "m", "s", "i"]
        user = input("Enter 'a' for addition \nEnter 's' for subtarction \nEnter 'm' for multiply \nEnter 'i' for interchange : ")

        if user == "a":
            add_row1 = int(input("\nEnter the row number to add : "))
            add_row2 = int(input("\nEnter the row number to add : "))
            add = adding(add_row1, add_row2, mat)
            print(add)
            print("*"*80)
            
        elif user == "s":
            subt_row1 = int(input("\nEnter the row number to subtract : "))
            subt_row2 = int(input("\nEnter the row number to subtract : "))
            sub = subtracting(subt_row1, subt_row2, mat)
            print(sub)
            print("*"*80)

        elif user == "m":
            multiply_row1 = int(input("\nEnter the row number to multiply : "))
            multiply_row2 = float(input("\nEnter the number to multiply :  "))
            product = multiply(multiply_row1, multiply_row2, mat)
            print(product)
            print("*"*80)

        elif user == "i":
            again_row_1 = int(input("\nEnter number for 1st Row : "))
            again_row_2 = int(input("\nEnter number for 2nd Row: "))
            change = inter_change(again_row_1, again_row_2, mat)
            print(change)
            print("*"*80)
        
        end = ["e", "c"]
        ending = input("\n Enter 'e' to end and 'c' to continue program : ")
        
        if ending == "c" :
            continue     
        elif ending == "end" :
            break    
