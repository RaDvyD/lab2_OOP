from triangle import Triangle
from quadrilateral import Quadrilateral, NamedQuadrilateral

def main():
    triangle = Triangle(3, 4, 5)
    print(triangle)
    print("Perimeter of triangle:", triangle.perimeter())
    print("Area of triangle:", triangle.area())

    quad = Quadrilateral(4, 5, 6, 7, 8, 9)
    print(quad)
    print("Perimeter of quadrilateral:", quad.perimeter())
    print("Area of quadrilateral:", quad.area())

    named_quad = NamedQuadrilateral(4, 5, 6, 7, 8, 9, "MyShape")
    print(named_quad)
    print(named_quad.description())
    print("Perimeter of named quadrilateral:", named_quad.perimeter())
    print("Area of named quadrilateral:", named_quad.area())

    print("Is it a valid triangle?", Triangle.is_triangle(3, 4, 5))


if __name__ == "__main__":
    main()
