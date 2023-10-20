class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return  2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
      # pic = '*' * self.width + '\n'
      # pic = pic * self.height
        pic = ""
        for _ in range(self.height):
            pic += "*" * self.width + "\n"
        return pic

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
       # return self.get_area() // ob.get_area()

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def __str__(self):
        return f'(Square(side= {self.width}))'

    def set_side(self, s):
        self.width = s
        self.height = s


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
