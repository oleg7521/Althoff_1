class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.height * self.base / 2

tri = Triangle(20, 30)
print(tri.area())

        
