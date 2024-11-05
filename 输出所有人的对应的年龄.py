
# 输入：n个人，每个人年龄相差m岁。
# 输出：输出所有人的对应的年龄（从第1个人为10岁开始）
m = 0
def years(n):
    a = n

    if n == 1:
        print('第1个人年龄为10岁')
        return 10
    else:
        n = years(n-1) + m
        print(f'第{a}个人年龄为{n}岁')
        return n

n = int(input('多少个人: '))
if n == 1:
    print('第1个人年龄为10岁')
else:
    m = int(input('每个人年龄相差几岁'))
    years(n)
