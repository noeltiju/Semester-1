def scaling(row1,s):
    for i in range(len(row1)):
        row1[i] = row1[i]*s
    return row1

def adding(row1,row2):
    for i in range(len(row1)):
        row1[i] += row2[i]

    return row1

def row_reduction_algo(matrix,row,column):
    rows = len(matrix) ; columns = len(matrix[0])
    others = [i for i in range(rows) if i != row]
    element = matrix[row][column]

    if element!= 0:
        
        row_ = matrix[row].copy()
        matrix[row]  = scaling(row_,(1/element))

        for i in others:
            el = matrix[i][column]
            if el == 0:
                continue
            row2 = matrix[row].copy()
            row1 = matrix[i].copy()
            matrix[i] = adding(row1,scaling(row2,-el))
        pivots_rows[row]=1
        pivots_cols[column]=1

def main_algo(matrix):
    rows = len(matrix) ; columns = len(matrix[0])
    count = 0
    matrix.sort()
    for row in range(len(matrix)):

        for column in range(len(matrix[0])):
            if pivots_rows[row]!=1:
                row_reduction_algo(matrix,row,column)

            else:
                break

def columns(matrix):
    columns = [[]for i in range(len(matrix[0]))]
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            columns[col].append(matrix[row][col])

    return columns

def parametric_soln(matrix,cols,pivots_cols,pivots_rows):
    soln = dict()
    non_pivots = [i for i in range(len(pivots_cols)) if pivots_cols[i] == 0]
    for i in non_pivots:
        variable = f"x{i+1}"
        free_column = [0 for i in range(len(matrix[0]))]

        val = cols[i]
        
        count = 0
        for k in range(len(free_column)):
            if k not in non_pivots:
                free_column[k] = val[count]*(-1)
                count+=1

        free_column[i]=1

        soln[variable] = free_column

    if soln:
        return soln

def interchange(matrix):            
    matrix.sort(reverse = True)

def pivot_rows_maker(matrix,cols):
    pivots = [0 for i in matrix]
    for i in range(len(cols)):
        col = cols[i]
        index = 0
        for j in range(len(col)):
            element = col[j]
            if element == 1:
                index = j
                continue

            if element != 0:
                break

        else:

            pivots[index] = 1

    return pivots

def solution_printer_free(soln,n):
    for i in range(n):
        variable = "x" + str(i+1)
        if variable in soln:
            print(f"{variable} is free")
        
        else:
            print(f"{variable} = ",end="")
            free_variables = list(soln.keys())
            for free in free_variables:
                el = soln[free][i]
                print(f"{free}({el})",end=" ")
                if free != free_variables[-1]:
                    print("+",end=" ")
    
            print()

def solution_printer_fixed(soln,n):
    for i in range(n):
        variable = "x" + str(i+1)
        print(f"{variable} = 0")

def variables_set(n):
    v = []
    for i in range(n):
        variable = "x" + str(i+1)
        v.append(variable)

    return v
matrix=[]

with open("matrix.txt") as myfile:
    k = myfile.readlines()
    for i in k:
        if i != "":
            l = list(map(int,i.split()))
            matrix.append(l)

pivots_rows=[0 for i in range(len(matrix))]
pivots_cols=[0 for i in range(len(matrix[0]))]


main_algo(matrix)
interchange(matrix)
print("\nRREF of [A 0]: \n")
for i in matrix:
    for j in i:
        print(j,end="\t")

    print("|"+"0")
cols = columns(matrix)
pivots_rows = pivot_rows_maker(matrix,cols)


soln = parametric_soln(matrix,cols,pivots_cols,pivots_rows)
print("\nParametric Solution:\n")
v = variables_set(len(matrix[0]))
if soln:
    print(v,end=" = ")
    l = list(soln.keys())    
    for key in l:
        print(key,soln[key],end=" ")
        if key != l[-1]:
            print("+",end=" ")

    print()

else:
    print(v,end=" = ")
    print([0 for i in range(len(matrix[0]))])



print("\nGeneral Solution:\n")
if soln:    
    solution_printer_free(soln,len(matrix[0]))

else:
    solution_printer_fixed(soln,len(matrix[0]))

print()