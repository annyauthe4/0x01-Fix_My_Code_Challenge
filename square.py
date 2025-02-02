#!/usr/bin/python3
"""Module defines a Square class and methods."""


class Square():
    """Defines a square class with dynamic attributes."""

    def __init__(self, *args, **kwargs):
        """Initializes a square where all sides are equal."""
        if "width" in kwargs:
            self.width = kwargs["width"]
            self.height = kwargs["width"]
        else:
            self.width = 0
            self.height = 0

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
