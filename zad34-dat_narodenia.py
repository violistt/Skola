import sys
from collections import defaultdict
input = sys.stdin.readline

ziaci = [i.strip().split() for i in open("ziaci.txt", 'r')]
d = {1: "januar", 2: "februar", 3: "marec", 4: "april", 5: "maj", 6: "jun", 7: "jul", 8: "august", 9: "september", 10: "oktober", 11: "november", 12: "december"}
mesiac = defaultdict(lambda: [])
for cislo, priez, meno in ziaci:
    m = int(cislo[2 : 4]) # mesiac
    if (m > 12): # Je to zena
        m -= 50
    datum = str(str(int(cislo[4 : 6])) + '.' + str(m) + '.19' + cislo[0 : 2])
    mesiac[d[m]].append((datum, priez, meno))
for i in range(1, 13):
    if (not d[i] in mesiac):
        print(f"{d[i]}:")
    else:
        print(f"{d[i]}:") # Nazov mesiaca
        m = sorted(mesiac[d[i]])
        for datum, priez, meno in m:
            print(datum, priez, meno)
