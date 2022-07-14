## the first line of output is private key 

from random import randbytes
import base64
import curve25519

WG_KEY_LEN = 32
WG_KEY_LEN_BASE64 = int(((((WG_KEY_LEN) + 2) / 3) * 4 + 1))

def encodePrivKey(key):
    return base64.b64encode(key)


privkey = randbytes(WG_KEY_LEN)
encodedPrivKey = encodePrivKey(privkey)


pubkey = curve25519.curve25519_base(privkey)
encodedPubKey = base64.b64encode(pubkey)
print(encodedPrivKey.decode("ASCII"))
print(encodedPubKey.decode("ASCII"))