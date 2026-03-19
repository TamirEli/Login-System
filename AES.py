import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()


def get_user_string():
    user_input = input("Enter a string: ")
    return user_input

def divided_into_blocks():




user_string = get_user_string()
print("You entered:", user_string)
