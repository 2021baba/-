year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
sum_days = 0
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:#判断是否是闰年
    days[1] = 29
for i in range (month-1):
    sum_days = sum_days + days[i]
sum_days += day
print(sum_days)