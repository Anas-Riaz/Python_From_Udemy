# formatting string through different method

# a = "Anas"
# # b = "this is %s" %av
# # print(b)
# x = "Hello"
# comma = ","
# # b = "{} {}this is {} "
# # c  = b.format(x ,comma ,a)
# # print(c)

# b = f" {x} {comma} this is {a}"
# print(b)

# -------------------------------------------------------------------------------------#

#                                 join function                                        #

a = ["Anas","Arqam","Abdur rehman","Ashir","Huzaifa"]

# for i in a :
#     print(i,"and",end="")
    
c = ", ".join(a)
print (c)     