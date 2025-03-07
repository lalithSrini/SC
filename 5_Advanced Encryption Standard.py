#AES#
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)  # Initialize AES cipher in CBC mode
    iv = cipher.iv  # Get initialization vector
    padded_text = pad(plaintext.encode(), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return iv + encrypted_text  # Store IV + Ciphertext together

def aes_decrypt(encrypted_text, key):
    iv = encrypted_text[:AES.block_size]  # Extract IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(encrypted_text[AES.block_size:]), AES.block_size)
    return decrypted_text.decode()

# Example Usage
key = get_random_bytes(16)  # 16 bytes key for AES-128
plaintext = "Lalith Srinivas"

encrypted_text = aes_encrypt(plaintext, key)
decrypted_text = aes_decrypt(encrypted_text, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text.hex()}")
print(f"Decrypted: {decrypted_text}")