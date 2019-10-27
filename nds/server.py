#!/usr/bin/env python3

import nds
import os
import socketserver


class MyTCPHandler(socketserver.StreamRequestHandler):
    flag = "flag{xxxxxxxxxxxxxxxxxxxxxxxxxx}".encode()
    key = os.urandom(256)

    def handle(self):
        input, output = self.rfile, self.wfile
        flag_encrypted = nds.cipher(self.flag, self.key)

        try:
            output.write("Welcome!".encode())
            output.write(("\n" + flag_encrypted.hex()).encode())

            while True:
                output.write("\nInput? ".encode())
                data = input.readline().decode().strip()

                try:
                    data_bytes = bytes.fromhex(data)
                except ValueError:
                    output.write("Invalid hex input.\n".encode())
                    continue

                if len(data_bytes) % 16 != 0:
                    output.write("Input must be a multiple of 16 bytes.\n".encode())
                    continue

                bad = False
                for x in range(0, len(data_bytes), 16):
                    if data_bytes[x:x+16] in [flag_encrypted[0:16], flag_encrypted[16:32]]:
                        output.write("You're not allowed to decrypt that!\n".encode())
                        bad = True
                        break
                if bad:
                    continue

                output.write((nds.cipher(data_bytes, self.key).hex() + "\n").encode())

        except (BrokenPipeError, ConnectionResetError):
            pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999

    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
