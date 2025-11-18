# filename: 36_affine_caesar.py
import math

def encrypt_affine(plain, a, b):
    out = []
    for ch in plain.upper():
        if ch.isalpha():
            p = ord(ch)-65
            out.append(chr(((a*p + b) % 26) + 65))
        else:
            out.append(ch)
    return ''.join(out)

def decrypt_affine(cipher, a, b):
    if math.gcd(a,26) != 1:
        raise ValueError("a not invertible modulo 26; decryption impossible.")
    a_inv = pow(a, -1, 26)
    out=[]
    for ch in cipher.upper():
        if ch.isalpha():
            c = ord(ch)-65
            out.append(chr(((a_inv*(c - b)) % 26) + 65))
        else:
            out.append(ch)
    return ''.join(out)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
plain = input("Enter plaintext: ")
print("Encrypting...")
ct = encrypt_affine(plain, a, b)
print("Cipher:", ct)
try:
    pt = decrypt_affine(ct, a, b)
    print("Decrypted:", pt)
except ValueError as e:
    print("Decryption failed:", e)
    print("Example failure: a=2,b=3 -> E(0)=E(13)=3 shows not one-to-one.")
