import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import constant_time


def _hash(message):
    return hashlib.sha256(message).digest()[0:6]


def _pkcs1v15_pad(message, key_bytes):
    hashed_message = _hash(message)
    padding_len = key_bytes - len(hashed_message) - 3
    padding = bytes([0x00, 0x01] + [0xff] * padding_len + [0x00])
    return padding + hashed_message


def keygen(key_size):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return public_key, private_key


def sign(message, private_key):
    d = private_key.private_numbers().d
    n = private_key.public_key().public_numbers().n
    key_bytes = private_key.key_size // 8
    padded_hash = _pkcs1v15_pad(message, key_bytes)
    return pow(int.from_bytes(padded_hash, byteorder='big'), d, n).to_bytes(key_bytes, byteorder='big')


def verify(message, signature, public_key):
    e = public_key.public_numbers().e
    n = public_key.public_numbers().n
    key_bytes = public_key.key_size // 8
    padded_hash = pow(int.from_bytes(signature, byteorder='big'), e, n).to_bytes(key_bytes, byteorder='big')
    expected_padded_hash = _pkcs1v15_pad(message, key_bytes)
    return constant_time.bytes_eq(padded_hash, expected_padded_hash)
