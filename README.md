# 🔐 Modern Ciphers

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask-green.svg)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/Frontend-TailwindCSS-blueviolet)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web-based cryptography tool for encrypting and decrypting text using **modern ciphers** like **Fernet**, **AES**, **RSA**, and **ChaCha20**. Built with a Python Flask backend and a Tailwind CSS-powered dashboard frontend.

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the App](#running-the-app)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- 🔐 **Fernet**: AES-CBC with HMAC-based symmetric encryption.
- 🔐 **AES**: Block cipher with configurable mode, padding, and IV.
- 🔐 **RSA**: Asymmetric encryption using public/private key pair.
- 🔐 **ChaCha20**: Fast and secure stream cipher alternative.
- 🖥️ **UI**: Responsive Tailwind dashboard with live encryption/decryption.

---

## 🧰 Tech Stack

- **Backend**: Flask (Python 3.8+), `cryptography`, `pycryptodome`
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Key Management**: Fernet key, RSA key pair (PEM files)

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- OpenSSL (for RSA key generation)
- Git (optional)

### 📥 Installation

```bash
# Clone the repository
git clone <repository-url>
cd "Modern ciphers"

# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 🔐 Environment Variables

Create a `.env` file in the project root:

```env
FLASK_APP=app.py
FLASK_ENV=development
FERNET_KEY=<your-generated-fernet-key>
RSA_PRIVATE_KEY=keys/private.pem
RSA_PUBLIC_KEY=keys/public.pem
```

- **Generate a Fernet key** in Python:
  ```python
  from cryptography.fernet import Fernet
  print(Fernet.generate_key().decode())
  ```

- **Generate RSA keys** using OpenSSL:
  ```bash
  openssl genpkey -algorithm RSA -out keys/private.pem -pkeyopt rsa_keygen_bits:2048
  openssl rsa -pubout -in keys/private.pem -out keys/public.pem
  ```

### ▶️ Running the App

```bash
flask run
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🗂️ Project Structure

```
Modern ciphers/
├── app.py               # Flask app entry point
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
├── templates/
│   └── index.html       # HTML dashboard
├── static/
│   ├── style.css
│   └── script.js
└── keys/
    ├── private.pem
    └── public.pem
```

---

## 🧪 Usage

1. Select your cipher from the dropdown.
2. Enter plaintext or ciphertext.
3. Enter required key (and IV if needed).
4. Click **Encrypt** or **Decrypt**.
5. View the result instantly.

---

## 🛣️ Roadmap

- [x] Fernet encryption/decryption
- [ ] AES (CBC mode) implementation
- [ ] RSA encryption/decryption
- [ ] ChaCha20 support
- [ ] Unit tests for ciphers
- [ ] Dockerize the application

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes, features, or improvements.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> © 2025 – Made with 🛡️ and Flask
