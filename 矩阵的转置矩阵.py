import ast  # 用于安全地解析输入字符串为列表


def t(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0] * rows for _ in range(cols)]


    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed



lit = input('请输入一个嵌套列表如[[1,2], [3,4], [5,6]]: ')
matrix = ast.literal_eval(lit)  # 将字符串转换为嵌套列表


print(t(matrix))
