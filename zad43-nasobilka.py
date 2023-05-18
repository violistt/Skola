import sys
import random
from collections import deque

q = deque()
a = []
for _ in range(10):
    n = random.randint(1, 10)
    m = random.randint(1, 10)
    q.append((n, m, 0))
    a.append((f"{n} * {m} = {n * m}"))
with open("nasobilka_vystup.txt", 'w') as file:
    for vyraz in a:
        file.write("%s\n" % vyraz)
bodov = 0
for i in range(10):
    x, y, t = q[0]
    v = int(input(f"Kolko je {x} * {y}? "))
    if (v == x * y and not t):
        bodov += 1
    else:
        q.append((x, y, 1))
    q.popleft()
print(bodov)
