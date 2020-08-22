#  matrix creation
def matrix(mat_no):
    row, col = map(int, input().split())
    print(f"Enter{mat_no}matrix: ")
    matrx = []
    for i in range(row):
        temp = list(map(eval, input().split()))
        if len(temp) == col:
            matrx.append(temp)
        else:
            print("ERROR")
            break
    return matrx, row, col


#  matrix addition
def matrix_add():
    print("Enter size of first matrix: ", end="")
    matrix_a, a_row, a_col = matrix(" first ")
    print("Enter size of second matrix: ", end="")
    matrix_b, b_row, b_col = matrix(" second ")
    result = []
    if a_row == b_row and a_col == b_col:
        for i, j in zip(matrix_a, matrix_b):
            temp = []
            for k, l in zip(i, j):
                temp.append(k + l)
            result.append(temp)
        print("The result is: ")
        return mat_print(result)
    else:
        print("The operation cannot be performed.")


#  matrix multiplication with a number
def matrix_mul_const():
    print("Enter size of matrix: ")
    matrx, row, col = matrix(" ")
    result = []
    number = int(input("Enter constant: "))
    for i in matrx:
        temp = []
        for j in i:
            temp.append(j * number)
        result.append(temp)
    print("The result is: ")
    return mat_print(result)
            

#  printing elements of matrices
def mat_print(result):
    for i in result:
        temp = ''
        for j in i:
            temp += str(j) + " "
        print(temp)


#  multiplication of two matrices
def mat_mul():
    print("Enter size of first matrix: ")
    mat_a, row_a, col_a = matrix(" first ")
    print("Enter size of second matrix: ")
    mat_b, row_b, col_b = matrix(" second ")
    if col_a == row_b:
        result = []
        for i in range(row_a):
            temp = []
            for j in range(col_b):
                x = 0
                for k in range(row_b):
                    x += mat_a[i][k] * mat_b[k][j]
                temp.append(x)
            result.append(temp)
        print("The result is: ")
        return mat_print(result)
    else:
        print("The operation cannot be performed.")


def transpose():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    choice = int(input("Your choice: "))
    print("Enter matrix size: ")
    matrx, row, col = matrix(" ")
    if choice == 1:
        result = []
        for i in range(col):
            result.append([0 for i in range(row)])
        for i in range(row):
            for j in range(col):
                result[j][i] = matrx[i][j]
        print("The result is: ")
        return mat_print(result)
    elif choice == 2:
        result =[]
        for i in range(col - 1, -1, -1):
            temp = ''
            for j in range(row):
                temp += str(matrx[j][i]) + " "
            temp = map(eval, temp.split())
            temp = list(temp)
            result.append(temp[::-1])
        print("The result is: ")
        return mat_print(result)
    elif choice == 4:
        result = []
        for i in range(row - 1, -1, -1):
            result.append(matrx[i])
        print("The result is: ")
        return mat_print(result)
    elif choice == 3:
        result = []
        for i in matrx:
            result.append(i[::-1])
        print("The result is: ")
        return mat_print(result)
            
  
def det(matrix):
    if len(matrix) == 2:
        if len(matrix) == len(matrix[0]):
            return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    elif len(matrix) == 1:
        return matrix[0][0]
    else:
        answer = 0
        for i in range(len(matrix[0])):
            new_mat = []
            for j in range(len(matrix[0])):
                temp = []
                for k in range(len(matrix[0])):
                    if j != 0 and k != i:
                        temp.append(matrix[j][k])
                if temp:
                    new_mat.append(temp)
            answer += matrix[0][i] * det(new_mat) * ((-1) ** i)
        return answer
  
  

def cofactor(matrix):
    if len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix[0]) == 2:
        return (matrix[1][1] * matrix[0][0]) - (matrix[1][0] * matrix[0][1])
    else:
        cofactor_matrix = []
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[i])):
                new_matrix = []
                for k in range(len(matrix)):
                    temp1 = []
                    for l in range(len(matrix[0])):
                        if k != i and l != j:
                            temp1.append(matrix[k][l])
                    if temp1:
                        new_matrix.append(temp1)
                temp.append(det(new_matrix) * ((-1) ** (i + j)))
            cofactor_matrix.append(temp)
        return cofactor_matrix  


def truncate(number):
    number = str(number)
    before, after = map(str, number.split("."))
    if len(after) >= 2:
        return float(before + "." + after[:2])
    else:
        return float(before + "." + after)
    
      
#  MAIN
while True:
    print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate the determinant
6. Inverse matrix
0. Exit''')
    choice = int(input("Your choice: "))
    if choice == 1:
        matrix_add()
    elif choice == 2:
        matrix_mul_const()
    elif choice == 3:
        mat_mul()
    elif choice == 4:
        transpose()
    elif choice == 5:
        print("Enter matrix size")
        matrx, row, col = matrix(" ")
        print("The result is: ")
        print(det(matrx))
    elif choice == 6:
        print("Enter matrix size")
        matrx, row, col = matrix(" ")
        if det(matrx) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            cofactor_mat = cofactor(matrx)
            det_number = det(matrx)
            result = []
            for i in cofactor_mat:
                temp = []
                for j in i:
                    if j * (1 / det_number) == -0.0:
                        temp.append(0)
                    else:
                        if "." in str(j * (1 / det_number)):
                            temp.append(truncate(j * (1 / det_number)))
                        else:
                            temp.append(j * (1 / det_number))
                result.append(temp)
            print("The result is: ")
            temp = []
            for i in range(col):
                temp.append([0 for i in range(row)])
            for i in range(row):
                for j in range(col):
                    temp[j][i] = result[i][j]       
            mat_print(temp)
    elif choice == 0:
        exit()
    else: 
        continue

