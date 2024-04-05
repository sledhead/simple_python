
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt(plain_text, password):
    salt = get_random_bytes(AES.block_size)
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_GCM)
    cipher_text, tag = cipher.encrypt_and_digest(pad(plain_text, AES.block_size))
    return salt + cipher.nonce + cipher_text + tag

def decrypt(cipher_text, password):
    salt = cipher_text[:AES.block_size]
    nonce = cipher_text[AES.block_size:AES.block_size*2]
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plain_text = unpad(cipher.decrypt(cipher_text[AES.block_size*2:-16]), AES.block_size)
    return plain_text