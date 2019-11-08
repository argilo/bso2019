#!/usr/bin/env python3

import base64
import shlex
import subprocess
import flask
import rsa

public_key, private_key = rsa.keygen(1024)

app = flask.Flask(__name__)


@app.route("/")
def home():
    text = flask.request.args.get("text", "")
    command = f"convert -background lightblue -fill blue -pointsize 40 -size 320x -gravity Center {shlex.quote('caption:' + text)} png:-"
    signature = rsa.sign(command.encode(), private_key).hex()
    return flask.render_template("index.html", text=text, command=command, signature=signature)


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

    png = subprocess.check_output(command, shell=True)
    result = b"data:image/png;base64," + base64.b64encode(png)
    return flask.Response(result, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
