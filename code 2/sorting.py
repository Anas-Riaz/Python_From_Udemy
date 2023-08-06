a = [3, 8, 7, 6, 4, 1,5, 2, 9, 0]
# n = len(a)
# print(a)
# j = 0
# while j < n:
#     s = a[j]
#     p = j
#     i = j + 1
#     while i < n:
#         if a[i] < s:
#             s = a[i]
#             p = i
#         i += 1
#     t = a[j]
#     a[j] = a[p]
#     a[p] = t
#     j += 1
# print(a)

n = len(a)   # length = 10
print(a)     
j = 0 
while j < len(a) : 
    s = a[j]         # s = 9
    p = j            # p = 0 
    i = j + 1        # i = 1
    while i <len(a) :     
                          # first phase    seccond phase   .......
        if a[i] < s :     # 8 < 9  true    7 < 8           ....... 
            s = a[i]      # s = 8          s = 7           .......
            p = i         # p = 1          p = 2           .......
        i += 1            # i = 2          i = 3           .......
    
    t = a[j]              # t = a[0] = 9
    a[j] = a[p]           # a[0] = a[9]
    a[p] = t              # a[9] = 9
    j += 1                # j = 2
print(a)