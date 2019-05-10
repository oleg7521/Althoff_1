class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

rec = Rectangle(3, 4)
squ = Square(4)
print(rec.calculate_perimeter(), squ.calculate_perimeter())
