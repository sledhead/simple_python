
#will use this code to generate a user defined key.
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

key = get_random_bytes(32) # 32 bytes * 8 = 256 bits (1 byte = 8 bits)
print(key)

#store in a salt which will be used with a user password
salt = key # Salt you generated
password = 'password123' # Password provided by the user, can use input() to get this

new_key = PBKDF2(password, salt, dkLen=32) # Your key that you can encrypt with
print(new_key)