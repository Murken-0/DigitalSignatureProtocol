def hexFromInt(number:int) -> str: 
    hexadecimal = "{0:x}".format(number)
    if len(hexadecimal) % 2 == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal

def intFromHex(hexadecimal:str) -> int:
    return int(hexadecimal, 16)