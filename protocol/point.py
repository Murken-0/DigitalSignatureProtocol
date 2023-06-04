from protocol.curve import secp256k1

def inverse(number, modulus):
        return pow(number, -1, modulus)

class Point:

    def __init__(self, x=0, y=0):
        a = secp256k1.A
        b = secp256k1.B
        p = secp256k1.P
        
        if (y ** 2) % p != (x ** 3 + a * x + b) % p:
            raise Exception("The point is not on the curve")
        
        self.x = x
        self.y = y

    def isAtInfinity(self):
        return self.y == 0
    
    def is_equal_to(self, point):
        return self.x == point.x & self.y == point.y
    
    def add(self, point):
        p = secp256k1.P
        if self.is_equal_to(point):
            slope = (3 * point.x ** 2) * inverse(2 * point.y, p) % p
        else:
            slope = (point.y - self.y) * inverse(point.x - self.x, p) % p
        x = (slope ** 2 - point.x - self.x) % p
        y = (slope * (self.x - x) - self.y) % p
        return Point(x, y)
    
    def multiply(self, times):
        current_point = self
        current_coefficent = 1

        prev_points = []
        while current_coefficent < times:
            prev_points.append((current_coefficent, current_point))
            if 2 * current_coefficent <= times:
                current_point = current_point.add(current_point)
            else:
                next_point = self
                next_coefficent = 1
                for (previus_coefficent, previus_point) in prev_points:
                    if previus_coefficent + current_coefficent <= times:
                        if previus_point.x != current_point.x:
                            next_coefficent = previus_coefficent
                            next_point = previus_point
                current_point = current_point.add(next_point)
                current_coefficent += next_coefficent
        return current_point
