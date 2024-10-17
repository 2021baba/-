def fun(a,b,c):
    print(a)
    print(b)
    print(c)

#函数的调用
fun(10,20,30)#函数调用时的参数传递,称为位置传参

lst=[11,22,33]
fun(*lst)#*将列表中的每个元素都转换为位置实参传入

fun(a=1,b=2,c=3)#关键字实参

dic={'a':111,'b':222,'c':333}
fun(**dic)#**将字典中的每个键值对都转换为关键字实参传入

def fun2(a,b=10):#b在函数的定义处,所以b是形参,而且进行了赋值,所以b为默认值形
    print(a)
    print(b)

def fun3(*args):#个数可变的位置形参
    print(args)

def fun4(**args2):#个数可变的关键字形参
    print(args2)

fun3(10,20,30)
fun4(a=10,b=20,c=30)#结果是字典

def fun5(a,b,c,d)
    print(a)
    print(b)
    print(c)
    print(d)

fun5(10,20,30,40)#位置实参传递
fun5(a=10,b=20,c=30,d=40)#关键字实参传递
fun(10,20,c=30,d=40)#位置实参传递+关键字实参传递
#在def时,b,c之间加*,*之后的只能使用关键字传递


