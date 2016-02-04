

class BlockCipher:

    def __init__(self):
        self.blockLength = 0
        self.keyLength = 0
        self.data = []
        self.key = []
        
    def encrypt(self):
        raise NotImplementedError

    def decrypt(self):
        raise NotImplementedError

    def trace(self):
        return {'data': self.data, 'key': self.key}

    def get_blocklength(self):
        return self.blockLength

    def get_keylength(self):
        return self.keyLength

    def load_key(self, key):
        self.key = key

    def load_data(self, data):
        self.data = data
