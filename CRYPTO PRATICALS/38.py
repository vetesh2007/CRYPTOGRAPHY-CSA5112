# filename: 38_hill_known_plaintext.py
"""
Recover 2x2 Hill cipher key given two plaintext-ciphertext block pairs.
Solve: K * P_matrix = C_matrix (mod 26) => K = C * P^{-1} mod 26
"""
def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b,a%b)
    return (g, y1, x1 - (a//b)*y1)

def modinv(a,m):
    g,x,y = egcd(a,m)
    if g!=1: raise Exception("No inverse")
    return x % m

def matrix_inv_2x2(mat):
    a,b,c,d = mat
    det = (a*d - b*c) % 26
    det_inv = modinv(det,26)
    inv = [ (d*det_inv)%26, (-b*det_inv)%26, (-c*det_inv)%26, (a*det_inv)%26 ]
    return [x%26 for x in inv]

def matrix_mul_2x2(A,B):
    return [
        (A[0]*B[0] + A[1]*B[2]) % 26,
        (A[0]*B[1] + A[1]*B[3]) % 26,
        (A[2]*B[0] + A[3]*B[2]) % 26,
        (A[2]*B[1] + A[3]*B[3]) % 26
    ]

# Input: two plaintext blocks (each length 2) and corresponding ciphertext blocks
print("Provide two plaintext 2-letter blocks and corresponding ciphertext 2-letter blocks.")
p1 = input("Plain1 (2 letters): ").upper().strip()
p2 = input("Plain2 (2 letters): ").upper().strip()
c1 = input("Cipher1 (2 letters): ").upper().strip()
c2 = input("Cipher2 (2 letters): ").upper().strip()

P = [ (ord(p1[0])-65), (ord(p2[0])-65), (ord(p1[1])-65), (ord(p2[1])-65) ]  # columns
C = [ (ord(c1[0])-65), (ord(c2[0])-65), (ord(c1[1])-65), (ord(c2[1])-65) ]

try:
    P_inv = matrix_inv_2x2(P)
    K = matrix_mul_2x2(C, P_inv)
    print("Recovered 2x2 key matrix (row-major):")
    print(f"[{K[0]} {K[1]}]\n[{K[2]} {K[3]}]")
except Exception as e:
    print("Failed to invert P matrix mod 26. Error:", e)
    print("Need plaintext pairs that form invertible matrix mod 26.")
