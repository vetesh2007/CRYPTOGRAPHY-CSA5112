def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0
    for char in plaintext.upper():
        if char.isalpha():
            shift = (ord(key[key_index]) - 65)
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

# Example
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

output:
Enter plaintext: ATTACKATDAWN
Enter key: LEMON
Ciphertext: LXFOPVEFRNHR

