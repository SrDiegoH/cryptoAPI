import base64

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

from flask import request, Flask, jsonify

import json

app = Flask(__name__)

@app.route('/')
def root():
    key = 'TEST_KEY'.encode("UTF-8")
    text = 'Working'.encode("UTF-8")
    text_encrypted = encrypt(text, key)

    return decrypt(text_encrypted, key)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text').encode("UTF-8")
    password = request.form.get('key').encode("UTF-8")

    return encrypt(text, password)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form.get('text').encode("UTF-8")
    password = request.form.get('key').encode("UTF-8")

    return decrypt(text, password)

def encrypt(text, password):
    key = SHA256.new(password).digest()
    IV = Random.new().read(AES.block_size)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    padding = AES.block_size - len(text) % AES.block_size

    text += bytes([padding]) * padding
    data = IV + encryptor.encrypt(text)

    return base64.b64encode(data).decode("UTF-8")

def decrypt(text, password):
    source = base64.b64decode(text)
    key = SHA256.new(password).digest()
    IV = source[:AES.block_size]

    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])

    padding = data[-1]

    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")

    return data[:-padding]

if __name__ == '__main__':
    app.run()