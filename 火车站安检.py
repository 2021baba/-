has_ticket = input('是否有车票')
if has_ticket == '有':
    has_ticket = 1
else:
    has_ticket = 0
has_ticket = bool(int(has_ticket))
if has_ticket == True:#判断是否有车票
    has_knife = input('是否有刀')
    if has_knife == '有':#判断是否有刀
        knife_length = int(input('请输入刀的长度'))
        if knife_length <= 20 and knife_length > 0:#判断刀长度是否有符合
            print('欢迎乘车')
        elif knife_length > 20:
            print('刀的长度过长，不允许进门')
        else:
            print('输入错误')
    elif has_knife == '无':
        print('欢迎乘车')
    else:
        print('输入错误')
elif has_ticket == False:
    print('没有车票，不允许进门')



