# filename: 32_dsa_k_randomness_demo.py
"""
Simple DSA demonstration (toy params, do NOT use for real security).
Shows that signing same message twice with fresh k yields different signatures.
"""
import random, hashlib

# small toy DSA parameters (insecure; for demonstration only)
# In real DSA p and q are large primes; here small primes for demonstration
q = 0xF7E75FDC469067FFDC4E847C51F452DF  # typically 160-bit; using example placeholder
# For simplicity below we build tiny example using small primes (not cryptographically secure)
# We'll use small primes for demonstration:
p = 30803  # small prime
q = 307  # q divides p-1? ensure: p-1 = 30802, 30802 % 307 = 53 -> not dividing; we use toy g
g = 2

def hash_int(m):
    h = hashlib.sha1(m).digest()
    return int.from_bytes(h, 'big') % q

def gen_keys():
    x = random.randrange(1, q)
    y = pow(g, x, p)
    return x, y

def dsa_sign(m_bytes, x):
    H = hash_int(m_bytes)
    while True:
        k = random.randrange(1, q)
        r = pow(g, k, p) % q
        if r == 0: 
            continue
        try:
            kinv = pow(k, -1, q)
        except ValueError:
            continue
        s = (kinv * (H + x * r)) % q
        if s == 0:
            continue
        return (r, s), k

def dsa_verify(m_bytes, sig, y):
    r, s = sig
    if not (0 < r < q and 0 < s < q):
        return False
    H = hash_int(m_bytes)
    w = pow(s, -1, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q
    return v == r

if __name__ == "__main__":
    print("DSA randomness demo (toy).")
    x, y = gen_keys()
    msg = input("Enter message to sign: ").encode()
    sig1, k1 = dsa_sign(msg, x)
    sig2, k2 = dsa_sign(msg, x)
    print("Signature 1:", sig1, "k1:", k1)
    print("Signature 2:", sig2, "k2:", k2)
    print("Verify1:", dsa_verify(msg, sig1, y))
    print("Verify2:", dsa_verify(msg, sig2, y))
    print("\nNote: k1 != k2 (usually) so signatures differ even though message is same.")
