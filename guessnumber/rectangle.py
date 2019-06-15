class Rectangle:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y)*2

    def getArea(self):
        return self.x * self.y

x = int(input('长为：'))
y = int(input('宽为：'))
r = Rectangle(x,y)
a = int(r.getArea())
b = int(r.getPeri())
print('面积为:%d'% a)
print('周长为:%d'% b)

