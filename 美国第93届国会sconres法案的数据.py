import json
import csv
import os
from calendar import month
from dataclasses import field
from itertools import count
month_count_1 = {}

for i in range(1,128):
    f = open(f'.//第9次作业素材//93//bills//sconres//法案{i}号//data.json')
    data = json.load(f)
    status_date = data['status_at']
    year, month, day = status_date.split('-')
    if month not in month_count_1:
        month_count_1[month] = 0

    month_count_1[month] += 1


for month, count in month_count_1.items():
    # print(f'{month}:{count}')
    pass

with open('status_at.csv', 'w', newline='') as file:
    fieldnames = ['month', 'count']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for month, count in month_count_1.items():
        writer.writerow({'month': month, 'count': count})

month_count_2 = {}
for i in range(1, 128):
    f = open(f'.//第9次作业素材//93//bills//sconres//法案{i}号//data.json')
    data = json.load(f)
    introduced_at_date = data['introduced_at']
    year, month, day = introduced_at_date.split('-')
    if month not in month_count_2:
        month_count_2[month] = 0

    month_count_2[month] += 1

for month, count in month_count_2.items():
    # print(f'{month}:{count}')
    pass

with open('introduced_at.csv', 'w', newline='') as file:
    fieldnames = ['month', 'count']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for month, count in month_count_2.items():
        writer.writerow({'month': month, 'count': count})

# print(os.listdir('.//第9次作业素材//93//bills//sconres'))
# for file in range(1,128):
#     os.rename(f'.//第9次作业素材//93//bills//sconres//sconres{file}', f'.//第9次作业素材//93//bills//sconres//法案{file}号')


