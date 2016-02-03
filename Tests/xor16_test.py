
import cryptotraces.BlockCipher.Xor16

c = cryptotraces.BlockCipher.Xor16()
l = c.get_blocklength()
lk = c.get_keylength()
c.load_key(range(1,lk+1))
c.load_data(range(0,l))
print c.trace()
c.encrypt()
print c.trace()
c.decrypt()
print c.trace()
    

