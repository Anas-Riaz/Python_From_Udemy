def gauss_matrix(nr):
    j = 0
    m = []
    while j < nr:
        i = 0
        k = []
        while i < nr + 1:
            if i == nr:
                a = float(input(f"Enter Augmented Matrix Coefficient {j+1}: "))
                k.append(a)
            else:
                a = float(input(f"Enter value of A{j+1}{i+1}: "))
                k.append(a)
            i += 1
        m.append(k)
        j += 1
    print()

    # ------    PRINT   -------
    # m = [[5, 6, 3, 3], [2, -3, -8, 5], [3, 4, 4, 7]]
    print("The Augmented Matrix")
    print("=" * 20)
    col_width = max(len(str(value)) for row in m for value in row) + 2
    for i in range(nr):
        for j in range(nr + 1):
            if j == nr - 1:
                print("".join(str(m[i][j]).ljust(col_width)), sep="\t", end="|")
                print(end="\t")
            else:
                print("".join(str(m[i][j]).ljust(col_width)), end="\t")
        print()
    print()
    return m


def interchange(a, b, m):
    m[a], m[b] = m[b], m[a]
    return m


def subtracting(a, b, m):
    for i in range(len(m[a])):
        m[a][i] -= m[b][i]
    return m


def multiply(a, b, m):
    for i in range(len(m[a])):
        m[a][i] *= b
    return m


def multiply_sub(c, a, b, m):
    m = multiply(a, c, m)
    m = subtracting(b, a, m)
    return m


def gauss_jordan():
    n = int(input("Enter the dimension of square matrix: "))
    m = gauss_matrix(n)
    z = 1
    ans = "y"
    while ans == "y":
        print("Enter the value which you want to make ONE")
        print()
        row = int(input("Enter the row no. : ")) - 1
        column = int(input("Enter the column no. : ")) - 1
        print()

        pivot = m[row][column]

        if pivot == 0:
            print("Can't solve b/c PIVOT is ZERO")
            return None

        m = interchange(0, row, m)
        m = multiply(0, 1 / pivot, m)

        for j in range(1, n):
            m1 = list(m[0])
            next_value = m[j][column]
            if next_value != 0:
                m = multiply_sub(next_value, 0, j, m)
            m[0] = m1

        m = interchange(0, row, m)

        print(f"STEP {z}")
        print("=" * 20)
        col_width = max(len(str(value)) for row in m for value in row) + 2
        for i in range(n):
            for j in range(n + 1):
                if j == n - 1:
                    print("".join(str(m[i][j]).ljust(col_width)), sep="\t", end="|")
                    print(end="\t")
                else:
                    print("".join(str(m[i][j]).ljust(col_width)), end="\t")
            print()
        print()

        if z >= n:
            ans = input("Would you still like to do some changes? (Y/N): ").lower()
            while ans != "y" and ans != "n":
                print("Please select a valid option")
                ans = input("Would you still like to do some changes? (Y/N): ").lower()

        z += 1
    for i in range(n):
        print(f"X{i + 1}: {m[i][-1]}")


gauss_jordan()
