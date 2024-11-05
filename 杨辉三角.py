def triangle(n):
    if n == 1:
        print([1])
        return [1]
    else:
        prev_row = triangle(n - 1)  # 获取前一行的结果
        new_row = [1]  # 开始新的一行，并先添加一个1
        # 生成新行的中间部分
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)  # 添加最后一个1
        print(new_row)
        return new_row

numRows = int(input("Enter number of rows: "))
triangle(numRows)
