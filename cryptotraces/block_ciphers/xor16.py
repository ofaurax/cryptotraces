
from cryptotraces.block_ciphers import interface

class Xor16(interface.BlockCipher):

    def __init__(self):
        self.blockLength = 16
        self.keyLength = 16
        self.data = list(range(0, 16))
        self.key = list(range(0, 16))

    def encrypt(self):
        print(self.data)
        for i in range(0, self.blockLength):
            self.data[i] ^= self.key[i]

    def decrypt(self):
        self.encrypt()
    

