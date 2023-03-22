def encrypt(key, plaintext):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt(key, ciphertext):
    plaintext = [''] * (len(ciphertext) // key)
    for col in range(key):
        pointer = col
        for row in range(len(ciphertext) // key):
            plaintext[row] += ciphertext[pointer]
            pointer += key
    return ''.join(plaintext)

# Contoh penggunaan
plaintext = "Ini adalah contoh dari Transposition Chiper"
key = 3

# Enkripsi pesan
ciphertext = encrypt(key, plaintext)
print("Pesan yang telah dienkripsi: ", ciphertext)

# Dekripsi pesan
decrypted = decrypt(key, ciphertext)
print("Pesan asli yang telah didekripsi: ", decrypted)
