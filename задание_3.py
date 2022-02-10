class Rectangle:

    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def calc_squre(self):
        return self._length*self._width

    def calc_perimeter(self):
        return 2 * (self._length+self._width)

rec = Rectangle(10, 9)

print(rec.calc_squre())
print(rec.calc_perimeter())
print(rec.length)
print(rec.width)

