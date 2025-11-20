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

output:
Enter the encrypted text: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

Letter frequency in the ciphertext:

A : 1
B : 3
C : 1
D : 1
E : 2
F : 1
G : 1
H : 1
I : 1
J : 1
K : 1
L : 4
M : 1
N : 1
O : 2
P : 1
Q : 2
R : 2
S : 1
T : 1
U : 1
V : 1
W : 1
X : 1
Y : 1
Z : 1

Most frequent letters (in order):
L -> 4
B -> 3
Q -> 2
E -> 2
R -> 2
O -> 2
N -> 1
F -> 1
Z -> 1
H -> 1
Y -> 1
T -> 1
K -> 1
C -> 1
U -> 1
G -> 1
J -> 1
M -> 1
P -> 1
W -> 1
X -> 1
I -> 1
A -> 1
S -> 1
V -> 1

