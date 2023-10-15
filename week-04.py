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


def hex2string (input):
    '''
    >>> hex2string('61')
    'a'
    >>> hex2string('776f726c64')
    'world'
    >>> hex2string('68656c6c6f')
    'hello'
    '''
    hex_characters = [input[i:i + 2] for i in range(0, len(input), 2)]
    result =''
    for c in hex_characters:
        result += chr(int(c, base=16))
    return result

def string2hex (input):
    '''
    >>> string2hex('a')
    '61'
    >>> string2hex('hello')
    '68656c6c6f'
    >>> string2hex('world')
    '776f726c64'
    >>> string2hex('foo')
    '666f6f'
    '''
    characters = [input[i] for i in range(len(input))]
    result = ''
    for c in characters:
        result += hex(ord(c))[2:]
    return result

def hex_xor (input_1, input_2):
    '''
    >>> hex_xor('0aabbf11','12345678')
    '189fe969'
    >>> hex_xor('12cc','12cc')
    '0000'
    >>> hex_xor('1234','2345')
    '3171'
    >>> hex_xor('111','248')
    '359'
    >>> hex_xor('8888888','1234567')
    '9abcdef'
    '''
    result = ''
    for i in range(len(input_1)):
        byte_1 = fillupbyte(bin(int(str(input_1[i]), base=16))[2:], 4, 'left')
        byte_2 = fillupbyte(bin(int(str(input_2[i]), base=16))[2:], 4, 'left')

        tmp_result = ''
        for j in range(len(byte_1)):
            if (byte_1[j] == byte_2[j]):
                tmp_result += '0'
            else:
                tmp_result += '1'

        result += str(hex(int(tmp_result, base=2))[2:])

    return result

def encrypt_single_byte_xor (input, single_byte):
    '''
    >>> encrypt_single_byte_xor('aaabbccc','00')
    'aaabbccc'
    >>> encrypt_single_byte_xor(string2hex('hello'),'aa')
    'c2cfc6c6c5'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('hello'),'aa'),'aa'))
    'hello'
    >>> hex2string(encrypt_single_byte_xor(encrypt_single_byte_xor(string2hex('Encrypt and decrypt are the same'),'aa'),'aa'))
    'Encrypt and decrypt are the same'
    '''
    result = ''
    for c in input:
        result += hex_xor(c,single_byte)
    return result

def decrypt_single_byte_xor (input):
    '''
    >>> decrypt_single_byte_xor('e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480')
    'Hi! You have found me!'
    >>> decrypt_single_byte_xor('b29e9f96839085849d9085989e9f82d1889e84d199908794d197989f95d1859994d181908282869e8395d0')
    'Congratulations you have find the password!'
    >>> decrypt_single_byte_xor('e1ded996ddd8d9c1c596c1ded7c296dfc596ded7c6c6d3d8dfd8d18996e1ded3c4d396d7db96ff89')
    'Who knows what is happening? Where am I?'
    '''
    best_score = 0
    best_message = ""
    input_bytes = bytes.fromhex(input)

    for possible_key in range(256):
        decrypted_message = ""
        for byte in input_bytes:
            xor_result = byte ^ possible_key
            char = chr(xor_result)
            if char in valid_characters:
                decrypted_message += char
        else:
            score = sum(1 for char in decrypted_message if char in valid_characters)
            if score > best_score:
                best_score = score
                best_message = decrypted_message

    return best_message