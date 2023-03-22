import string
import random

def generate_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return dict(zip(string.ascii_lowercase, alphabet))

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += key[char.lower()]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += list(key.keys())[list(key.values()).index(char.lower())]
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan :
key = generate_key()
plaintext = "contoh dari penggunaan subtitution chiper"
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)

print("Key:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
