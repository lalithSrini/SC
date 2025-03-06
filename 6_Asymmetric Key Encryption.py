import random
from math import gcd

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.choice([i for i in range(2, phi) if gcd(i, phi) == 1])
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return (message ** e) % n

def decrypt(ciphertext, private_key):
    d, n = private_key
    return (ciphertext ** d) % n

# Given values
p = 53
q = 59
message = 89

# Generate keys
public_key, private_key = generate_keys(p, q)

# Encrypt the message
encrypted_message = encrypt(message, public_key)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, private_key)

# Print results
print(f"Encrypted message is {encrypted_message}")
print(f"Decrypted message is {decrypted_message}")
