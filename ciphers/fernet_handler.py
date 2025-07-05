from cryptography.fernet import Fernet

# Static Fernet key for testing — must be 32 url-safe base64-encoded bytes
# You can generate one using: Fernet.generate_key()
FERNET_KEY = b'8ByKslmLEYzslU9Bkp1PTpI0cnRlz3Vt-qY5hOEP2oc='  # Replace with your secure key

fernet = Fernet(FERNET_KEY)

# Encrypt plaintext using Fernet
def encrypt_fernet(plaintext: str) -> str:
    return fernet.encrypt(plaintext.encode()).decode()

# Decrypt ciphertext using Fernet
def decrypt_fernet(ciphertext: str) -> str:
    return fernet.decrypt(ciphertext.encode()).decode()
