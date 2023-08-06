# ---------------------------------------------------------------------------------------------------
def Simple_Matrix_And_Labels():
    # -----------------------------------------------------------------------------------------
    no_of_rows = int(input("Enter number of Rows you want : "))
    no_of_columns = int(input("Enter number of Columns you want : "))
    print("Making Matrix ")            
    Matrix = []
    for i in range(no_of_rows):
        k = []
        for j in range(no_of_columns):
            value = float(input(f"Enter matrix element {i+1}{j+1} : "))
            k.append(value)
        Matrix.append(k)
    # -----------------------------------------------------------------------------------------
    ColumnLabels = []
    print("Enter Columns Labels ")
    for i in range(no_of_columns):
        LabelNo = str(input(f"Enter Column Label {i + 1} : ")) 
        ColumnLabels.append(LabelNo)
    # ------------------------------------------------------------------------------------------
    RowLabels = []    
    print("Enter Rows Labels ")
    for i in range(no_of_rows):
        LabelNo = str(input(f"Enter Row Label {i + 1} : ")) 
        RowLabels.append(LabelNo)    
    # --------------------------------------------------------------------------------------------
    return Matrix, RowLabels, ColumnLabels
# --------------------------------------------------------------------------------------------------- 
def Negative_smallest(Matrix):
    smallestvalue =  Matrix[0][0]
    index = 0 
    for i in range(1 , len(Matrix[0])):
        if Matrix[0][i] < smallestvalue :
            smallestvalue = Matrix[0][i]
            index = i
        
        if smallestvalue < 0 :
            return index
        else :
            return -1
# ---------------------------------------------------------------------------------------------------
def PivotElement_one (Matrix, PivotRow, PivotColumn):
    PivotElement = Matrix[PivotRow][PivotColumn]
    for i in range(len(Matrix[0])):
        Matrix[PivotRow][i] / PivotElement
    
    return Matrix    
# ---------------------------------------------------------------------------------------------------
def RemaingElement_Zero(Matrix, PivotRow, PivotColumn):
    for i in range(len(Matrix)) :
        if i != PivotRow:
            multiplier = Matrix[i][PivotColumn]
            for j in range(len(Matrix[0])):
                Matrix[i][j] -= (Matrix[PivotRow][j] * multiplier)
    
    return Matrix
# ---------------------------------------------------------------------------------------------------
def Smallest_positive(ratios) :
    smallestvalue = abs(ratios[0])
    index = 0 
    for i in range(1 , len(ratios[0])):
        if  smallestvalue > ratios[i] > 0 :
            smallestvalue = ratios[i]
            index = i
        
        if ratios[index] > 0 :
            return index + 1
        else :
            return -1
#----------------------------------------------------------------------------------------------------
def displaymatrix (Matrix, no_of_rows, no_of_columns) :                                                    
    print("="* 40)                                                                                      
    for row in range(no_of_rows):                                                                     
        for column in range(no_of_columns):                                                              
            print("%6.2f" % Matrix[row][column] , end = "\t" )                                          
        print()                                                                                       
# ---------------------------------------------------------------------------------------------------        
def Maximization ():        
    while(True):
        Matrix, row_labels, column_labels = Simple_Matrix_And_Labels() 
         
        pivot_column = Negative_smallest(Matrix[0])
        if pivot_column == -1 :
            break
        
        Ratios = []
        for i in range(len(Matrix)):
            ratio = Matrix[i][-1]/Matrix[i][pivot_column]
            Ratios.append(ratio) 
        
        pivot_row = Smallest_positive(Ratios)
        if pivot_row == -1 :
            break   
        
        Matrix = PivotElement_one(Matrix, pivot_row, pivot_column) 
        Matrix = RemaingElement_Zero(Matrix, pivot_row, pivot_column)
    return Matrix      
# ---------------------------------------------------------------------------------------------------
def displayprogram():
    print("=" * 30)
    
# ---------------------------------------------------------------------------------------------------
matrix = Maximization ()
print(matrix)