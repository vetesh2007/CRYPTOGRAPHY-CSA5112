# Monoalphabetic Cipher - Simple Letter Frequency Counter

text = input("Enter the encrypted text: ").upper()

freq = {}
for ch in text:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

print("\nLetter frequency in the ciphertext:")
for letter in sorted(freq):
    print(f"{letter} : {freq[letter]}")

# Optional: Show letters by highest frequency
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("\nMost frequent letters (in order):")
for letter, count in sorted_freq:
    print(f"{letter} -> {count}")
