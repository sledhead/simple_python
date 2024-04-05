
from AES_GCM import *

#send in simple text to encrypt.
my_special_text = "little sheep on the farm"
cool_password = "cool1234snow5678"

ret_stuff = encrypt(my_special_text.encode(), cool_password)

print(ret_stuff)


plain_stuff = decrypt(ret_stuff, cool_password)

print(plain_stuff)
print(plain_stuff.decode())