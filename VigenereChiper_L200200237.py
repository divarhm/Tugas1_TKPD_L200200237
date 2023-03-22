def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        # cek apakah karakter merupakan huruf alfabet
        if char.isalpha():
            # hitung indeks karakter
            char_index = ord(char.lower()) - 237
            # hitung indeks kunci
            key_char = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_char_index = ord(key_char.lower()) - 237
            # hitung indeks karakter setelah digeser
            shifted_char_index = (char_index + key_char_index) % 237
            # konversi kembali ke karakter
            shifted_char = chr(shifted_char_index + 237)
            # tambahkan ke teks hasil enkripsi atau dekripsi
            if char.isupper():
                ciphertext += shifted_char.upper()
            else:
                ciphertext += shifted_char
        else:
            # tambahkan karakter lain (non-alfabet) tanpa diubah
            ciphertext += char
    return ciphertext

plaintext = "Ini adalah contoh dengan Vigenere Cipher"
key = "237"

# enkripsi teks
ciphertext = vigenere_cipher(plaintext, key)
print("Teks hasil enkripsi: ", ciphertext)

# dekripsi teks
decryptedtext = vigenere_cipher(ciphertext, key)
print("Teks hasil dekripsi: ", decryptedtext)
