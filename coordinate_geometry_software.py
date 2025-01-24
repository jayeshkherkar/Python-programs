class Point:

    def __init__(self, a, b):
        self._x = a
        self._y = b

    def set_points(self, a1, b1):
        self._x = a1
        self._y = b1

    def get_points(self):
        print(self)

    def __str__(self):
        return '({},{})'.format(self._x, self._y)

    # Distance between two points

    def distance(self, other):
        return ((other.y - self._y) ** 2 + (other.x - self._x) ** 2) ** 0.5

    # Distance of point from origin

    def Distance(self):
        return self.distance(Point(0,0))

    # Midpoint of two given points

    def midpoint(self, other):
        x1 = (self._x + other.x) / 2
        y1 = (self._y + other.y) / 2
        return '({},{})'.format(x1, y1)

    # If line passes through two points then we find the slope

    @staticmethod
    def SLOPE(p1, p2):
        return 'slope = {}/{}'.format((p2._y - p1._y), (p2._x - p1._x))


class line:

    def __init__(self, a, b, c):

        self._X = a
        self._Y = b
        self._C = c

    def set_line(self, a1, b1, c1):

        self.X = a1
        self.Y = b1
        self.C = c1

    def get_line(self):

        print(self)

    def __str__(self):

        if ((self.X < 0 and self.Y > 0 and self.C > 0) or (self.X > 0 and self.Y > 0 and self.C > 0)):

            return '{}x+{}y+{} = 0'.format(self.X, self.Y, self.C)

        elif ((self.X < 0 and self.Y < 0 and self.C > 0) or (self.X > 0 and self.Y < 0 and self.C > 0)):

            return '{}x{}y+{} = 0'.format(self.X, self.Y, self.C)

        elif ((self.C < 0 and self.Y < 0 and self.X < 0) or (self.C < 0 and self.Y < 0 and self.X > 0)):

            return '{}x{}y{} = 0'.format(self.X, self.Y, self.C)

        elif ((self.Y > 0 and self.X < 0 and self.C < 0) or (self.Y > 0 and self.X > 0 and self.C < 0)):

            return '{}x+{}y{} = 0'.format(self.X, self.Y, self.C)

        '''elif((self.Y<0 and self.X<0 and self.C>0) or (self.Y<0 and self.X>0 and self.C>0)):

            return '{}x-{}y+{} = 0'.format(self.X,self.Y,self.C)'''

    def point_lies_on_line(l, p):

        V = l.X * p.x + l.Y * p.y + l.C

        if V == 0:

            print("Point is on the line")

        else:

            print("Point is not on the line")

    def D(l, p):

        return (abs(l.X * p.x + l.Y * p.y + l.C)) / ((l.X) ** 2 + (l.Y) ** 2) ** 0.5

    def slope(self):

        return 'slope = {}/{}'.format(-self.X, self.Y)


p1 = Point(4, 6)
p2 = Point(3, 2)
print(Point.SLOPE(p1, p2))
# l1 = line(2,3,-5)
# print(l1.slope())




