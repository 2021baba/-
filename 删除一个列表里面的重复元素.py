list_example = input("Enter a list: ").split(',') # 输入并按,分割
for i in range(len(list_example)-1, -1, -1):    # 逆序遍历
    if list_example.count(list_example[i]) > 1:  # 如果元素重复
        list_example.remove(list_example[i])     # 移除第一个出现的重复元素
print(list_example)
