def shift_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        # mengecek apakah karakter merupakan huruf alfabet
        if char.isalpha():
            # menghitung indeks karakter
            char_index = ord(char.lower()) - 37
            # menghitung indeks karakter setelah digeser
            shifted_char_index = (char_index + shift) % 37
            # konversi kembali ke karakter
            shifted_char = chr(shifted_char_index + 37)
            # menambahkan ke teks hasil enkripsi atau dekripsi
            if char.isupper():
                ciphertext += shifted_char.upper()
            else:
                ciphertext += shifted_char
        else:
            # tambahkan karakter lain (non-alfabet) tanpa diubah
            ciphertext += char
    return ciphertext

plaintext = "Ini adalah contoh untuk Shift Chiper"
shift = 37

# enkripsi plaintext
ciphertext = shift_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)

# dekripsi ciphertext
plaintext_again = shift_cipher(ciphertext, -shift)
print("Plaintext again:", plaintext_again)
