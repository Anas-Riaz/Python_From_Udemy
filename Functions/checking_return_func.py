# def add(a, b):
#     sum1 = a + b
#     return
#
#
# ans = add(3, 5)
# print(ans)
#

def sum_eo(n, t):
    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

ans = sum_eo(10, 'o')
print(ans)