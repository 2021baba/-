
def Fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

num = int(input('Enter a number: '))
print(Fibonacci(num))
