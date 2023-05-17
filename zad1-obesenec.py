import sys
import random
from os import system
input = sys.stdin.readline

slova = [i.strip() for i in open("obesenec.txt", 'r').readlines()]
slovo = list(random.choice(slova))
n = len(slovo)
_s = []
for i in range(n):
    _s.append('.' if (i == n - 1) else '. ')
for i in range(10):
    system('clear')
    print(f"Zostavajucich pokusov: {10 - i}\n")
    print(*_s)
    s = input()[:-1]
    for j in range(n):
        if (slovo[j] == s[0]):
            slovo[j] = '$'
            _s[j] = s[0]
    if (set(slovo) == {'$'}):
        system('clear')
        print(*_s)
        print(f"\nGratulujem, Uhadol si na {i}. pokus :D")
        sys.exit()
print("Prehral si :(")
