import numpy as np

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def text_to_numbers(text):
    return [ord(c) - ord('a') for c in text.lower().replace(" ", "")]

def numbers_to_text(nums):
    return ''.join([chr(n % 26 + ord('a')) for n in nums])

def encrypt(text, key):
    text += 'x' if len(text) % 2 else ''
    nums = text_to_numbers(text)
    res = []
    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        res.extend((key @ pair % 26).flatten())
    return numbers_to_text(res)

def decrypt(text, key):
    det = int(round(np.linalg.det(key))) % 26
    det_inv = mod_inverse(det, 26)
    if det_inv is None:
        return "Key not invertible"
    adj = np.array([[key[1,1], -key[0,1]], [-key[1,0], key[0,0]]]) % 26
    inv_key = (det_inv * adj) % 26
    nums = text_to_numbers(text)
    res = []
    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        res.extend((inv_key @ pair % 26).flatten())
    return numbers_to_text(res)

# Main
choice = input("E=Encrypt, D=Decrypt: ").upper()
key = np.array(list(map(int, input("Enter 4 numbers for 2x2 key: ").split()))).reshape(2,2)

if choice == 'E':
    print("Encrypted:", encrypt(input("Plaintext: "), key))
elif choice == 'D':
    print("Decrypted:", decrypt(input("Ciphertext: "), key))
else:
    print("Invalid choice!")
