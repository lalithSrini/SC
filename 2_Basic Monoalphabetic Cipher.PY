import string

def generate_cipher_key(shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    key = {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}
    return key

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += key[char]
            else:
                encrypted_message += key[char.lower()].upper()
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_message += reverse_key[char]
            else:
                decrypted_message += reverse_key[char.lower()].upper()
        else:
            decrypted_message += char
    return decrypted_message

def main():
    shift = int(input("Enter the shift value for the cipher: "))
    key = generate_cipher_key(shift)
    choice = input("Encrypt or decrypt? (e/d): ").strip().lower()
    
    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        print("Encrypted message:", encrypt(message, key))
    elif choice == 'd':
        message = input("Enter the message to decrypt: ")
        print("Decrypted message:", decrypt(message, key))
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()