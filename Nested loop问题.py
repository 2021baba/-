n = int(input('输入一个奇数: '))
if n % 2 == 0:
    print('输入错误,输入一个奇数')
else:
    line = int((n-1)/2)
    for i in range(1,line+2):
        num_b =int(i*2-1)
        num_a =int((n-num_b)/2)
        print(f"{' '*num_a+'*'*num_b}")
    for i in range(line,0,-1):
        num_b =int(i*2-1)
        num_a =int((n-num_b)/2)
        print(f"{' '*num_a+'*'*num_b}")
