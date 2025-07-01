import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Import Fernet handlers from the separate module
from ciphers.fernet_handler import encrypt_fernet, decrypt_fernet

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Home route — renders the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Encrypt endpoint — handles encryption based on selected cipher
@app.route('/encrypt', methods=['POST'])
def encrypt_text():
    data = request.json
    cipher = data.get('cipher')
    text = data.get('text', '')

    try:
        if cipher == 'fernet':
            # Delegate encryption to Fernet handler module
            encrypted = encrypt_fernet(text)
            return jsonify({'result': encrypted})
        else:
            return jsonify({'error': 'Unsupported cipher'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Decrypt endpoint — handles decryption based on selected cipher
@app.route('/decrypt', methods=['POST'])
def decrypt_text():
    data = request.json
    cipher = data.get('cipher')
    text = data.get('text', '')

    print("🔍 Decrypt request received:")
    print(f"cipher = {cipher}")
    print(f"text = {text}")

    try:
        if cipher == 'fernet':
            decrypted = decrypt_fernet(text)
            return jsonify({'result': decrypted})
        else:
            return jsonify({'error': 'Unsupported cipher'}), 400
    except Exception as e:
        print("❌ Decryption failed:", str(e))  # Add this line
        return jsonify({'error': str(e)}), 400


# Run the app locally on port 5000
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
