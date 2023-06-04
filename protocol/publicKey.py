from protocol.point import Point
from protocol.curve import secp256k1


class PublicKey:

    def __init__(self, point:Point):
        self.point:Point = point
        self.curve = secp256k1

    def __str__(self) -> str:
        return str(self.point)