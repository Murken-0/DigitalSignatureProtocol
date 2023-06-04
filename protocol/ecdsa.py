from hashlib import sha256
from curve import secp256k1
from random import randint
from signature import Signature
from utils.binary import numberFromByteString
from utils.compatibility import *
from point import *


class Ecdsa:

    @classmethod
    def sign(cls, message:str, privateKey):
        n = secp256k1.N
        r = 0
        while r == 0:
            k = randint(1, n - 1)
            r_point = secp256k1.G.multiply(k)
            r = r_point.x % n
        
        hashedMsg = sha256(message.encode()).digest()
        num = numberFromByteString(hashedMsg)

        k_inverse = inverse(k, n)
        s = k_inverse * (num + r * privateKey) % n

        return Signature(r, s)

    @classmethod
    def verify(cls, message, signature, publicKey):
        # byteMessage = sha256(toBytes(message)).digest()
        # numberMessage = numberFromByteString(byteMessage)
        s_inverse = inverse(signature.s, secp256k1.N)
        u = message