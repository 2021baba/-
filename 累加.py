n = int(input('Enter a number n: '))
sum = 0
for i in range(1,n+1):
    num = (-1) ** (i+1) * (1 / (2 * i - 1))
    sum += num
print(sum)