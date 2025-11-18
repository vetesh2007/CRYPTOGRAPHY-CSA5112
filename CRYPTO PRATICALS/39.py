# 39. Additive (Caesar) Cipher – Frequency Attack

from collections import Counter

# Standard English letter frequency table
ENGLISH_FREQ = {
    'E': 12.0, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
    'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
    'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
    'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
    'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10,
    'Z': 0.07
}

def score_text(text):
    score = 0
    for char in text.upper():
        if char in ENGLISH_FREQ:
            score += ENGLISH_FREQ[char]
    return score

def decrypt_caesar(cipher, shift):
    result = ""
    for c in cipher:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base - shift) % 26 + base)
        else:
            result += c
    return result

cipher = input("Enter ciphertext: ")
top_n = int(input("How many top plaintexts to display? "))

results = []

for shift in range(26):
    plaintext = decrypt_caesar(cipher, shift)
    score = score_text(plaintext)
    results.append((score, shift, plaintext))

# Sort by score highest first
results.sort(reverse=True)

print("\nTop possible plaintexts:")
for i in range(top_n):
    print(f"\nRank {i+1}:")
    print(f"Shift = {results[i][1]}")
    print(f"Plaintext = {results[i][2]}")
