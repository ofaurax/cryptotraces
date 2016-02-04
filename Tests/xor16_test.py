
import pprint
from cryptotraces.block_ciphers import xor16

c = xor16.Xor16()
l = c.get_blocklength()
lk = c.get_keylength()
ref = list(range(0,l))

c.load_key(list(range(1,lk+1)))
c.load_data(ref)

pp = pprint.PrettyPrinter()
pp.pprint(c.trace())
c.encrypt()
pp.pprint(c.trace())
c.decrypt()
pp.pprint(c.trace())

#fail -> raise AssertionError
assert ref == c.trace()['data']
