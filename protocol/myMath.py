from protocol.point import Point
from protocol.curve import secp256k1

class Math:

    @staticmethod
    def inverse(number:int, modulus:int):
        num = number
        mod = modulus
        return pow(num, -1, mod)

    @staticmethod
    def isAtInfinity(point:Point):
        return point.y == 0
    
    @staticmethod
    def is_points_equal(first: Point, second:Point):
        eq_x = first.x == second.x
        eq_y = first.y == second.y
        return eq_x and eq_y
    
    @classmethod
    def add(cls, first:Point, second:Point):
        p = secp256k1.P
        if cls.is_points_equal(first, second):
            slope = (3 * second.x ** 2) * cls.inverse(2 * second.y, p) % p
        else:
            slope = (second.y - first.y) * cls.inverse(second.x - first.x, p) % p
        x = (slope ** 2 - second.x - first.x) % p
        y = (slope * (first.x - x) - first.y) % p
        return Point(x, y)
    
    @classmethod
    def multiply(cls, point:Point, times:int):
        current_point = point
        current_coefficent = 1

        prev_points = []
        while current_coefficent < times:
            prev_points.append((current_coefficent, current_point))
            if 2 * current_coefficent <= times:
                current_coefficent *= 2
                current_point = cls.add(current_point, current_point)
            else:
                next_point = point
                next_coefficent = 1
                for (previus_coefficent, previus_point) in prev_points:
                    if previus_coefficent + current_coefficent <= times:
                        if previus_point.x != current_point.x:
                            next_coefficent = previus_coefficent
                            next_point = previus_point
                current_point = cls.add(current_point, next_point)
                current_coefficent += next_coefficent
        return current_point