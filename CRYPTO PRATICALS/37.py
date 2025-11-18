# filename: 37_monoalphabetic_topn.py
import random, math
from collections import Counter

ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def score_text(text):
    freq = Counter(c for c in text.upper() if c.isalpha())
    score = 0
    for i,(c,_) in enumerate(freq.most_common()):
        if i < len(ENGLISH_FREQ_ORDER) and c == ENGLISH_FREQ_ORDER[i]:
            score += (len(freq)-i)
    return score

def random_key():
    letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    perm=letters[:]
    random.shuffle(perm)
    return dict(zip(letters,perm))

def apply_key(text,key):
    out=[]
    for ch in text:
        if ch.upper() in key and ch.isalpha():
            mapped=key[ch.upper()]
            out.append(mapped.lower() if ch.islower() else mapped)
        else:
            out.append(ch)
    return ''.join(out)

def tweak_key_swap(key):
    a,b = random.sample(list(key.keys()),2)
    nk = key.copy()
    nk[a], nk[b] = nk[b], nk[a]
    return nk

def solve(ciphertext, top_n=10, restarts=200, iters=2000):
    candidates=[]
    for _ in range(restarts):
        key=random_key()
        plain=apply_key(ciphertext,key)
        s=score_text(plain)
        for _ in range(iters):
            k2 = tweak_key_swap(key)
            p2 = apply_key(ciphertext,k2)
            s2 = score_text(p2)
            if s2 > s or random.random() < 0.001:
                key, s, plain = k2, s2, p2
        candidates.append((s, plain))
    candidates.sort(reverse=True)
    return candidates[:top_n]

if __name__=='__main__':
    ct = input("Enter ciphertext: ")
    topn = int(input("Top how many results? "))
    results = solve(ct, top_n=topn)
    for i,(s,p) in enumerate(results,1):
        print(f"\nOption {i} (score {s}):\n{p}")
