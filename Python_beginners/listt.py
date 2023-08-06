# numbers = [1.3, 3.2, 2.21, 21.2, 1.2, 2.1]
# arrange = sorted(numbers)
# even = [0, 2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# new_list = even + odd
# new_list2 = odd + even
#
# more_numbers = list(new_list)
#
# slic = new_list[:]
# print(slic)

# min_value = 25
# max_value = 70
# data = [2, 5, 10, 11, 65, 45, 6, 7, 43, 4, 80, 14, 9, 77, 9, 97]
# data.sort()
# print(data)
# for index, value in enumerate(data):
#     if value >= min_value:
#         stop = index
#         break
# print(stop)
# del data[:stop]
# print(data)

# start = 0
# for index in range(len(data)-1, -1, -1):
#     if data[index] <= max_value:
#         start = index +1
#         break
# print(start)
# del data[start : ]
# print(data)


a = [1, 3, 4, 5, 6, "anas", 384.5]
b = a
print(a, "\t", b)
a[6] = "adding"
print(a, "\t", b)
del a[6]
print(a, "\t", b)

del b[1]
print(a, "\t", b)
