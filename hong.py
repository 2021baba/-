import jieba
from collections import Counter
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


with open("C:\\Users\\zbddd\\Desktop\\ppt\\第11次作业素材\\红楼梦.txt", 'r', encoding='ANSI') as file:
    content = file.read()
jieba.load_userdict('C:\\Users\\zbddd\\Desktop\\ppt\\第11次作业素材\\字典.txt')
words = jieba.lcut(content)
word_count = Counter(words)


l = ['宝玉', '黛玉', '宝钗', '湘云', '凤姐', '李纨', '元春', '迎春', '探春', '惜春', '妙玉', '巧姐', '秦氏']
sorted_word_count = sorted(((word, word_count[word]) for word in l), key=lambda x: x[1], reverse=True)


with open('C:\\Users\\zbddd\\Desktop\\ppt\\第11次作业素材\\character_appearance.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['人物', '出场次数'])
    for word, count in sorted_word_count:
        writer.writerow([word, count])


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 8))
bars = plt.bar([x[0] for x in sorted_word_count], [x[1] for x in sorted_word_count], color='skyblue')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')
plt.xlabel('人物')
plt.ylabel('出场次数')
plt.title('《红楼梦》人物出场次数')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
