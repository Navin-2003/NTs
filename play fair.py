from pycipher import Playfair

# 1. Prepare a 25-letter key (A-Z without J) from a base key
def prepare_key(base_key):
    base_key = base_key.upper().replace('J', 'I').replace(' ', '')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is excluded
    key = ""
    # Add letters from base key (ignore duplicates)
    for char in base_key:
        if char not in key and char in alphabet:
            key += char
    # Add remaining letters from alphabet
    for char in alphabet:
        if char not in key:
            key += char
    return key

# 2. Define the base key and plaintext
base_key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")


# 3. Prepare the key and plaintext
key = prepare_key(base_key)
plaintext = plaintext.upper().replace('J', 'I')  # Replace J with I

# 4. Initialize the Playfair cipher with the prepared key
cipher = Playfair(key)

# 5. Encrypt and decrypt
encrypted = cipher.encipher(plaintext)
decrypted = cipher.decipher(encrypted)

# 6. Display results
print("play fair Key:", key)
print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
