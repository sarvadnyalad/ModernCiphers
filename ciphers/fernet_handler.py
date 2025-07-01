import os 
from cryptography.fernet import Fernet # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()
fernet = Fernet(os.getenv("FERNET_KEY"))    # Fernet key is mentioned in .env file

# Encryption of fernet cipher 
def encrypt_fernet(plaintext: str) -> str:      
    return fernet.encrypt(plaintext.encode()).decode()

# Decryption of fernet cipher 
def decrypt_fernet(ciphertext: str) -> str:
    return fernet.decrypt(ciphertext.encode()).decode()

key = os.getenv("FERNET_KEY")
if not key:
    raise ValueError("FERNET_KEY not found in .env file or environment variables")
fernet = Fernet(key)
