class Checker:
    def __init__(self,number):
        self.number = number

    def int(self):
        if type(self.number) == int:
            return True
        else:
            return False

    def prime(self):
        for i in range(2,self.number):
            if self.number % i == 0:
                return False
        return True

    def digits(self):
        if self.int:
            number = str(self.number)
            return len(number)
        else:
            return False

    def sum(self):
        total_sum = 0
        number = self.number
        while number > 0:
            # n % 10 获得最低位的数字
            total_sum += number % 10
            # n // 10 去掉最低位的数字
            number //= 10
        return total_sum

    def Print(self):
        print(f"{self.number:.2e}")
        print(f"{self.number:,}")

checker = Checker(73022222)
print(checker.int())
print(checker.prime())
print(checker.digits())
print(checker.sum())
checker.Print()