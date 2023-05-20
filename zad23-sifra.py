import sys
input = sys.stdin.readline

k = list(map(int, input().split()))[:-1]
m = len(k)
s = input()[:-1]
n = len(s)
_s = [' '] * n
medzier = 0
for i in range(n):
    if (s[i] == ' '):
        medzier += 1
        continue
    pozicia = ord(s[i]) - 96
    posun = k[i % m - medzier]
    if (pozicia + posun > 26):
        pozicia = (pozicia + posun) % 26
    else:
        pozicia += posun
    _s[i] = chr(pozicia + 96)
print(''.join(_s))
