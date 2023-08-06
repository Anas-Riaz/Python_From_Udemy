nR = int(input("Enter no. of rows : ")) #nR = no, of rows
nC = int(input("Enter no. of columnss : ")) #nR = no, of columns
m = []
j = 0
while j < nR:
    k = []
    i = 0
    while i < nC :
        a = int(input("ENTER no. :"))
        k.append(a)
        i+=1
    m.append(k)
    j+=1
print(m)
