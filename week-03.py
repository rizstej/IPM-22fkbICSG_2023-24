base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def hex2bin(input):
    '''
    >>> hex2bin('f')
    '1111'
    >>> hex2bin('5')
    '101'
    >>> hex2bin('1')
    '1'
    >>> hex2bin('61')
    '1100001'
    '''
    hexadecimal_number = "0x" + str(input)
    tmp = bin(int(hexadecimal_number, base=16))
    result = tmp[2:]
    return result


def bin2hex(input):
    '''
    >>> bin2hex('1111')
    'f'
    >>> bin2hex('100001')
    '21'
    >>> bin2hex('1')
    '1'
    '''
    binary_number = "0b" + str(input)
    tmp = hex(int(binary_number, base=2))
    result = tmp[2:]
    return result


def fillupbyte(input, byte=8):
    '''
    >>> fillupbyte('011')
    '00000011'
    >>> fillupbyte('1')
    '00000001'
    >>> fillupbyte('10111')
    '00010111'
    >>> fillupbyte('11100111')
    '11100111'
    >>> fillupbyte('111001111')
    '0000000111001111'
    '''

    divModRes = divmod(len(input), byte)
    byte_result = byte
    if (divModRes[0] != 0):
        if (divModRes[1] != 0):
            byte_result = divModRes[0] * byte + byte

    result = input.rjust(byte_result, '0')
    return result


def int2base64(input):
    '''
    >>> int2base64(0x61)
    'YQ=='
    >>> int2base64(0x78)
    'eA=='
    '''
    hexadecimal_number = str(hex(input))
    tmp = fillupbyte(hex2bin(hexadecimal_number[2:]))

    byte = 6
    divModRes = divmod(len(str(tmp)), byte)
    byte_result = byte
    if (divModRes[0] != 0):
        if (divModRes[1] != 0):
            byte_result = divModRes[0] * byte + byte

    binary_string = tmp.ljust(byte_result, '0')
    base64_characters = [binary_string[i:i + byte] for i in range(0, len(binary_string), byte)]

    base64_result = ''

    for c in base64_characters:
        base64_result += base64_table[int(c, base=2)]

    byte = 4
    divModRes = divmod(len(str(base64_result)), byte)
    byte_result = byte
    if (divModRes[0] != 0):
        if (divModRes[1] != 0):
            byte_result = divModRes[0] * byte + byte
    result = base64_result.ljust(byte_result, '=')

    return result


def hex2base64(input):
    '''
    >>> hex2base64('61')
    'YQ=='
    >>> hex2base64('123456789abcde')
    'EjRWeJq83g=='
    '''
    hexadecimal_number = "0x" + str(input)
    tmp = fillupbyte(hex2bin(hexadecimal_number[2:]))

    byte = 6
    divModRes = divmod(len(str(tmp)), byte)
    byte_result = byte
    if (divModRes[0] != 0):
        if (divModRes[1] != 0):
            byte_result = divModRes[0] * byte + byte

    binary_string = tmp.ljust(byte_result, '0')
    base64_characters = [binary_string[i:i + byte] for i in range(0, len(binary_string), byte)]

    base64_result = ''

    for c in base64_characters:
        base64_result += base64_table[int(c, base=2)]

    byte = 4
    divModRes = divmod(len(str(base64_result)), byte)
    byte_result = byte
    if (divModRes[0] != 0):
        if (divModRes[1] != 0):
            byte_result = divModRes[0] * byte + byte
    result = base64_result.ljust(byte_result, '=')

    return result
