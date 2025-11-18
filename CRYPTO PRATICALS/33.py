# filename: 33_des_pycryptodome.py
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad8(b): return b + b'\x00' * ((8 - len(b) % 8) % 8)

key = input("Enter 8-byte key hex (16 hex chars) or press Enter to use random: ").strip()
if not key:
    keyb = get_random_bytes(8)
    print("Using random key:", keyb.hex())
else:
    keyb = bytes.fromhex(key)
iv = get_random_bytes(8)
plaintext = input("Enter plaintext: ").encode()
cipher = DES.new(keyb, DES.MODE_CBC, iv)
ct = cipher.encrypt(pad8(plaintext))
print("IV:", iv.hex())
print("Ciphertext (hex):", ct.hex())

# Decrypt
dec = DES.new(keyb, DES.MODE_CBC, iv)
pt = dec.decrypt(ct).rstrip(b'\x00')
print("Decrypted:", pt.decode())
