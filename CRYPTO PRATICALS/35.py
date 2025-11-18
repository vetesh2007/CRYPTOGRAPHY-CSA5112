# filename: 35_one_time_vigenere.py
import random, string

def encrypt_otv(plain, key_stream):
    res = []
    for i,ch in enumerate(plain.upper()):
        if ch.isalpha():
            shift = key_stream[i]
            c = chr(((ord(ch)-65 + shift) % 26) + 65)
            res.append(c)
        else:
            res.append(ch)
    return ''.join(res)

def decrypt_otv(cipher, key_stream):
    res=[]
    for i,ch in enumerate(cipher.upper()):
        if ch.isalpha():
            shift = key_stream[i]
            p = chr(((ord(ch)-65 - shift) % 26) + 65)
            res.append(p)
        else:
            res.append(ch)
    return ''.join(res)

plain = input("Enter plaintext: ")
n = len([c for c in plain if c.isalpha()]) or 1
ks = [random.randrange(0,26) for _ in range(len(plain))]
cipher = encrypt_otv(plain, ks)
print("Key stream (numbers):", ks)
print("Ciphertext:", cipher)
print("Recovered:", decrypt_otv(cipher, ks))
