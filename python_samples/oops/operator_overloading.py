'''
    Module file for Operator Overloading sample class
'''


class Point:
    '''
        Point class to represent a point on 2-D plot
    '''
    def __init__(self, val_x, val_y):
        self.val_x = val_x
        self.val_y = val_y

    def __add__(self, point):
        val_x = self.val_x + point.val_x
        val_y = self.val_y + point.val_y
        return Point(val_x, val_y)

    def __sub__(self, point):
        val_x = self.val_x - point.val_x
        val_y = self.val_y - point.val_y
        return Point(val_x, val_y)

    def __str__(self):
        return f"Point({self.val_x}, {self.val_y})"


if __name__ == '__main__':
    p1 = Point(3, 5)
    p2 = Point(1, 2)
    print(p1 + p2)
    print(p1 - p2)
    p1 += Point(2, 4)
    print(p1)
    p1 -= p2
    print(p1)
