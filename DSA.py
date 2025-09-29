from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# 1. Generate a DSA key pair (private & public)
key = DSA.generate(2048)
public_key = key.publickey()

# 2. Message to sign
message = input("Enter a message to sign: ").encode()

# 3. Sign the message with the private key
hash_obj = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)
print("Signature (hex):", signature.hex())

# 4. Verify the signature with the public key
hash_obj2 = SHA256.new(message)
verifier = DSS.new(public_key, 'fips-186-3')
try:
    verifier.verify(hash_obj2, signature)
    print("Signature is valid.")
except ValueError:
    print("Signature is invalid.")
