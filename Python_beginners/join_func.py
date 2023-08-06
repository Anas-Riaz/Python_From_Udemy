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

for meals in menu:
    for index in range(len(meals) - 1, -1, -1):
        if meals[index] == "spam":
            del meals[index]
    print(", ".join(meals))
# Join function can iterate in list used  only for string literals