# filename: 31_cmac_subkeys.py
"""
CMAC subkey generation (RFC 4493).
- For block size 128 bits (AES): Rb = 0x87
- For block size 64 bits (e.g. DES / 3DES): Rb = 0x1B
Generates K1 and K2 from key by:
  L = E_k(0^blocksize)
  K1 = L << 1  XOR (Rb) if MSB(L)==1
  K2 = K1 << 1 XOR (Rb) if MSB(K1)==1
"""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def xor_bytes(a,b):
    return bytes(x^y for x,y in zip(a,b))

def left_shift_one(bitstring: bytes) -> bytes:
    out = bytearray(len(bitstring))
    carry = 0
    for i in range(len(bitstring)-1, -1, -1):
        b = bitstring[i]
        out[i] = ((b << 1) & 0xFF) | carry
        carry = (b >> 7) & 0x01
    return bytes(out)

def generate_cmac_subkeys_aes(key: bytes):
    block_size = 16  # bytes -> 128 bits
    cipher = AES.new(key, AES.MODE_ECB)
    L = cipher.encrypt(b'\x00' * block_size)
    Rb = bytes([0]*15 + [0x87])  # 128-bit Rb = 0x87 in low-order byte
    K1 = left_shift_one(L)
    if (L[0] & 0x80):  # MSB is 1
        K1 = xor_bytes(K1, Rb)
    K2 = left_shift_one(K1)
    if (K1[0] & 0x80):
        K2 = xor_bytes(K2, Rb)
    return L, K1, K2

def generate_cmac_subkeys_blocksize64(key48_bytes):
    # Example for 64-bit block ciphers: Rb = 0x1B (single low-order byte)
    # This function assumes an external 64-bit encryption function is available.
    # Here we simulate by AES on 8-byte block for demonstration.
    from Crypto.Cipher import DES
    cipher = DES.new(key48_bytes, DES.MODE_ECB)
    L = cipher.encrypt(b'\x00' * 8)
    Rb = bytes([0]*7 + [0x1B])
    K1 = left_shift_one(L)
    if (L[0] & 0x80):
        K1 = xor_bytes(K1, Rb)
    K2 = left_shift_one(K1)
    if (K1[0] & 0x80):
        K2 = xor_bytes(K2, Rb)
    return L, K1, K2

if __name__ == "__main__":
    print("CMAC subkey generator (AES-128 example).")
    key = input("Enter AES-128 key hex (32 hex chars) or press Enter for random: ").strip()
    if not key:
        keyb = get_random_bytes(16)
        print("Using random key (hex):", keyb.hex())
    else:
        keyb = bytes.fromhex(key)
    L, K1, K2 = generate_cmac_subkeys_aes(keyb)
    print("L  =", L.hex())
    print("K1 =", K1.hex())
    print("K2 =", K2.hex())
    print("\n(a) Constants: Rb(128-bit) = 0x87 ; Rb(64-bit) = 0x1B")
    print("b) Why left shift & XOR works: left shift multiplies the field element by x (GF(2^n)).")
    print("If MSB was 1, shifting would overflow the field; XOR with Rb implements modular reduction by the polynomial (makes result remain in field).")
