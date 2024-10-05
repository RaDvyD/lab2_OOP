import math


# Базовий клас Трикутник
class Triangle:
    # Атрибут класу (використовується для всіх екземплярів класу)
    shape_type = "Triangle"

    # Конструктор за замовчуванням та з переданими параметрами
    def __init__(self, a=1, b=1, c=1):
        # Приватні атрибути (починаються з "_")
        self._a = a
        self._b = b
        self._c = c

    # Властивість (property) для сторони 'a' (з можливістю зміни)
    @property
    def a(self):
        return self._a

    # Сетер (метод для зміни значення атрибуту через property)
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side length must be positive")  # Викидання винятку при некоректному значенні

    # Метод для обчислення периметру
    def perimeter(self):
        return self._a + self._b + self._c

    # Метод для обчислення площі трикутника за формулою Герона
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    # Перевизначення методу __str__ для виводу об'єкта у вигляді рядка
    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}"

    # Статичний метод для перевірки, чи можна утворити трикутник з даними сторонами
    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and b + c > a and a + c > b


# Похідний клас Чотирикутник, наслідує клас Трикутник
class Quadrilateral(Triangle):
    # Атрибут класу
    shape_type = "Quadrilateral"

    # Конструктор, що ініціалізує чотири сторони і дві діагоналі
    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c)  # Виклик конструктора базового класу
        self._d = d  # Четверта сторона
        self._e = e  # Перша діагональ
        self._f = f  # Друга діагональ

    # Перевизначення методу для обчислення периметру (сума всіх сторін)
    def perimeter(self):
        return self._a + self._b + self._c + self._d

    # Перевизначення методу для обчислення площі за формулою з зображення
    def area(self):
        # Формула, наведена на зображенні
        numerator = (4 * self._e ** 2 * self._f ** 2) - (
                    (self._b ** 2 + self._d ** 2 - self._a ** 2 - self._c ** 2) ** 2)
        return math.sqrt(numerator) / 16

    # Перевизначення методу __str__ для надання текстового представлення об'єкта
    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}, d={self._d}, diagonals e={self._e}, f={self._f}"


# Додатковий клас для множинного наслідування
class Shape:
    # Конструктор з можливістю встановлення імені
    def __init__(self, name="Unknown"):
        self.name = name

    # Метод для виводу опису об'єкта
    def description(self):
        return f"This is a shape called {self.name}."


# Клас з множинним наслідуванням (наслідує як Quadrilateral, так і Shape)
class NamedQuadrilateral(Quadrilateral, Shape):
    # Конструктор, що наслідує з двох батьківських класів
    def __init__(self, a, b, c, d, e, f, name="Quadrilateral"):
        Quadrilateral.__init__(self, a, b, c, d, e, f)  # Виклик конструктора класу Quadrilateral
        Shape.__init__(self, name)  # Виклик конструктора класу Shape

    # Перевизначення методу __str__ з додаванням імені фігури
    def __str__(self):
        return f"{self.name}: {Quadrilateral.__str__(self)}"


# Демонстраційний алгоритм для роботи з класами
def main():
    # Створення екземпляру класу Трикутник
    triangle = Triangle(3, 4, 5)
    print(triangle)  # Використання перевизначеного __str__
    print("Perimeter of triangle:", triangle.perimeter())  # Виклик методу периметра
    print("Area of triangle:", triangle.area())  # Виклик методу площі

    # Створення екземпляру класу Чотирикутник
    quad = Quadrilateral(4, 5, 6, 7, 8, 9)
    print(quad)  # Використання перевизначеного __str__
    print("Perimeter of quadrilateral:", quad.perimeter())  # Виклик перевизначеного методу периметра
    print("Area of quadrilateral:", quad.area())  # Виклик перевизначеного методу площі

    # Створення екземпляру класу з множинним наслідуванням
    named_quad = NamedQuadrilateral(4, 5, 6, 7, 8, 9, "MyShape")
    print(named_quad)  # Використання перевизначеного __str__ з ім'ям
    print(named_quad.description())  # Виклик методу з другого батьківського класу Shape
    print("Perimeter of named quadrilateral:", named_quad.perimeter())  # Виклик методу периметра
    print("Area of named quadrilateral:", named_quad.area())  # Виклик методу площі

    # Демонстрація статичного методу
    print("Is it a valid triangle?", Triangle.is_triangle(3, 4, 5))


if __name__ == "__main__":
    main()
import math


# Базовий клас Трикутник
class Triangle:
    # Атрибут класу (використовується для всіх екземплярів класу)
    shape_type = "Triangle"

    # Конструктор за замовчуванням та з переданими параметрами
    def __init__(self, a=1, b=1, c=1):
        # Приватні атрибути (починаються з "_")
        self._a = a
        self._b = b
        self._c = c

    # Властивість (property) для сторони 'a' (з можливістю зміни)
    @property
    def a(self):
        return self._a

    # Сетер (метод для зміни значення атрибуту через property)
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side length must be positive")  # Викидання винятку при некоректному значенні

    # Метод для обчислення периметру
    def perimeter(self):
        return self._a + self._b + self._c

    # Метод для обчислення площі трикутника за формулою Герона
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    # Перевизначення методу __str__ для виводу об'єкта у вигляді рядка
    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}"

    # Статичний метод для перевірки, чи можна утворити трикутник з даними сторонами
    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and b + c > a and a + c > b


# Похідний клас Чотирикутник, наслідує клас Трикутник
class Quadrilateral(Triangle):
    # Атрибут класу
    shape_type = "Quadrilateral"

    # Конструктор, що ініціалізує чотири сторони і дві діагоналі
    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c)  # Виклик конструктора базового класу
        self._d = d  # Четверта сторона
        self._e = e  # Перша діагональ
        self._f = f  # Друга діагональ

    # Перевизначення методу для обчислення периметру (сума всіх сторін)
    def perimeter(self):
        return self._a + self._b + self._c + self._d

    # Перевизначення методу для обчислення площі за формулою з зображення
    def area(self):
        # Формула, наведена на зображенні
        numerator = (4 * self._e ** 2 * self._f ** 2) - (
                    (self._b ** 2 + self._d ** 2 - self._a ** 2 - self._c ** 2) ** 2)
        return math.sqrt(numerator) / 16

    # Перевизначення методу __str__ для надання текстового представлення об'єкта
    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}, d={self._d}, diagonals e={self._e}, f={self._f}"


# Додатковий клас для множинного наслідування
class Shape:
    # Конструктор з можливістю встановлення імені
    def __init__(self, name="Unknown"):
        self.name = name

    # Метод для виводу опису об'єкта
    def description(self):
        return f"This is a shape called {self.name}."


# Клас з множинним наслідуванням (наслідує як Quadrilateral, так і Shape)
class NamedQuadrilateral(Quadrilateral, Shape):
    # Конструктор, що наслідує з двох батьківських класів
    def __init__(self, a, b, c, d, e, f, name="Quadrilateral"):
        Quadrilateral.__init__(self, a, b, c, d, e, f)  # Виклик конструктора класу Quadrilateral
        Shape.__init__(self, name)  # Виклик конструктора класу Shape

    # Перевизначення методу __str__ з додаванням імені фігури
    def __str__(self):
        return f"{self.name}: {Quadrilateral.__str__(self)}"


# Демонстраційний алгоритм для роботи з класами
def main():
    # Створення екземпляру класу Трикутник
    triangle = Triangle(3, 4, 5)
    print(triangle)  # Використання перевизначеного __str__
    print("Perimeter of triangle:", triangle.perimeter())  # Виклик методу периметра
    print("Area of triangle:", triangle.area())  # Виклик методу площі

    # Створення екземпляру класу Чотирикутник
    quad = Quadrilateral(4, 5, 6, 7, 8, 9)
    print(quad)  # Використання перевизначеного __str__
    print("Perimeter of quadrilateral:", quad.perimeter())  # Виклик перевизначеного методу периметра
    print("Area of quadrilateral:", quad.area())  # Виклик перевизначеного методу площі

    # Створення екземпляру класу з множинним наслідуванням
    named_quad = NamedQuadrilateral(4, 5, 6, 7, 8, 9, "MyShape")
    print(named_quad)  # Використання перевизначеного __str__ з ім'ям
    print(named_quad.description())  # Виклик методу з другого батьківського класу Shape
    print("Perimeter of named quadrilateral:", named_quad.perimeter())  # Виклик методу периметра
    print("Area of named quadrilateral:", named_quad.area())  # Виклик методу площі

    # Демонстрація статичного методу
    print("Is it a valid triangle?", Triangle.is_triangle(3, 4, 5))


if __name__ == "__main__":
    main()
import math


# Базовий клас Трикутник
class Triangle:
    # Атрибут класу (використовується для всіх екземплярів класу)
    shape_type = "Triangle"

    # Конструктор за замовчуванням та з переданими параметрами
    def __init__(self, a=1, b=1, c=1):
        # Приватні атрибути (починаються з "_")
        self._a = a
        self._b = b
        self._c = c

    # Властивість (property) для сторони 'a' (з можливістю зміни)
    @property
    def a(self):
        return self._a

    # Сетер (метод для зміни значення атрибуту через property)
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side length must be positive")  # Викидання винятку при некоректному значенні

    # Метод для обчислення периметру
    def perimeter(self):
        return self._a + self._b + self._c

    # Метод для обчислення площі трикутника за формулою Герона
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    # Перевизначення методу __str__ для виводу об'єкта у вигляді рядка
    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}"

    # Статичний метод для перевірки, чи можна утворити трикутник з даними сторонами
    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and b + c > a and a + c > b


# Похідний клас Чотирикутник, наслідує клас Трикутник
class Quadrilateral(Triangle):
    # Атрибут класу
    shape_type = "Quadrilateral"

    # Конструктор, що ініціалізує чотири сторони і дві діагоналі
    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c)  # Виклик конструктора базового класу
        self._d = d  # Четверта сторона
        self._e = e  # Перша діагональ
        self._f = f  # Друга діагональ

    # Перевизначення методу для обчислення периметру (сума всіх сторін)
    def perimeter(self):
        return self._a + self._b + self._c + self._d

    # Перевизначення методу для обчислення площі за формулою з зображення
    def area(self):
        # Формула, наведена на зображенні
        numerator = (4 * self._e ** 2 * self._f ** 2) - (
                    (self._b ** 2 + self._d ** 2 - self._a ** 2 - self._c ** 2) ** 2)
        return math.sqrt(numerator) / 16

    # Перевизначення методу __str__ для надання текстового представлення об'єкта
    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}, d={self._d}, diagonals e={self._e}, f={self._f}"


# Додатковий клас для множинного наслідування
class Shape:
    # Конструктор з можливістю встановлення імені
    def __init__(self, name="Unknown"):
        self.name = name

    # Метод для виводу опису об'єкта
    def description(self):
        return f"This is a shape called {self.name}."


# Клас з множинним наслідуванням (наслідує як Quadrilateral, так і Shape)
class NamedQuadrilateral(Quadrilateral, Shape):
    # Конструктор, що наслідує з двох батьківських класів
    def __init__(self, a, b, c, d, e, f, name="Quadrilateral"):
        Quadrilateral.__init__(self, a, b, c, d, e, f)  # Виклик конструктора класу Quadrilateral
        Shape.__init__(self, name)  # Виклик конструктора класу Shape

    # Перевизначення методу __str__ з додаванням імені фігури
    def __str__(self):
        return f"{self.name}: {Quadrilateral.__str__(self)}"


# Демонстраційний алгоритм для роботи з класами
def main():
    # Створення екземпляру класу Трикутник
    triangle = Triangle(3, 4, 5)
    print(triangle)  # Використання перевизначеного __str__
    print("Perimeter of triangle:", triangle.perimeter())  # Виклик методу периметра
    print("Area of triangle:", triangle.area())  # Виклик методу площі

    # Створення екземпляру класу Чотирикутник
    quad = Quadrilateral(4, 5, 6, 7, 8, 9)
    print(quad)  # Використання перевизначеного __str__
    print("Perimeter of quadrilateral:", quad.perimeter())  # Виклик перевизначеного методу периметра
    print("Area of quadrilateral:", quad.area())  # Виклик перевизначеного методу площі

    # Створення екземпляру класу з множинним наслідуванням
    named_quad = NamedQuadrilateral(4, 5, 6, 7, 8, 9, "MyShape")
    print(named_quad)  # Використання перевизначеного __str__ з ім'ям
    print(named_quad.description())  # Виклик методу з другого батьківського класу Shape
    print("Perimeter of named quadrilateral:", named_quad.perimeter())  # Виклик методу периметра
    print("Area of named quadrilateral:", named_quad.area())  # Виклик методу площі

    # Демонстрація статичного методу
    print("Is it a valid triangle?", Triangle.is_triangle(3, 4, 5))


if __name__ == "__main__":
    main()
