list1 = ["cakes", "chocolates", "pan cakes"]
print(list1)
print(id(list1))

list2 = list1
print(id(list2))

list1 += ["cookies"]
print(list1)
print(id(list1))
print(id(list2))

# -----------------------------------------------------------------------------

name = "ANAS"
print(name)
print(id(name))

temp = name
print(id(name))

name2 = " Riaz"
name += name2
print(name)
print(id(name))
