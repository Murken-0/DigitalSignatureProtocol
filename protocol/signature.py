from protocol.binary import hexFromInt

class Signature:
    def __init__(self, r, s):
        self.r = r
        self.s = s
    
    def __str__(self) -> str:
        return "\n(r = {},\n s = {})".format(hexFromInt(self.r), hexFromInt(self.s))