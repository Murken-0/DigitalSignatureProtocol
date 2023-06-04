from protocol.privateKey import PrivateKey
from protocol.publicKey import PublicKey
from random import randint
from protocol.myMath import Math as m
from protocol.signature import Signature

class Ecdsa:

    @staticmethod
    def sign(message:int, private_key:PrivateKey) -> Signature:
        n = private_key.curve.N
        r = 0
        while r == 0:
            k = randint(1, n - 1)
            r_point = m.multiply(private_key.curve.G, k)
            r = r_point.x % n

        k_inverse = m.inverse(k, n)
        s = k_inverse * (message + r * private_key.secret) % n

        return Signature(r, s)

    @staticmethod
    def verify(message:str, signature:Signature, public_key:PublicKey) -> bool:
        s_inverse = m.inverse(signature.s, public_key.curve.N)
        u = message * s_inverse % public_key.curve.N
        v = signature.r * s_inverse % public_key.curve.N
        c_point = m.add(m.multiply(public_key.curve.G, u), m.multiply(public_key.point, v)) 
        return c_point.x == signature.r