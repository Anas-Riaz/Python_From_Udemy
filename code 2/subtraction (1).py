# print("For 1st Matrix")
# nC1 = int(input("Enter no. of Columns: "))
# nR1 = int(input("Enter no. of Rows: "))
# a = 0
# m = []    # FINAL MATRIX
# while a < nR1:
#     i = 0
#     k = []
#     a += 1
#     while i < nC1:
#         b1 = float(input("Enter a number: "))
#         k.append(b1)
#         i += 1
#     m.append(k)
# print(m)

# print("For 2nd Matrix")
# nC2 = int(input("Enter no. of Columns: "))
# nR2 = int(input("Enter no. of Rows: "))
# a = 0
# n = []    # FINAL MATRIX
# while a < nR2:
#     i = 0
#     k = []
#     a += 1
#     while i < nC2:
#         b2 = float(input("Enter a number: "))
#         k.append(b2)
#         i += 1
#     n.append(k)
# print(n)

# result = []
# if nR1 == nR2 and nC1 == nC2:
#     i = 0
#     while i < nR1:
#         r = []
#         i += 1
#         j = 0
#         while j < nC1:
#             r.append(m[i][j] - n[i][j])
#             j += 1
#         result.append(r)
#     print(result)
# else:
#     print("Addition is not possible")

# ====================================================================================== #

print("for first matrix")

nC_1 = int(input("enter number of colomns you want : "))
nR_1 = int(input("enter number of rows you want : "))

final_matrix_1 = []
i = 0 
while i< nR_1 :
    j = 0 
    final_sub_matrix_1 = []
    while j < nC_1 :
        a = int(input("Enter number : "))
        final_sub_matrix_1.append(a)
        j += 1
    final_matrix_1.append(final_sub_matrix_1)
    i += 1
    
print(final_matrix_1)          

# ======================================================================================= #
print("="*20)
# ======================================================================================= #

print("for second matrix")

nC_2 = int(input("enter number of colomns you want : "))
nR_2 = int(input("enter number of rows you want : "))

final_matrix_2 = []
i = 0
while i < nR_2:
    j = 0
    final_sub_matrix_2 = []
    while j < nC_2:
        a = int(input("Enter number : "))
        final_sub_matrix_2.append(a)
        j += 1
    final_matrix_2.append(final_sub_matrix_2)
    i += 1

print(final_matrix_2)

# =============================[1, 2]===[1, 2]===================================== #
print("="*20)
# =============================[3, 4]===[3, 4]===================================== #

ans = []

if nR_1 == nR_2 and nC_1 == nR_2 :
    c = 0
    while c < nR_1 :
        d = 0
        g = []
        while d < nC_1 :
            x = final_matrix_1[c][d] - final_matrix_2[c][d]
            g.append(x)
            d += 1
        ans.append(g)
        c += 1 
    print(ans) 
else :
    print("subtraction not possible")        