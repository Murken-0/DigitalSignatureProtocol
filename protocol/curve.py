from .mymath import Math
from .point import Point


class CurveFp:

    def __init__(self, A, B, P, N, Gx, Gy, name):
        self.A = A
        self.B = B
        self.P = P
        self.N = N
        self.G = Point(Gx, Gy)
        self.name = name

    def contains(self, p):
        if not 0 <= p.x <= self.P - 1:
            return False
        if not 0 <= p.y <= self.P - 1:
            return False
        if (p.y**2 - (p.x**3 + self.A * p.x + self.B)) % self.P != 0:
            return False
        return True

    def length(self):
        return (1 + len("%x" % self.N)) // 2

    def y(self, x, isEven):
        ySquared = (pow(x, 3, self.P) + self.A * x + self.B) % self.P
        y = Math.modularSquareRoot(ySquared, self.P)
        if isEven != (y % 2 == 0):
            y = self.P - y
        return y

secp256k1 = CurveFp(
    name="secp256k1",
    A=0x0000000000000000000000000000000000000000000000000000000000000000,
    B=0x0000000000000000000000000000000000000000000000000000000000000007,
    P=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    N=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    Gx=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    Gy=0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
)