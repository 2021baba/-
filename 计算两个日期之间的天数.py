def sum_days(a):
    year,month,day = a.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    sum_days = 0
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:#判断是否是闰年
        days[1] = 29
    for i in range (month-1):
        sum_days = sum_days + days[i]
    sum_days += day
    return (sum_days)


def newyearsday(a):
    year, month, day = a.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    sum_days = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    alldays = 365
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # 判断是否是闰年
        days[1] = 29
        alldays = 366
    for i in range(month - 1):
        sum_days = sum_days + days[i]
    sum_days += day
    m = alldays-sum_days
    return (m)

def center(a,b):
    year_a, month_a, day_a = a.split('-')
    year_a = int(year_a)
    month_a = int(month_a)
    day_a = int(day_a)

    year_b, month_b, day_b = b.split('-')
    year_b = int(year_b)
    month_b = int(month_b)
    day_b = int(day_b)
    if year_a == year_b:
        sum_years = 0
        a = sum_days(Day1)
        b = sum_days(Day2)
        sum_day = b - a
        print(sum_day)

    else:
        for year in range(year_a, year_b+1):
            sum_years = 0
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # 判断是否是闰年
                days = 366
            else:
                days = 365
            sum_years += days
            a = sum_days(Day2)

            b = newyearsday(Day1)

            sum = a + b + sum_years
        print(sum_years)







Day1 = input('输入日期,如“2019-01-12”')
Day2 = input('输入日期,如“2019-01-12”')
# print(sum_days(Day1))
# print(newyearsday(Day1))
center(Day1,Day2)