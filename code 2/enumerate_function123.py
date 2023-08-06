

# x = [24,53,64,79,72]

# i = 1
# for item in x :
#     if i % 2 != 0 :
#         print(item)
#     i += 1

f = [ 24, 53, 64, 79, 72]
# enumerate starts with 0th index

for index,item in enumerate (f) :
    if index % 2 == 0:
        print(item)
