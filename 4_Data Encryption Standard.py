#DES#
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB) 
    padded_text = pad(plaintext.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)
    return decrypted_text.decode()

key = b'8bytekey'  
plaintext = "Lalith Srinivas"

encrypted_text = des_encrypt(plaintext, key)
decrypted_text = des_decrypt(encrypted_text, key)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text.hex()}")
print(f"Decrypted: {decrypted_text}")