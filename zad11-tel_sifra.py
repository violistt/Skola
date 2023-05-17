import sys
from collections import defaultdict
input = sys.stdin.readline

s = input()[:-1]
kod = {' ': 0, 'A': 1, 'B': 11, 'C': 111, 'D': 2, 'E': 22, 'F': 222, 'G': 3, 'H': 33, 'I': 333, 'J': 4, 'K': 44, 'L': 444, 'M': 5, 'N': 55, 'O': 555, 'P': 6, 'Q': 66, 'R': 666, 'S': 7, 'T': 77, 'U': 777, 'V': 8, 'W': 88, 'X': 888, 'Y': 9, 'Z': 99}
pocet = defaultdict(lambda: 0)
for c in s:
    print(kod[c], end = ' ')
    for k in str(kod[c]):
        pocet[k] += 1
print()
pocet = sorted(list(pocet.items()), key = lambda k: -k[1])
res = [pocet[0][0]]
for c, p in pocet:
    if (p != pocet[0][0]):
        break
    res.append(c)
print("Najčastejšie zvolené políčka:", *res)
