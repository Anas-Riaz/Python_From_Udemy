numbers = (0, 1, 2, 3, 4, 5)


# will print tuple
# print(numbers)
# will print numbers(tuple) value separately means we are providing single value at a time like numbers[0] ,numbers[1]
# print(*numbers)
# above statement print like the below statement
# print(0, 1, 2, 3, 4, 5)


def test_star(*args):
    # here args contain packed tuple
    print(args)
    # (0, 1, 2, 3, 4, 5)
    for x in args:
        print(x)
    # x is iterating through args


test_star(0, 1, 2, 3, 4, 5)
