from protocol.curve import secp256k1
from protocol.binary import hexFromInt
from random import randint
from protocol.publicKey import PublicKey
from protocol.myMath import Math as m

class PrivateKey:

    def __init__(self):
        self.curve = secp256k1
        self.secret = randint(1, self.curve.N - 1)

    def __str__(self) -> str:
        return hexFromInt(self.secret) 

    def publicKey(self) -> PublicKey:
        return PublicKey(m.multiply(self.curve.G, self.secret))