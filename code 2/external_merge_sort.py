# listt1 = [4,3,2,8,62,76,24,8,]

# def External_merge_sot(list):
#     f1 = []
#     f2 = []
#     i = 0 
#     j  = 1 
#     while (True) :
#         if list[i] > list[j] :
#             f1.append(list[i])
#             i += 1
#         elif list[i] <= list[j] :
#             f2.append(list[j])
#             j += 1   

n = 28 
c = []
i = 1
while i <= n:
     
    if n % i == 0 :
        c.append(i)
    i += 1  
print(c)