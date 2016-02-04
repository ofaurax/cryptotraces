
from cryptotraces.block_ciphers import xor16

c = xor16.Xor16()
l = c.get_blocklength()
lk = c.get_keylength()
c.load_key(list(range(1,lk+1)))
c.load_data(list(range(0,l)))
print(c.trace())
c.encrypt()
print(c.trace())
c.decrypt()
print(c.trace())
    
#fail
raise AssertionErrors
