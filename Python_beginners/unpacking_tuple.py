data = 1, 3, 5, 6
a, b, c, d = data
print(a, b, c, d)

listed_data = [2, 4, 6]
x, y, z = listed_data
print(x)
print(y)
print(z)

# listed_data.append(1)
# x, y, z = listed_data
# print(x)
# print(y)
# print(z)

# unpacking a list leads you to crash your program unlike tuples because it can not be changed

# enumerate function return index and value in tuple

# for index , character in enumerate(abcdefgh"):
#   print(index, character)
for t in enumerate("abcdefgh"):
    print(t)
