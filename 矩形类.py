class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def judge(self):
        if self.width == self.height:
            return True
        else:
            return False

    def disjoint(self, B):
        """判断当前矩形与矩形B是否不相交"""
        # 两个矩形不相交的条件是其中一个矩形完全在另一个矩形的左边、右边、上面或下面
        if (self.x + self.width < B.x or self.x > B.x + B.width or
                self.y + self.height < B.y or self.y > B.y + B.height):
            return True
        return False


rectangle1 = Rectangle(5,5,(1,1),12)

print(rectangle1.width)
print(rectangle1.height)

print(rectangle1.judge())

rectangle2 = Rectangle(12,10,(1,1),12)

print(rectangle2.width)
print(rectangle2.height)

print(rectangle2.judge())