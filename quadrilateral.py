from triangle import Triangle
import math
from shape import Shape

class Quadrilateral(Triangle):
    shape_type = "Quadrilateral"

    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c)
        self._d = d
        self._e = e
        self._f = f

    def perimeter(self):
        return self._a + self._b + self._c + self._d

    def area(self):
        numerator = (4 * self._e ** 2 * self._f ** 2) - ((self._b ** 2 + self._d ** 2 - self._a ** 2 - self._c ** 2) ** 2)
        return math.sqrt(numerator) / 16

    def __str__(self):
        return f"{self.shape_type} with sides a={self._a}, b={self._b}, c={self._c}, d={self._d}, diagonals e={self._e}, f={self._f}"

class NamedQuadrilateral(Quadrilateral, Shape):
    def __init__(self, a, b, c, d, e, f, name="Quadrilateral"):
        Quadrilateral.__init__(self, a, b, c, d, e, f)
        Shape.__init__(self, name)

    def __str__(self):
        return f"{self.name}: {Quadrilateral.__str__(self)}"
