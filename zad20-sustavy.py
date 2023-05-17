import sys
input = sys.stdin.readline

with open('cis-sustavy.txt', 'r') as file:
    for line in file:
        n, zaklad = line.split()
        zaklad = int(zaklad)
        # desiat = int(n, zaklad) # Bud to takto okasles
        # Alebo si to napises sam
        _n = n
        desiat = 0
        mocnina = 0
        while (_n):
            try:
                k = int(_n[-1])
            except:
                k = ord(_n[-1]) - 55
            desiat += k * (zaklad ** mocnina)
            mocnina += 1
            _n = _n[:-1]
        print(f"({n}){zaklad} = {desiat}")
