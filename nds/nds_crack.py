#!/usr/bin/env python3

import nds
import os
import socket

HOST = "oldschool.area52.airforce"
PORT = 9999


def read_until(s, msg):
    buffer = b""
    while not buffer.endswith(msg):
        buffer += s.recv(1024)
    return buffer


def nds_cipher(s, msg):
    s.send((msg.hex() + "\n").encode())
    data = read_until(s, b"input? ").decode()
    return bytes.fromhex(data.split("\n")[0])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = read_until(s, b"input? ").decode()
ciphertext = bytes.fromhex(data.split("\n")[4])

cracked_key = [0] * 256
for key_byte in range(256):
    chosen_plaintext = [0] * 8
    for x in range(8):
        chosen_plaintext.append(((key_byte & (0x80 >> x)) << x) | 0x0f)
    u = bytes(chosen_plaintext)
    target = nds_cipher(s, u)

    big_plaintext = b""
    for x in range(256):
        cracked_key[key_byte] = x
        test = u[8:16] + bytes([a ^ b for a, b in zip(u[0:8], nds.f(u[8:16], bytes(cracked_key)))])
        big_plaintext += test

    big_ciphertext = nds_cipher(s, big_plaintext)
    x = big_ciphertext.index(target[0:8]) // 16
    cracked_key[key_byte] = x
    print(f"Key byte {key_byte} is 0x{x:02x}.")

print(nds.cipher(ciphertext, bytes(cracked_key)).decode())
