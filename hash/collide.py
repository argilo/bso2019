#!/usr/bin/env python3

import base64
import hashlib
import urllib.request

server = "localhost:5000"


def hash(message):
    return hashlib.sha256(message).digest()[0:6]


with urllib.request.urlopen(f"http://localhost:5000/?text=foobar") as f:
    cmd = f.read().decode().split('data-command="')[1].split('"')[0]

seen = {}
for x in range(0x2000000):
    h = hash(cmd.replace("foobar", str(x)).encode())
    seen[h] = x

while True:
    target_command = input("Command? ")

    x = 0
    while True:
        command = f"{target_command} ; echo {x} > /dev/null"
        h = hash(command.encode())
        if h in seen:
            break
        x += 1

    with urllib.request.urlopen(f"http://{server}/?text={seen[h]}") as f:
        sig = f.read().decode().split('data-signature="')[1].split('"')[0]

    data = urllib.parse.urlencode({"command": command, "signature": sig}).encode()
    with urllib.request.urlopen(f"http://{server}/api/run_command", data) as f:
        print(base64.b64decode(f.read().split(b",")[1]).decode())
