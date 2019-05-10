class Shape:
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, pri):
        self.side += pri

squ = Square(4)
squ.what_am_i()
req = Rectangle(3,4)
req.what_am_i()
