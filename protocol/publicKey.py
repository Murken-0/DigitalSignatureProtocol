from .point import Point
from .curve import secp256k1

class PublicKey:

    def __init__(self, point: Point):
        self.point = point
        self.curve = secp256k1

    def toString(self, encoded=False):
        return "X={x}; Y={y}".format(x = self.point.x, y = self.point.y)