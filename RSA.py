from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Step 1: Generate RSA key pair
key_size = 2048  # You can change this if needed
key = RSA.generate(key_size)
private_key = key
public_key = key.publickey()

# Step 2: Input plaintext
plaintext = input("Enter the plaintext message: ").encode()  # Convert to bytes

# Step 3: Encrypt using the public key
cipher_encrypt = PKCS1_OAEP.new(public_key)
ciphertext = cipher_encrypt.encrypt(plaintext)
# Convert to base64 for readability
ciphertext_b64 = base64.b64encode(ciphertext).decode()
print("\nEncrypted text (base64):", ciphertext_b64)

# Step 4: Decrypt using the private key
cipher_decrypt = PKCS1_OAEP.new(private_key)
# Convert back from base64
ciphertext_bytes = base64.b64decode(ciphertext_b64)
decrypted_text = cipher_decrypt.decrypt(ciphertext_bytes).decode()
print("\nDecrypted text:", decrypted_text)
