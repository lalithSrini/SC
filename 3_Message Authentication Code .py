import hashlib

def generate_hashes(input_string):
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    sha512_hash = hashlib.sha512(input_string.encode()).hexdigest()
    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    print(f"Input: {input_string}")
    print("The hexadecimal equivalent of SHA256 is :",sha256_hash)
    # print(sha256_hash)
    print("The hexadecimal equivalent of SHA512 is :",sha512_hash)
    # print(sha512_hash)
    print("The hexadecimal equivalent of SHA1 is :",sha1_hash)
    # print(sha1_hash)

str1 = "GeekforGeeks"
generate_hashes(str1)