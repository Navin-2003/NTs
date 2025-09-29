from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = input("Enter an 8-character secret key: ").encode()
if len(key) != 8:
    raise ValueError("Key must be exactly 8 bytes long for DES.")

cipher = DES.new(key, DES.MODE_ECB)

choice = int(input("Enter 1 to Encrypt or 2 to Decrypt: "))

if choice == 1:
    plaintext = input("Enter the plaintext message: ").encode()
    padded_plaintext = pad(plaintext, DES.block_size)
    encrypted_data = cipher.encrypt(padded_plaintext)
    print("Encrypted (hex):", encrypted_data.hex())

elif choice == 2:
    encrypted_hex = input("Enter the encrypted hex message: ")
    try:
        encrypted_data = bytes.fromhex(encrypted_hex)
    except ValueError:
        print("Invalid hex input.")
        exit()

    decrypted_padded_data = cipher.decrypt(encrypted_data)
    try:
        decrypted_data = unpad(decrypted_padded_data, DES.block_size)
        print("Decrypted text:", decrypted_data.decode())
    except ValueError:
        print("Incorrect decryption or wrong padding.")

else:
    print("Invalid choice!")
