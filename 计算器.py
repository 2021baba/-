import sys
a=input('请输入一个数字：')
b=input('请输入一个数字：')
do=input('请输入运算方式（+,-,*,/）：')
try:
    a=eval(a)
    b=eval(b)
except NameError:
    print('你输入的不是数字')
    sys.exit()
except:
    print('其他错误')
    sys.exit()
if do=='+':
    print(a+b)
elif do=='-':
    print(a-b)
elif do=='*':
    print(a*b)
elif do=='/':
    try:
        c=a/b
    except ZeroDivisionError:
        print('除数不能为0')
        sys.exit()
    else:
        a=eval(a)
        b=eval(b)
        print(a/b)
else:
    print('其他错误')


