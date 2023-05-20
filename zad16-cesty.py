import sys
input = sys.stdin.readline

cesty = [i.strip().split() for i in open("cesty.txt", 'r')]
n = len(cesty)
dlzka = 0
x, y, m = -1, -1, 0
for i, cesta in enumerate(cesty):
    for j, c in enumerate(cesta):
        w = int(c)
        dlzka += w
        if (w > m):
            m = w
            x, y = i, j
print(f"Celkova dlzka cestnej siete: {dlzka // 2}")
print(f"Najviac vzdialene mesta: {x + 1}-{y + 1} ({m} km)")
