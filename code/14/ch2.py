class Shape:
    def what_am_i(self):
        print("Я - фигура.")

class Square(Shape):
    square_list = []
    
    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, pri):
        self.side += pri

    def what_am_i(self):
        super().what_am_i()
        print("Я - квадрат.")

    def __repr__(self):
        return "{} на {} на {} на {}".format(self.side,
                                             self.side,
                                             self.side,
                                             self.side)


a_squ = Square(29)
print(Square.square_list)
b_squ = Square(93)
print(Square.square_list)
a_squ.what_am_i()
print(a_squ)
print(b_squ)

