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

    def change_size(self, pri):
        self.side += pri

squ = Square(100)
print(squ.side)
squ.change_size(-50)
print(squ.side)
