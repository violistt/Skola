import sys
from collections import defaultdict

freq = [i.strip().split() for i in open("frekv.txt", 'r')]
for f in freq:
    if (len(f) == 1):
        f.insert(0, ' ')
    f[1] = int(f[1])
sifra = [i.strip() for i in open("sifro.txt", 'r')]
d = defaultdict(lambda: 0)
for s in sifra:
    for c in s:
        d[c] += 1
freq.sort(key = lambda k: k[1])
cnt = sorted(d.items(), key = lambda k: k[1])
a = defaultdict(lambda: '')
for i in range(len(freq)):
    a[cnt[i][0]] = freq[i][0]
desif = []
for s in sifra:
    d = []
    for c in s:
        d.append(a[c])
    desif.append(d)
print("Desifrovany text:")
for d in desif:
    print(''.join(d))
with open('kluc.txt', 'w') as kluc:
    for znak, povodny in a.items():
        kluc.write(f"{znak} {povodny}\n")
