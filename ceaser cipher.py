text = input("Enter text: ")
shift = int(input("Enter shift: "))
mode = input("Encrypt or Decrypt (e/d): ")

if mode == 'd':
    shift = -shift  # reverse shift for decryption

result = ""
for c in text:
    if c.isupper():
        result += chr((ord(c) - 65 + shift) % 26 + 65)
    elif c.islower():
        result += chr((ord(c) - 97 + shift) % 26 + 97)
    else:
        result += c

print("Result:", result)
