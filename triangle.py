import math

class Triangle:
    shape_type = "Triangle"

    def __init__(self, a=1, b=1, c=1):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError("Side length must be positive")

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}"

    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and b + c > a and a + c > b
