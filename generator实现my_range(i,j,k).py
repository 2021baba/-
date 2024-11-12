

def my_range(start, end, step):
    while start < end:
        yield start
        start += step

# 打印 my_range 函数生成的值
for value in my_range(1, 10, 2):
    print(value)


generator = my_range(1, 10, 2)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

