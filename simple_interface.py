
from AES_GCM import *

#send in simple text to encrypt.
my_special_text = "little sheep on the farm"
cool_password = "cool1234"

ret_stuff = encrypt(my_special_text, cool_password)

print(ret_stuff)
