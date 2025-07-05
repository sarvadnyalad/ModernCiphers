import os
from flask import Flask, render_template, request, jsonify

# Import Fernet and AES handlers
from fernet_handler import encrypt_fernet, decrypt_fernet
from aes_handler import encrypt_aes, decrypt_aes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    data = request.json
    cipher = data.get('cipher')
    text = data.get('text', '')

    try:
        if cipher == 'fernet':
            encrypted = encrypt_fernet(text)
        elif cipher == 'aes':
            encrypted = encrypt_aes(text)
        else:
            return jsonify({'error': 'Unsupported cipher'}), 400
        return jsonify({'result': encrypted})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    data = request.json
    cipher = data.get('cipher')
    text = data.get('text', '')

    try:
        if cipher == 'fernet':
            decrypted = decrypt_fernet(text)
        elif cipher == 'aes':
            decrypted = decrypt_aes(text)
        else:
            return jsonify({'error': 'Unsupported cipher'}), 400
        return jsonify({'result': decrypted})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
