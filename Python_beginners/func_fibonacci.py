def fibonacci(n: int) -> int:
    """
    Return the `n`th fibonacci number, for positive `n` .

    :param n:
    :return:
    """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


a = int(input("Enter number: "))
answer = fibonacci(a)
print(answer)

