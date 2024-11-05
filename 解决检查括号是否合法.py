def is_valid(s):
    if not s:
        return True

    # 循环检查是否含有相邻的匹配括号对
    brackets = ['[]', '{}', '()']
    while any(bracket in s for bracket in brackets):
        for bracket in brackets:
            s = s.replace(bracket, '')
    # 如果删除完后为空，则说明括号有效，否则无效
    return not s


a = input('输入一组括号: ')
print(is_valid(a))
