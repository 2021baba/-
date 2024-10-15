m = int(input("请输入第m年: "))
n = int(input("请输入第n年: "))
sum = 0
for year in range(m,n+1):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # 判断是否是闰年
        days = 366
    else:
        days = 365
    sum += days
print(sum)