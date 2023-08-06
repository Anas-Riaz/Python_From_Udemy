# lambda function or annonymous function

# def add (a,b) :
#     return a+b
# print(add(4, 6))


# add = lambda x , y : x + y
# print(add(5 , 5))

# def list (a):
#     return a[1]
# a = [2,4,1,6,49,2,34,64]
# v.sort()
# print(list(a))

def a_t(a) :
   return a[1]

a = [[2, 4], [1, 6], [9, 2]]
# a.sort(key =lambda x : x[1])
a.sort (key=a_t)
print(a)