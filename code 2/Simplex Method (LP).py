def matrix(nr,nc):
    m = []
    for r in range(nr):
        l = []
        for c in range(nc):
            elem = float(input(f"Input Element {r+1},{c+1}: "))
            l.append(elem)
        m.append(l)
    return(m)

def display_matrix(m):
    nr = len(m)
    nc = len(m[0])
    for r in range(nr):
        for c in range(nc):
            print("%5.3f" % (m[r][c]) , end = '\t')
        print()
    print('-'*60)    

def makepivotelementone(m,pr,pc):
    nc = len(m[0])
    PivotElement = m[pr][pc]
    for c in range(nc):
        m[pr][c] = m[pr][c] / PivotElement

def makepivotcolumnzero(m,pr,pc):
    nr = len(m)
    nc = len(m[0])
    for r in range(nr):
        if r != pr:
            constant = m[r][pc]    
            for c in range(nc):
                m[r][c] = m[r][c] - constant * m[pr][c]    

##---------------- Additional Functions For Simplex--------------

def ColumnIndexOfMostNegative(m):
    nc = len(m[0])
    mostnegative = m[0][0]
    negativeindex = 0
    for c in range(nc-1):
        if m[0][c] < mostnegative:
            mostnegative = m[0][c]
            negativeindex = c
    if mostnegative < 0:
        return(negativeindex)
    else:
        return(-1)    

def RowIndexOfLeastRatio(m,pivotcolumn):
    nr = len(m)
    smallestratio = m[1][-1]/m[1][pivotcolumn]
    RowIndexOfLeastRatio = 1
    for i in range(1, nr):
        if smallestratio > (m[i][-1] / m[i][pivotcolumn]):
            smallestratio = m[i][-1] / m[i][pivotcolumn]
            RowIndexOfLeastRatio = i
    return(RowIndexOfLeastRatio)

##---------------------MAIN PROGRAM--------------------------------            
nr = int(input("Enter Number Of Rows: "))
nc = int(input("Enter Number Of Columns: "))

m = matrix(nr,nc)
display_matrix(m)



pivotcolumn = ColumnIndexOfMostNegative(m)
pivotrow = RowIndexOfLeastRatio(m,pivotcolumn)
user = int(input("Enter 0 To Stop/ Enter 1 to Carry On: "))
while user == 1:
    makepivotelementone(m,pivotrow,pivotcolumn)
    makepivotcolumnzero(m,pivotrow,pivotcolumn)
    display_matrix(m)
    pivotcolumn = ColumnIndexOfMostNegative(m)
    pivotrow = RowIndexOfLeastRatio(m,pivotcolumn)
    user = int(input("Enter 0 To Stop/ Enter 1 to Carry On: "))
else:
    print("PROGRAM ENDED")
