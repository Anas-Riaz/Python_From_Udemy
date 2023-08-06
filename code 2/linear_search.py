# a = [12, 34, 56, 50, 78, 90, 56]
# n = len(a)
# v = int(input("Enter the value you want to search: "))
# f = "n"
# for i in range(n):
#     if a[i] == v:
#         f = "y"
#         break
# if f == "y":
#     print(f"The number is found at position: {i+1}.")
# else:
#     print("Number not found.")
    


# ========================================== Linear search ============================================#

a = [64, 35, 1, 2, 49, 4, 580, 46, 18, 6, 78] 
num = int(input("Enter number you want to search : "))
x = "n"
for i in range(len(a)) :
    if a[i] == num :
        x = "y"
        break

if x == "y" :
    print(f"The number position at: {i+1}")
else :
    print("Number not found.")