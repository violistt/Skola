import sys
from collections import defaultdict
input = sys.stdin.readline

sutaziaci = [i.split() for i in open("skok_do_dialky.txt", 'r').readlines()]
krajiny = defaultdict(lambda: 0)
vykony = []
for meno, krajina, v1, v2, v3, v4, v5 in sutaziaci:
    krajiny[krajina] += 1
    vykony.append((meno, krajina, max(v1, v2, v3, v4, v5)))
for krajina, pocet in krajiny.items():
    print(f"{krajina}, počet súťažíacich: {pocet}")
print()
vykony.sort(key = lambda k: (-int(k[2]), k[0])) # Utriedime podla vykonov a mien
naj = vykony[0][2]
print("Víťazi:")
for meno, krajina, vykon in vykony:
    if (vykon != naj):
        break
    print(meno, krajina, vykon)
