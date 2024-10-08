user = input('请出石头、剪刀、布')
if user == '石头':
    print('你出石头')
    user = 1
elif user == '剪刀':
    print('你出剪刀')
    user = 2
elif user == '布':
    print('你出布')
    user = 3
else:
    print("输入错误")
import random
computer = random.randint(1,3)

#1表示拳头,2表示剪刀,3表示布
if computer == 1:#电脑拳头
    print("电脑出石头")
    if user == 1:
        print('平局')
    elif user == 3:
        print('你赢了')
    else:
        print('你输了')

if computer == 2:#电脑剪刀
    print('电脑出剪刀')
    if user == 2:
        print('平局')
    elif user == 1:
        print('你赢了')
    else:
        print('你输了')

if computer == 3:#电脑布
    print('电脑出布')
    if user == 3:
        print('平局')
    elif user == 2:
        print('你赢了')
    else:
        print('你输了')


