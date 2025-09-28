import math

def prepare_text(text, rows):
    text = text.upper().replace(" ", "")
    # Padding with 'X' to fill matrix properly
    while len(text) % rows != 0:
        text += 'X'
    return text

def encrypt_rail_fence(text, rows):
    text = prepare_text(text, rows)
    cols = len(text) // rows

    # Create matrix and fill row-wise
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = text[index]
            index += 1

    # Read column-wise to generate ciphertext
    cipher = ''
    for c in range(cols):
        for r in range(rows):
            cipher += matrix[r][c]
    return cipher

def decrypt_rail_fence(cipher, rows):
    cols = len(cipher) // rows

    # Create matrix and fill column-wise
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = cipher[index]
            index += 1

    # Read row-wise to recover plaintext
    plain = ''
    for r in range(rows):
        for c in range(cols):
            plain += matrix[r][c]

    # Remove padding X if present
    return plain.rstrip('X')

# === Main Program ===
choice = input("Type E to Encrypt or D to Decrypt: ").strip().upper()
rows = int(input("Enter number of rows: "))

if choice == 'E':
    plaintext = input("Enter the plaintext: ").strip()
    encrypted = encrypt_rail_fence(plaintext, rows)
    print("Encrypted Text:", encrypted)

elif choice == 'D':
    ciphertext = input("Enter the ciphertext: ").strip().upper()
    decrypted = decrypt_rail_fence(ciphertext, rows)
    print("Decrypted Text:", decrypted)

else:
    print("Invalid choice! Please enter E or D.")
