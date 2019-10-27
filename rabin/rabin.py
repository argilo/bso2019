#!/usr/bin/env python3

import os
import random


def is_prime(n):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(40):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def next_prime_3mod4(n):
    while True:
        if is_prime(n):
            return n
        n += 4


def random_prime_3mod4(bits):
    x = int.from_bytes(os.urandom(bits // 8), byteorder="big")
    return next_prime_3mod4(x | (1 << (bits - 1)) | 3)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def crt(a, b, m, n):
    return ((a * n * mul_inv(n, m)) + (b * m * mul_inv(m, n))) % (m * n)


def mod_sqrt(a, p, q):
    root_p = pow(a % p, (p + 1) // 4, p)
    root_q = pow(a % q, (q + 1) // 4, q)
    return (
        crt(root_p, root_q, p, q),
        crt(p - root_p, root_q, p, q),
        crt(root_p, q - root_q, p, q),
        crt(p - root_p, q - root_q, p, q)
    )


def rabin_keygen(bits):
    p = random_prime_3mod4(bits // 2)
    q = random_prime_3mod4(bits // 2)
    return p, q


def rabin_encrypt(message, n):
    m = int.from_bytes(message.encode(), byteorder="big")
    return pow(m, 2, n)


def rabin_decrypt(ciphertext, p, q):
    roots = mod_sqrt(ciphertext, p, q)
    for root in roots:
        message = root.to_bytes(2048 // 8, byteorder="big")
        if message[0:4] == bytes([0] * 4):
            return message
    return None


p, q = rabin_keygen(2048)
c = rabin_encrypt("Hello world!", p * q)
print(rabin_decrypt(c * 4, p, q))
