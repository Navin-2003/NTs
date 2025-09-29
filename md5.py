import hashlib

# Get input from user
user_input = input("Enter a string to hash: ")

# Hash the input (bytes)
md5_bytes = hashlib.md5(user_input.encode())

# Show byte representation
print("Byte equivalent of hash:", md5_bytes.digest())

# Show hexadecimal representation
print("Hexadecimal equivalent of hash:", md5_bytes.hexdigest())
