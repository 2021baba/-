from collections import Counter
import string


def most_wanted_letter(text):
    # 将所有字母转换为小写
    text = text.lower()

    # 使用列表解析保留字母，忽略其他符号
    letters = [char for char in text if char in string.ascii_lowercase]

    # 使用 Counter 统计每个字母的出现次数
    letter_counts = Counter(letters)

    # 找出出现次数最多的字母
    max_count = max(letter_counts.values())

    # 在所有最大值的字母中，选择字母表中最靠前的
    most_wanted = min([char for char, count in letter_counts.items() if count == max_count])

    return most_wanted


# 测试代码
text = input("请输入一段文本：")
result = most_wanted_letter(text)
print(f"出现最多的字母是：{result}")
