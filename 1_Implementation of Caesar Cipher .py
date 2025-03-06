def caesar_cipher(text, shift):
    ans = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            ans += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            ans += char  # Append non-alphabetic characters unchanged
    return ans

# Define input values
plaintext = "HELLO WORLD"
n = 1

# Encrypt the plaintext
encrypted_text = caesar_cipher(plaintext, n)

# Print results
print(f"Plain Text is: {plaintext}")
print(f"Shift pattern is: {n}")
print(f"Cipher Text is: {encrypted_text}")
