# number = str(input("Please enter three number : "))
# list1 = number.split(",")
# int_list = []
# for item in list1:
#     int_list.append(int(item))
# add = 0
# for index, value in enumerate(int_list):
#     if index == 2:
#         add -= value
#     else:
#         add += value
# print(add)
#

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
print(a, b, c)
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)
