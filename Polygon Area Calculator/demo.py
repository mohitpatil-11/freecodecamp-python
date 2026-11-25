from calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect)
print("Area:", rect.get_area())
print("Perimeter:", rect.get_perimeter())
print("Diagonal:", rect.get_diagonal())
print("Picture:")
print(rect.get_picture())

rect.set_width(8)
rect.set_height(4)
print(rect)

sq = Square(3)
print(sq)
print("Area:", sq.get_area())
print("Picture:")
print(sq.get_picture())

sq.set_side(2)
print(sq)

big = Rectangle(60, 10)
print(big.get_picture())  # too big

small = Rectangle(3, 2)
print("Fits inside:", Rectangle(12, 6).get_amount_inside(small))
