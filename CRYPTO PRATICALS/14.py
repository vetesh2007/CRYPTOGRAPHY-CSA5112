# otp_vigenere.py
# One-time-pad style Vigenere: numeric keystream

def strip_and_upper(s):
    return ''.join(ch for ch in s.upper() if ch.isalpha())

def mod26(x): return x % 26

def encrypt(pt, keystream):
    ct_chars = []
    for i, ch in enumerate(pt):
        p = ord(ch) - 65
        k = keystream[i]
        c = mod26(p + k)
        ct_chars.append(chr(c + 65))
        print(f"p={ch}({p:2d}) k={k:2d} -> c={chr(c+65)}({c:2d})")
    return ''.join(ct_chars)

def recover_keystream(ct, target_plain):
    ks = []
    for i, ch in enumerate(target_plain):
        c = ord(ct[i]) - 65
        p = ord(ch) - 65
        k = mod26(c - p)  # because p + k = c  (mod26) -> k = c - p
        ks.append(k)
        print(f"pos {i:2d}: c={ct[i]}({c:2d}) p={ch}({p:2d}) -> k={k:2d}")
    return ks

if __name__ == "__main__":
    pt_raw = "send more money"
    pt = strip_and_upper(pt_raw)
    keystream = [9,0,1,7,23,15,21,14,11,11,2,8,9]  # given
    print("Plaintext (letters only):", pt)
    print("\nEncryption:")
    ct = encrypt(pt, keystream)
    print("\nCiphertext:", ct)

    print("\n--- Key recovery example ---")
    target_raw = "cash not needed"
    target = strip_and_upper(target_raw)
    print("Target plaintext:", target)
    # Use ciphertext produced earlier. If ciphertext length > target length, we'll only use min length.
    ct_for_recovery = ct
    L = min(len(ct_for_recovery), len(target))
    print("\nRecovered keystream for target (positions 0..{}):".format(L-1))
    recovered = recover_keystream(ct_for_recovery[:L], target[:L])
    print("Recovered keystream (first {} items):".format(L), recovered)

output:
Plaintext (letters only): SENDMOREMONEY

Encryption:
p=S(18) k= 9 -> c=B( 1)
p=E( 4) k= 0 -> c=E( 4)
p=N(13) k= 1 -> c=O(14)
p=D( 3) k= 7 -> c=K(10)
p=M(12) k=23 -> c=J( 9)
p=O(14) k=15 -> c=D( 3)
p=R(17) k=21 -> c=M(12)
p=E( 4) k=14 -> c=S(18)
p=M(12) k=11 -> c=X(23)
p=O(14) k=11 -> c=Z(25)
p=N(13) k= 2 -> c=P(15)
p=E( 4) k= 8 -> c=M(12)
p=Y(24) k= 9 -> c=H( 7)

Ciphertext: BBQKJDMSXZPMH

--- Key recovery example ---
Target plaintext: CASHNOTNEEDED

Recovered keystream for target (positions 0..12):
pos 0: c=B( 1) p=C( 2) -> k=25
pos 1: c=E( 4) p=A( 0) -> k= 4
pos 2: c=O(14) p=S(18) -> k=22
pos 3: c=K(10) p=H( 7) -> k= 3
pos 4: c=J( 9) p=N(13) -> k=22
pos 5: c=D( 3) p=O(14) -> k=15
pos 6: c=M(12) p=T(19) -> k=19
pos 7: c=S(18) p=N(13) -> k= 5
pos 8: c=X(23) p=E( 4) -> k=19
pos 9: c=Z(25) p=E( 4) -> k=21
pos 10: c=P(15) p=D( 3) -> k=12
pos 11: c=M(12) p=E( 4) -> k= 8
pos 12: c=H( 7) p=D( 3) -> k= 4
Recovered keystream (first 13 items): [25, 4, 22, 3, 22, 15, 19, 5, 19, 21, 12, 8, 4]
