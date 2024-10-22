a = input('请输入字符串')
stack=[]
i = 0
j = 0
while i < len(a):
    stack.append(a[i])
    i+=1
b = ''
while j < len(a):
    b = b + stack.pop()
    j+=1

if a==b:
    print('字符串为回文数')
else:
    print('字符串不为回文数')
