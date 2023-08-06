
NoOfColumns = int(input("Enter no. of columns : "))
NoOfRows = int(input("Enter no. of rows : "))
m = []
for i in range(NoOfRows):
    k = []
    for j in range(NoOfColumns):
        value = float(input(f"Enter element {i + 1}{j + 1} : "))
        k.append(value)
    m.append(k)



def display():
    print("=" * 40)
    for row in range(NoOfRows):
        for c in range(NoOfColumns):
            print("%7.3f" % m[row][c], end="\t")
        print()
    print("=" * 40)

display()

PivotRow = int(input("Enter the number of row : "))
PivotColumn = int(input("Enter the number of column : "))
PivotRow -= 1
PivotColumn -= 1

while PivotColumn >= 0 and PivotRow >= 0:
    pivot_element = m[PivotRow][PivotColumn]
    for col in range(NoOfRows):  # for col in range(nr):
        m[col][PivotColumn] /= pivot_element     # m[col][pc] /= pivot_element

    display()

    for row in range(NoOfColumns):  # range(nc)
        if row != PivotRow:
            const = m[row][PivotColumn]
            for col in range(NoOfColumns):
                m[row][col] = m[row][col] - const * m[PivotRow][col]

    display()
    PivotRow = int(input("Enter the number of row : "))
    PivotColumn = int(input("Enter the number of column : "))
    PivotRow -= 1
    PivotColumn -= 1
