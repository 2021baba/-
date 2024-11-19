import csv
import json
import warnings
from os import write

file = open('stu.csv', 'w', encoding='UTF-8', newline='')
writer = csv.writer(file)
writer.writerow(['id','name','Chinese','Math','English'])

with open('.//第9次作业素材//stu.json', 'r',encoding='UTF-8') as f:
    data = json.load(f)
    for i in data:
        datai = [i]+data[i]
        print(datai)
        print(type(data))
        writer.writerow(datai)


file.close()
