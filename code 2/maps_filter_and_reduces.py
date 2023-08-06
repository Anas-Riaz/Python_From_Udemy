# ================================     Map     ========================================== #

# a = ["30", "10", "20", "5"]

# for i in range(4) :
#     a[i] = int(a[i])
#     a[i] = a[i] + 1
#     print(a[i])

# a = ["30", "10", "20", "5"]

# a = list(map(int,a))
# a[1] = a[1] + 2
# print(a[1])

# =================================      Filter     =====================================   #

# b = [1,2,3,4,5,6,7,8,9]

# def greaterthan_5 (num):
#     return num > 5

# greater_than = list(filter(greaterthan_5, b))
# print(greater_than)

# ================================      reduce      ===================================    #


from functools import reduce

list1 = [1,2,3,4]
number = reduce(lambda x,y : x + y , list1)
print(number)