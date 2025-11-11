import string

def keyword_cipher_alphabet(keyword):
    keyword = "".join(sorted(set(keyword.upper()), key=keyword.upper().index))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = keyword + "".join([ch for ch in alphabet if ch not in keyword])
    return cipher_alphabet

def encrypt_keyword_cipher(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alphabet = keyword_cipher_alphabet(keyword)
    mapping = {alphabet[i]: cipher_alphabet[i] for i in range(26)}

    result = ""
    for ch in plaintext.upper():
        if ch in mapping:
            result += mapping[ch]
        else:
            result += ch
    return result

# Example
keyword = "CIPHER"
plaintext = input("Enter plaintext: ")
ciphertext = encrypt_keyword_cipher(plaintext, keyword)
print("Ciphertext:", ciphertext)
