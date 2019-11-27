#!/usr/bin/env python3

import rabin
import socketserver


class MyTCPHandler(socketserver.StreamRequestHandler):
    private_key = rabin.keygen(1024)
    public_key = private_key.public_key()

    def handle(self):
        input, output = self.rfile, self.wfile
        message = b"foo bar baz"
        target_ciphertext = self.public_key.encrypt(message)

        try:
            output.write(f"o hai! my public key is:\n\n{self.public_key.n}\n\n".encode())
            output.write("shall we play a game?\n\n".encode())
            output.write(f"{target_ciphertext}\n\n".encode())

            while True:
                output.write("ciphertext? ".encode())
                data = input.readline().decode().strip()

                try:
                    ciphertext = int(data)
                except ValueError:
                    output.write("invalid integer input!\n\n".encode())
                    continue

                if ciphertext < 0 or ciphertext >= self.public_key.n:
                    output.write("invalid ciphertext!\n\n".encode())
                    continue

                if ciphertext == target_ciphertext:
                    output.write("nice try!\n\n".encode())
                    continue

                plaintext = self.private_key.decrypt(ciphertext)
                if plaintext:
                    output.write(f"{plaintext}\n\n".encode())
                else:
                    output.write("failed to decrypt!\n\n".encode())


        except (BrokenPipeError, ConnectionResetError):
            pass


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 7979

    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
