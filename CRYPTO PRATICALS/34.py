# filename: 34_ecb_cbc_cfb_modes.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad1zeros(data, block_size):
    pad_len = (block_size - (len(data) % block_size)) or block_size
    return data + b'\x80' + b'\x00' * (pad_len - 1)

def unpad1zeros(padded):
    i = len(padded)-1
    while i>=0 and padded[i]==0:
        i-=1
    if i>=0 and padded[i]==0x80:
        return padded[:i]
    raise ValueError("Invalid padding")

key = get_random_bytes(16)
bs = 16
pt = input("Enter plaintext: ").encode()
pt_padded = pad1zeros(pt, bs)

# ECB
ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = ecb.encrypt(pt_padded)
print("ECB ct hex:", ct_ecb.hex())
print("ECB recovered:", unpad1zeros(ecb.decrypt(ct_ecb)).decode())

# CBC
iv = get_random_bytes(bs)
cbc = AES.new(key, AES.MODE_CBC, iv)
ct_cbc = cbc.encrypt(pt_padded)
dec_cbc = AES.new(key, AES.MODE_CBC, iv).decrypt(ct_cbc)
print("CBC ct hex:", ct_cbc.hex())
print("CBC recovered:", unpad1zeros(dec_cbc).decode())

# CFB (no padding necessary for CFB in byte-granularity; but we'll use same padded text)
cfb = AES.new(key, AES.MODE_CFB, iv=iv)
ct_cfb = cfb.encrypt(pt)
print("CFB ct hex:", ct_cfb.hex())
print("CFB recovered:", AES.new(key, AES.MODE_CFB, iv=iv).decrypt(ct_cfb).decode())

print("\nMotivation to always pad even if final block is complete:")
print("- Avoid ambiguity when plaintext ends with bytes that match padding pattern.")
print("- Simplifies unpadding (always remove padding block).")
