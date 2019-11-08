#!/usr/bin/env python3

import os
import flask
import rsa

public_key, private_key = rsa.keygen(1024)

app = flask.Flask(__name__)


@app.route("/")
def home():
    text = flask.request.args.get("text", "")
    signature = rsa.sign(text.encode(), private_key).hex()
    return flask.render_template("index.html", text=text, signature=signature)


@app.route("/api/run_command", methods=["POST"])
def run_command():
    command = flask.request.form.get("command")
    signature = flask.request.form.get("signature")

    if command is None:
        return "command parameter is mandatory", 400
    if signature is None:
        return "signature parameter is mandatory", 400

    try:
        signature = bytes.fromhex(signature)
    except ValueError:
        return "signature must be hexadecimal", 400

    if not rsa.verify(command.encode(), signature, public_key):
        return "bad signature", 401

    os.system(command)
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
