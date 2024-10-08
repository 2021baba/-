year = int(input('请输入年份: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:#判断是否是闰年
    print(f'{year}年是润年')
else:
    print(f'{year}年不是润年')

