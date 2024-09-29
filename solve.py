#输入ax^2+bx+c=0中的浮点数a、b和c。如果有解，打印出二元次方程的解，形如“x1=1,x2=3”。如果没有解，则打印“该方程无解”。
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
x1 = 0
x2 = 0
if a ==0:
    if b != 0:
        x1 = -c / b
        x2 = "不存在"
    else:
        x1 = "该方程无解"
        x2 = "该方程无解"
else:
    if b ** 2 - 4 * a * c < 0:
        x1 = ("不存在")
        x2 = ("不存在")
    elif b ** 2 - 4 * a * c == 0:
        x1 = (-b) / (2 * a)
        x2 = ("不存在")
    else:
        x1 = ((-b) + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = ((-b) - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f"x1={x1}, x2={x2}")
