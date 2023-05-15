import sys
from math import log2
input = sys.stdin.readline

vylety = [riadok.strip().split() for riadok in open("cyklovylety.txt", 'r')]
for vylet in vylety:
    ciel = []
    datum = None
    vzdialenost = None
    cas = 0
    hodiny, minuty = 0, 0
    for j, udaj in enumerate(vylet):
        if (j == 0):
            datum = udaj
        elif (j == 1):
            vzdialenost = float(udaj)
        elif (j == 2):
            cas = float(udaj)
            hodiny = int(float(udaj) / 60)
            minuty = int(float(udaj) % 60)
            if (int(log2(minuty)) + 1 == 1):
                minuty = '0' + str(minuty)
        if (j > 2):
            ciel.append(udaj)
    ciel = ' '.join(ciel)
    priemerna_rychlost = "%.1f" % ((vzdialenost * 1000 / (cas * 60)) * 3.6)
    print(f"{datum} {vzdialenost} {hodiny}:{minuty} {priemerna_rychlost} {ciel}")
