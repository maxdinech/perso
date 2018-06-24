import sys
import time
sys.setrecursionlimit(10_000)
from functools import lru_cache
from collections import namedtuple

def duree(f):
    def f_bis(*args):
        t0 = time.time()
        res = f(*args)
        print("temps :", time.time() - t0, "s")
        return res
    return f_bis


Maison = namedtuple('Maison', 'x y')
Bureau = namedtuple('Bureau', 'x y cout')

u_0 = 1
a, b, c, d, e, f = 263, 269, 271, 281, 283, 293

## Question 1

@lru_cache(maxsize=None)
def u(t, i=0, j=0):
    if i == 0 and j == 0:
        if t == 0:
            return u_0
        return (a * u(t-1, i, j)) % b
    elif j == 0:
        return (c * u(t, i-1, j)) % d
    else:
        return (e * u(t, i, j-1)) % f

print(u(2))
print(u(1000))
print(u(1000, 4))
print(u(1000, 4, 2001))
print()

## Question 2

def maisons(t, n):
    return [Maison(u(t, 1, 2*i) - f//2, u(t, 1, 2*i + 1) - f//2) for i in range(1, n+1)]

def dist(M, B=Bureau(0, 0, 0)):
    return abs(M.x - B.x) + abs(M.y - B.y)

def maisons_proches(t, n):
    c = 0
    for M in maisons(t, n):
        c += 1*(dist(M) <= 200)
    return c

print(maisons_proches(1, 10))
print(maisons_proches(2, 100))
print(maisons_proches(3, 1000))
print()

## Question 3

def bureaux(t, m):
    return [Bureau(u(t, 2, 2*j) - f//2, u(t, 2, 2*j + 1) - f//2, 10 * u(t, 3, j))
            for j in range(1, m+1)]

def surface(t, m):
    Bx = bureaux(t, m)
    x_min = min([B.x for B in Bx])
    x_max = max([B.x for B in Bx])
    y_min = min([B.y for B in Bx])
    y_max = max([B.y for B in Bx])
    return (y_max - y_min) * (x_max - x_min)

print(surface(1, 10))
print(surface(2, 100))
print(surface(3, 1000))
print()

## Question 4

def bin(x):
    if x == 0:
        return []
    return bin(x // 2) + [x % 2]

def dec(tab):
    return sum([2**i * x for i, x in enumerate(tab[::-1])])

def B_m(I, m):
    tab = [1*(i in I) for i in range(m, 0, -1)]
    return dec(tab)

def I_m(x, m):
    tab = bin(x)
    tab = [0]*(m-len(tab)) + tab
    return [m+1-i for i in range(1, m+1) if tab[i-1]]

print(max(I_m(u(10) % 1024, 10)))
print(max(I_m(u(11) % 1024, 10)))
print(max(I_m(u(12) % 1024, 10)))
print()

## Question 5

def G(t, m, n):
    return maisons(t, n), bureaux(t, m)

def Cout(t, m, n, I):
    Ms, Bx = G(t, m, n)
    Bx = [B for (i, B) in enumerate(Bx, 1) if i in I]
    c = 0
    for B in Bx:
        c += B.cout
    for M in Ms:
        d = float('inf')
        for B in Bx:
            d = min(d, dist(M, B))
        c += d
    return c

def Cout_min(t, m, n):
    Ms, Bx = G(t, m, n)
    C = float('inf')
    x_max = 2**(m+1)
    for x in range(1, x_max + 1):
        I = I_m(x, m)
        Bxx = [B for (i, B) in enumerate(Bx, 1) if i in I]
        c = 0
        for B in Bxx:
            c += B.cout
        for M in Ms:
            d = float('inf')
            for B in Bxx:
                d = min(d, dist(M, B))
            c += d
            if c > C:
                break
        else:
            C = min(C, c)
    return C


# On donne à chaque maison la liste croissante des bureaux les plus proches !
def Cout_min_bis(t, m, n):
    Ms, Bx = G(t, m, n)
    indices = list(range(1, m+1))
    plus_proches = []
    for M in Ms:
        dist_M = lambda i: dist(M, Bx[i-1])
        plus_proches.append(sorted(indices, key=dist_M))
    C = float('inf')
    x_max = 2**(m+1)
    for x in range(1, x_max + 1):
        I = I_m(x, m)
        Bxx = [B for (i, B) in enumerate(Bx, 1) if i in I]
        c = 0
        for B in Bxx:
            c += B.cout
        for i in range(n):
            for j in plus_proches[i]:
                if j in I:
                    c += dist(Ms[i], Bx[j-1])
                    break
            if c > C:
                break
        else:
            C = min(C, c)
    return C
        
print(duree(Cout_min_bis)(1, 10, 20))
print(duree(Cout_min_bis)(2, 11, 30))
print(duree(Cout_min_bis)(3, 12, 100))
print(duree(Cout_min_bis)(4, 15, 1000))
print()

## Question 6














