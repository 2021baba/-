import ast
def x(matrix1,matrix2):
    rows1 = len(matrix1)
    rows2 = len(matrix2)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    transposed = [[0] * rows1 for _ in range(cols2)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                transposed[i][j] += matrix1[i][k] * matrix2[k][j]
    print(transposed)


lit1 = str(input('请输入一个嵌套列表如[[1,2], [3,4], [5,6]]'))
lit2 = str(input('请输入一个嵌套列表如[[1,2], [3,4], [5,6]]'))
matrix1 = ast.literal_eval(lit1)
matrix2 = ast.literal_eval(lit2)
x(matrix1,matrix2)