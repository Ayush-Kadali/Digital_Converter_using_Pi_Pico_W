# converting decimal to binary
def decimal_to_binary(n):
    n = int(n)
    return bin(n).replace("0b", "")

#converting octal to binary
def octal_to_binary(n):
    n = int(n, 8)
    return bin(n).replace("0b", "")

#converting hexadecimal to binary
def hex_to_binary(n):
    n = int(n, 16)
    return bin(n).replace("0b", "")

#converting grey code to binary
def grey_to_binary(n):
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n).replace("0b", "")

#converting excess-3 code to binary
def excess_3_to_binary(n):
    n = int(n, 2)
    n -= 3
    return bin(n).replace("0b", "")

def to_bin(datatype, data):
    if datatype == "Decimal":
        return decimal_to_binary(data)
    elif datatype == "Binary":
        return data
    elif datatype == "Octal":
        return octal_to_binary(data)
    elif datatype == "Hexadecimal":
        return hex_to_binary(data)
    elif datatype == "Grey":
        return grey_to_binary(data)
    elif datatype == "EX3":
        return excess_3_to_binary(data)

