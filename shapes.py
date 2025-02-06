import math

# базовый класс shape
class Shape:
    def __init__(self, color=None, name='Фигура'):
        self.name = name
        self.color = color

    @property
    def area(self) -> float:
        raise NotImplementedError('метод определен в подклассах')

    def describe(self) -> str:
        return f'Это {self.name}, цвета {self.color}. Площадь этой фигуры {self.area:.2f}'


# подкласс круг
class Circle(Shape):
    def __init__(self, radius, color=None):
        super().__init__(color=color, name='круг')
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)


# подкласс прямоугольник
class Rectangle(Shape):
    def __init__(self, width, height, color=None):
        super().__init__(name='прямоугольник', color=color)
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height


# подкласс треугольник
class Triangle(Shape):
    def __init__(self, base, height, color=None):
        super().__init__(name='треугольник', color=color)
        self.base = base
        self.height = height

    @property
    def area(self) -> float:
        return self.base * self.height / 2


# подкласс прямоугольника - квадрат
class Square(Rectangle):
    def __init__(self, width, color=None):
        super().__init__(height=width, color=color, width=width)







if __name__ == '__main__':
    circle = Circle(5, 'green')
    print(circle.describe())

    rectangle = Rectangle(5, 2,'purple')
    print(rectangle.describe())

    triangle = Triangle(5, 2, color='red')
    print(triangle.describe())

    square = Square(3, 'blue')
    print(square.describe())





