
import interface

class Xor16(interface.BlockCipher):

    def __init__(self):
        self.blockLength = 16
        self.keyLength = 16
        self.data = range(0, 16)
        self.key = range(0, 16)

    def encrypt(self):
        for i in range(0, self.blockLength):
            self.data[i] ^= self.key[i]

    def decrypt(self):
        self.encrypt()

if __name__ == '__main__':
    c = Xor16()
    l = c.get_blocklength()
    lk = c.get_keylength()
    c.load_key(range(1,lk+1))
    c.load_data(range(0,l))
    print(c.trace())
    c.encrypt()
    print(c.trace())
    c.decrypt()
    print(c.trace())
    

