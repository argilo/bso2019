#!/usr/bin/env python3

import flask
import rsa

public_key, private_key = rsa.keygen(2048)

message = b"A message I want to sign"
signature = rsa.sign(message, private_key)
print(rsa.verify(message, signature, public_key))
print(rsa.verify(message[:-1], signature, public_key))

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
