class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2
    
    def is_square(self):
        return self.width == self.height
    
Rec1 = Rectangle(5, 10)
print("-----Rectangle1-----")
print(Rec1.area())
print(Rec1.perimeter())

Rec2 = Rectangle(7, 7)
print("-----Rectangle2-----")
print(Rec2.is_square())

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

Sq1 = Square(5)
print("-----Square1-----")
print(Sq1.area())
print(Sq1.perimeter())
print(Sq1.is_square())

