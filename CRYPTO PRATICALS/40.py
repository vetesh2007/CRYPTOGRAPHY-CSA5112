# 40. Monoalphabetic Substitution Cipher – Frequency Attack

from collections import Counter
import string

ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def build_freq_map(cipher):
    counter = Counter([c for c in cipher.upper() if c.isalpha()])
    sorted_cipher_letters = ''.join([item[0] for item in counter.most_common()])
    mapping = {}

    for i, c in enumerate(sorted_cipher_letters):
        if i < len(ENGLISH_FREQ_ORDER):
            mapping[c] = ENGLISH_FREQ_ORDER[i]
    return mapping

def apply_mapping(cipher, mapping):
    result = ""
    for c in cipher:
        if c.upper() in mapping:
            if c.isupper():
                result += mapping[c.upper()]
            else:
                result += mapping[c.upper()].lower()
        else:
            result += c
    return result

def refine_mapping(mapping):
    # Generate variations by swapping letters (simple heuristic)
    variations = []
    letters = list(mapping.values())
    keys = list(mapping.keys())

    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            newmap = mapping.copy()
            newmap[keys[i]] = letters[j]
            newmap[keys[j]] = letters[i]
            variations.append(newmap)

    return variations

cipher = input("Enter ciphertext: ")
top_n = int(input("How many top plaintexts to show? "))

initial_map = build_freq_map(cipher)
initial_plain = apply_mapping(cipher, initial_map)

# Generate variations
maps = refine_mapping(initial_map)

results = [(initial_plain.count('E'), initial_plain)]

for m in maps:
    p = apply_mapping(cipher, m)
    score = sum(p.upper().count(ch) for ch in "ETAOIN")
    results.append((score, p))

results.sort(reverse=True)

print("\nTop plaintext guesses:")
for i in range(top_n):
    print(f"\nRank {i+1}:")
    print(results[i][1])
