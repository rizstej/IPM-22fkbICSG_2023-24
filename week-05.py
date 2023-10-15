key_list = [0x20, 0x44, 0x54,0x20]

#source: https://github.com/rizstej/IPM-22fkbICSG_2023-24/blob/main/week-04.py
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

#source: https://github.com/rizstej/IPM-22fkbICSG_2023-24/blob/main/week-04.py
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

#source:
def encrypt_by_add_mod (input, key):
    '''
    >>> encrypt_by_add_mod('Hello',123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Hello',123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    '''
    chars = [input[i] for i in range(len(input))]
    encrypted_code = ''
    for x in chars:
        encrypted_code += (hex2string(hex((int(string2hex(x),base=16)+key)%256)[2:]))

    return encrypted_code

def encrypt_xor_with_changing_key_by_prev_cipher (input, key, coding):
    '''
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    '''
    chars = [input[i] for i in range(len(input))]
    code = ''
    code_for_decrypt = []

    if coding == 'encrypt':
        for c in chars:
            code_for_decrypt.append(key)
            code += chr(ord(c) ^ key)
            key = ord(c) ^ key

    if coding == 'decrypt':
        for i in range(len(chars)):
            code += chr(ord(chars[i]) ^ key)
            key = (ord(code[i]) ^ key)

    return code

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key (input, key_list, coding):
    '''
    >>> key_list = [0x20, 0x44, 0x54, 0x20]
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
    'A&7D$@P'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
    'A%5B#GW'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'abcdefg'
    >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
    ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
    ...        key_list,'decrypt')
    'Hellobello, it will work for a long message as well'
    '''
    chars = [input[i] for i in range(len(input))]
    chunks = []
    part_1, part_2, part_3, part_4 = '', '', '', ''

    for i in range(len(chars)):
      if (i % 4) == 0: part_1 += chars[i]
      if (i % 4) == 1: part_2 += chars[i]
      if (i % 4) == 2: part_3 += chars[i]
      if (i % 4) == 3: part_4 += chars[i]

    chunks.append(part_1), chunks.append(part_2), chunks.append(part_3), chunks.append(part_4)
    coded_chunks = []
    code = ''

    if coding == 'encrypt':

        for i in range(len(chunks)):
            key = key_list[i]

            for c in chunks[i]:
                code += chr(ord(c) ^ key)
                key = ord(c) ^ key

            coded_chunks.append(code)
            code = ''

        part_1, part_2, part_3, part_4 = '', '', '', ''

        for i in range(len(coded_chunks)):
            for j in range(len(coded_chunks[i])):
                if (j % 4) == 0: part_1 += coded_chunks[i][j]
                if (j % 4) == 1: part_2 += coded_chunks[i][j]
                if (j % 4) == 2: part_3 += coded_chunks[i][j]
                if (j % 4) == 3: part_4 += coded_chunks[i][j]

        code += part_1
        code += part_2
        code += part_3
        code += part_4

    if coding == 'decrypt':

        for i in range(len(chunks)):
            key = key_list[i]

            for j in range(len(chunks[i])):
                code += chr(ord(chunks[i][j]) ^ key)
                key = ord(code[j]) ^ key

            coded_chunks.append(code)
            code = ''

        part_1, part_2, part_3, part_4 = '', '', '', ''

        for i in range(len(coded_chunks)):
            for j in range(len(coded_chunks[i])):
                if (j % 4) == 0: part_1 += coded_chunks[i][j]
                if (j % 4) == 1: part_2 += coded_chunks[i][j]
                if (j % 4) == 2: part_3 += coded_chunks[i][j]
                if (j % 4) == 3: part_4 += coded_chunks[i][j]

        code += part_1
        code += part_2
        code += part_3
        code += part_4

    return code