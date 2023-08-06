list1 = [[9,8,5],[7,1,2],[4,3,6]]
a = []
for i in range(len(list1)) :
    for j in range(len(list1[i])):
        s = list1[i][j]
        a.append(s)
a.sort()
print(a)
m = []
for g in range(3):
    k = []
    for h in range(len(a)):   
        if h <= 2:
            val = a[h]
            k.append(val)      
        elif h >= 3 and h <= 5 :
            val = a[h]
            k.append(val) 
        else:
            val = a[h]
            k.append(val)           
    m.append(k) 
print(m)