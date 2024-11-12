from types import new_class

members = {
    1 :{'name':'白月黑羽', 'level':3, 'coins':300},
    2 :{'name':'短笛魔王', 'level':5, 'coins':330},
    3 :{'name':'紫气一元', 'level':6, 'coins':340},
    4 :{'name':'拜月主',   'level':3, 'coins':32200},
    5 :{'name':'诸法空',   'level':4, 'coins':330},
    6 :{'name':'暗光城主', 'level':3, 'coins':320},
    7 :{'name':'心魔尊',   'level':3, 'coins':2300},
    8 :{'name':'日月童子', 'level':8, 'coins':3450},
    9 :{'name':'不死尸王', 'level':3, 'coins':324},
    10:{'name':'天池剑尊', 'level':9, 'coins':13100},
}

print('请选择操作选项\n'
    '   1.查看用户账号信息\n'
    '   2.添加用户\n'
    '   3.删除用户\n'
    '   4.列出所有用户信息\n'
    '   0.提出')

def find_member_by_name(search_name):
    for member_id, info in members.items():
        if info['name'] == search_name:
            return member_id,info   # 返回包含level和coins的字典
    return "没有找到该成员"

def check_member_by_name(search_name):
    for member_id, info in members.items():
        if info['name'] == search_name:
            return False   # 返回包含level和coins的字典
    print('账号已存在')
    return True

num = int(input())
if num == 0:
    pass
if num ==1:
    name = input('请输入账号名')
    result = find_member_by_name(name)
    print(f"ID:{result[0]},{result[1]}")
if num ==2:
    new_name = input('输入账号名、等级、金币数量')
    if check_member_by_name(new_name[0]):
        members.update({new_name[0]:{'name':new_name[0],'level':new_name[1],'coins':new_name[2]}})
        print(members)