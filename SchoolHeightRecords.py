class Student:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def new_record(self):
        return f"{self.name}, {self.height}"

All_Students = []

def add_student():
    name=input("请输入新学生的名字: ")
    height=input("请输入新学生的身高: "  )
    student=Student(name,height)
    All_Students.append(student)
    print('添加成功')

def display_students():
    # Function to print all students in a readable format
    print("所有学生名单:")
    for student in All_Students:
        print(student.new_record())

def find_student_height():
    name = input("请输入学生的名字: ")
    for student in All_Students:
        if student.name == name:
            print(f"学生 {student.name} 的身高是 {student.height}")
            break
        else:
            print("未找到该学生")

def remove_student():
    name = input("请输入要移除的学生名字: ")
    found = False
    for student in All_Students:
        if student.name == name:
            All_Students.remove(student)
            print(f"已移除学生：{name}")
            found = True
            break
    if not found:
        print("未找到该学生")

def main_menu():
    while True:
        print("\n欢迎来到学生身高记录管理系统")
        print("1 - 添加新学生")
        print("2 - 删除学生")
        print("3 - 查找学生身高")
        print("4 - 显示所有学生")
        print("5 - 退出程序并保存")
        choice = input("请选择一个操作 (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            find_student_height()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("退出程序。")
            break
        else:
            print("无效选择，请重试。")

if __name__ == "__main__":
    main_menu()


