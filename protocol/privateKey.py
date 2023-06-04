from curve import secp256k1
from publicKey import PublicKey
from random import randint
from utils.binary import hexFromInt


class PrivateKey:

    def __init__(self):
        self.curve = secp256k1
        self.secret = hexFromInt(randint(1, self.curve.N - 1))

    def publicKey(self):
        return PublicKey(self.curve.G.multiply(self.secret))