year = int(input('请输入年份: '))
month = int(input('请输入月份'))
day = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:#判断是否是闰年
    day[1] = 29
    print(day[month - 1])
else:
    print(day[month-1])