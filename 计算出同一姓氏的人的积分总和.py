nameScoreAge = {
    '薛蟠': (4560, 42),
    '薛蝌': (4460, 25),
    '薛宝钗': (5776, 43),
    '薛宝琴': (4346, 42),
    '王夫人': (3360, 25),
    '王熙凤': (4460, 35),
    '王子腾': (5660, 45),
    '王仁': (5034, 65),
    '贾蓉': (3446, 15),
    '贾芹': (5663, 25),
    '贾兰': (3443, 35),
    '贾芸': (4522, 25),
    '尤三姐': (5905, 45),
    '尤二姐': (5324, 25),
    '贾珍': (4603, 25),
}

# 创建一个新的字典来存储每个姓氏的分数总和
surnameScores = {}

# 遍历原字典
for name, (score, age) in nameScoreAge.items():
    surname = name[0]  # 获取姓氏（名字的第一个字）
    if surname in surnameScores:
        surnameScores[surname] += score  # 累加分数
    else:
        surnameScores[surname] = score  # 初始化分数

# 将姓氏和对应分数放入列表
firstNameScore = []
for surname, total_score in surnameScores.items():
    firstNameScore.extend([surname, total_score])


print(firstNameScore)
