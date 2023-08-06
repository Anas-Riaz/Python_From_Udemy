# program to print all list element without spam

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

i = int(1)
for meals in menu:
    print("list{0} = ".format(i), meals)
    for item in meals:
        if item == "spam":
            continue

        print(item)
    i += 1
