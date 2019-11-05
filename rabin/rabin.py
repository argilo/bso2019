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


class RabinPrivateKey:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.crt_coeff_1 = p * mul_inv(p, q)
        self.crt_coeff_2 = q * mul_inv(q, p)

    def _crt(self, a, b):
        return (a * self.crt_coeff_1 + b * self.crt_coeff_2) % (self.p * self.q)

    def _mod_sqrt(self, c):
        root_p = pow(c % self.p, (self.p + 1) // 4, self.p)
        root_q = pow(c % self.q, (self.q + 1) // 4, self.q)
        return (
            self._crt(root_p, root_q),
            self._crt(self.p - root_p, root_q),
            self._crt(root_p, self.q - root_q),
            self._crt(self.p - root_p, self.q - root_q)
        )

    def decrypt(self, ciphertext):
        roots = self._mod_sqrt(ciphertext)
        for root in roots:
            redundant_message = root.to_bytes(2048 // 8, byteorder="big")
            if redundant_message[-2:-1] == redundant_message[-1:]:
                message = redundant_message[:-1]
                return message
        return None

    def public_key(self):
        return RabinPublicKey(self.p * self.q)


class RabinPublicKey:
    def __init__(self, n):
        self.n = n

    def encrypt(self, message):
        redundant_message = message + message[-1:]
        m = int.from_bytes(redundant_message, byteorder="big")
        return pow(m, 2, self.n)


def rabin_keygen(bits):
    p = random_prime_3mod4(bits // 2)
    q = random_prime_3mod4(bits // 2)
    return RabinPrivateKey(p, q)


private_key = rabin_keygen(2048)
public_key = private_key.public_key()

n = 0
for x in range(100000):
    c = public_key.encrypt(("Hello world!" + str(x)).encode())
    message = private_key.decrypt(c)
    if message[0:4] != bytes([0] * 4):
        n += 1
        print(x, x / n)
