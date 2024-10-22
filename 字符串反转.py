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

print(b)