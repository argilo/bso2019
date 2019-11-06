#!/usr/bin/env python3

import hashlib

HASH_BYTES = 6


def hash(b):
    return hashlib.sha256(b).digest()[:HASH_BYTES]


x0 = bytes([0] * HASH_BYTES)

tortoise = hash(x0)
hare = hash(hash(x0))

while tortoise != hare:
    tortoise = hash(tortoise)
    hare = hash(hash(hare))

tortoise = x0
while tortoise != hare:
    in1, in2 = tortoise, hare
    tortoise = hash(tortoise)
    hare = hash(hare)

print(in1, in2)
print(hashlib.sha256(in1).hexdigest())
print(hashlib.sha256(in2).hexdigest())

quit()

seen = {}

n = 0
while True:
    in_bytes = n.to_bytes(8, byteorder="big")
    result = hashlib.sha256(in_bytes).digest()[0:6]
    if result in seen:
        print(f"collision: {seen[result]} {in_bytes}")
        print(hashlib.sha256(seen[result]).hexdigest())
        print(hashlib.sha256(in_bytes).hexdigest())
        break
    seen[result] = in_bytes

    n += 1
