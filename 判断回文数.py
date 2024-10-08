number = int(input('请输入一个五位数: '))
if number - 10000 < 0 or number - 99999 > 0:#判断是否为五位数
    print('输入错误')
number = str(number)
if number[0] == number[4] and number[1] == number[3]:#判断是否是回文数
    print('是回文数')
else:
    print('不是回文数')