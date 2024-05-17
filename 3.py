from math import gcd

# данные из задачт
cipher = [
    218,
    34,
    194,
    164,
    220,
    50,
    237,
    77,
    68,
    151,
    135,
    21,
    101,
    167,
    196,
    98,
    196,
    219,
    89,
    241,
    16,
    134,
    240,
    43,
    36,
    193,
    37,
    17,
    184,
    61,
    81,
    41,
    81,
    148,
    18,
    172,
    193,
    37,
    203,
    233,
    244,
    145,
    18,
    1,
    121,
    46,
    18,
    193,
]
y = 109
n = 247
p = 13
q = 19


# функция для расчета символа Лежандра 
def symbol_legendre(x, p):
    sl = pow(x, (p - 1) // 2, p)
    if sl == p - 1:
        return -1
    return sl


# функция для расшифровки Гольдвассера-Микали
def decrypt_GM(cipher, y, n, p, q):
    bits = []
    for c in cipher:
        legendre_p = symbol_legendre(c, p)
        legendre_q = symbol_legendre(c, q)
        if legendre_p == -1 or legendre_q == -1:
            bits.append(1)
        else:
            bits.append(0)

    message = bits_to_bytes(bits)  # тут переделываем в байты
    return message


# функция из битов в байты
def bits_to_bytes(bits):
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]
        byte_value = int("".join(map(str, byte)), 2)
        bytes_list.append(byte_value)
    return bytes_list


# функци] для преобразования из последовательности байтов в ASCII
def bytes_to_ascii(byte_list):
    return "".join(chr(byte) for byte in byte_list)


# расшифровка сообщения и результат до и после преобразований
message_bytes = decrypt_GM(cipher, y, n, p, q)
print("Расшифрованное сообщение (до преобразования ASCII):", message_bytes)

# переделываем список байтов в строку ASCII
message_ascii = bytes_to_ascii(message_bytes)
print("Расшифрованное сооьщение (после преобразования ASCII):", message_ascii)

#ответ
print("Ответ:", message_ascii)