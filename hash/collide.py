#!/usr/bin/env python3

import hashlib

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
