from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

plaintext = input("Enter the plaintext message: ").encode()
key = input("Enter an 8-character secret key: ").encode()

if len(key) != 8:
    raise ValueError("Key must be exactly 8 bytes long for DES.")

padded_plaintext = pad(plaintext, DES.block_size)
cipher = DES.new(key, DES.MODE_ECB)

encrypted_data = cipher.encrypt(padded_plaintext)
print("Encrypted (hex):", encrypted_data.hex())

decrypted_padded_data = cipher.decrypt(encrypted_data)
decrypted_data = unpad(decrypted_padded_data, DES.block_size)
print("Decrypted text:", decrypted_data.decode())
