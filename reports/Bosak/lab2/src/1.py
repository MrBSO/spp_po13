class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def is_square(self):
        return self.a == self.b
    
    def exists(self):
        return self.a > 0 and self.b > 0
    
    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"
    
    def __eq__(self, other):
        return self.area() == other.area()

print("Введите стороны прямоугольника:")
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))

r = Rectangle(a, b)
print(r)
print(f"Площадь: {r.area()}")
print(f"Периметр: {r.perimeter()}")
print(f"Квадрат? {r.is_square()}")
print(f"Существует? {r.exists()}")

r2 = Rectangle(5, 5)
print(f"\nРавны ли прямоугольники по площади? {r == r2}")