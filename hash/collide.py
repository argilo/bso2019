#!/usr/bin/env python3

import base64
import hashlib
import shlex
import urllib.request

target_command = "ls"


def hash(message):
    return hashlib.sha256(message).digest()[0:6]


def command(text):
    return f"convert -background lightblue -fill blue -pointsize 40 -size 320x -gravity Center {shlex.quote('caption:' + text)} png:-"


seen = {}

for x in range(0x1000000):
    h = hash(command(str(x)).encode())
    seen[h] = x

x = 0
while True:
    command = f"{target_command} ; echo {x} > /dev/null"
    h = hash(command.encode())
    if h in seen:
        break
    x += 1

with urllib.request.urlopen(f"http://localhost:5000/?text={seen[h]}") as f:
    sig = f.read().decode().split('data-signature="')[1].split('"')[0]

data = urllib.parse.urlencode({"command": command, "signature": sig}).encode()
with urllib.request.urlopen("http://localhost:5000/api/run_command", data) as f:
    output = base64.b64decode(f.read().split(b",")[1]).decode()

print(output)

exit()


x0 = bytes([0] * 6)

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
