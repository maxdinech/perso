"""
L ensemble de N entiers distincts, et t un entier.

(E) : x_1 + ... + x_k = t pour les x_i dans L

où chaque élement apparaît au plus une fois dans la somme.
"""

import functools
import time
import sys

blank = lambda x: print('XXX')

sys.setrecursionlimit(10_000)

memoize = functools.lru_cache(maxsize=None)

def duree(f):
    def f_bis(*args):
        t0 = time.time()
        res = f(*args)
        print(time.time() - t0, "s.")
        return res
    return f_bis


u0 = 26
t_0 = time.time()

## Question 1

def v(x, a, m):
    def vv(k):
        if k == 0:
            return x % m
        else:
            return (a * vv(k-1)) % m
    return vv

@memoize
def V(x, a, m, N):
    L = [x % m]
    for k in range(N):
        L.append(a * L[-1] % m)
    return L


print(v(u0, 157, 1009)(5))
print(v(u0, 353, 997)(47))
print(v(u0, 1151, 16381)(86))
print()

## Question 2

def collisions(L1, L2):
    c = 0
    for x in set(L1) & set(L2):
        c += L1.count(x) * L2.count(x)
    return c

def somme_2_coll(s1, C1, s2, C2, t):
    ss2 = {t-x for x in s2}
    c = 0
    for x in s1 & ss2:
        c += C1[x] * C2[t-x]
    return c

def somme_2(L1, L2, t):
    l1 = sorted(list(set(L1)))  # Croissante
    l2 = sorted(list(set(L2)), reverse=True)  # Décroissante
    i, j = 0, 0
    c = 0
    while i < len(l1) and j < len(l2):
        if l1[i] + l2[j] > t:
            j += 1
        elif l1[i] + l2[j] < t:
            i += 1
        else:
            c += L1.count(l1[i]) * L2.count(l2[j])
            i += 1
            j += 1
    return c

def somme_2_sorted(l1, C1, l2, C2, t):
    i, j = 0, 0
    c = 0
    while i < len(l1) and j < len(l2):
        if l1[i] + l2[j] > t:
            j += 1
        elif l1[i] + l2[j] < t:
            i += 1
        else:
            c += C1[l1[i]] * C2[l2[j]]
            i += 1
            j += 1
    return c

L1, L2 = V(u0, 157, 1009, 100), V(u0, 353, 997, 100)
print((collisions(L1, L2), somme_2(L1, L2, 112)))
L1, L2 = V(u0, 157, 1009, 300), V(u0, 353, 997, 300)
print((collisions(L1, L2), somme_2(L1, L2, 233)))
L1, L2 = V(u0, 157, 1009, 500), V(u0, 353, 997, 500)
print((collisions(L1, L2), somme_2(L1, L2, 185)))
print()


## Question 3

import tqdm

def somme_3(L1, L2, L3, t):
    l2 = sorted(list(set(L2)))  # Croissante
    l3 = sorted(list(set(L3)), reverse=True)  # Décroissante
    s2 = set(L2)
    s3 = set(L3)
    C2 = [L2.count(i) for i in range(max(L2)+1)]
    C3 = [L3.count(i) for i in range(max(L3)+1)]
    M = max(L2) + max(L3)
    m = min(L2) + min(L3)
    c = 0
    for x in set(L1):
        if m <= t-x <= M:
            c += L1.count(x) * somme_2_coll(s2, C2, s3, C3, t-x)
    return c

L1, L2, L3 = V(u0, 157, 1009, 100), V(u0, 353, 997, 100), V(13*u0, 157, 1009, 100)
print(duree(somme_3)(L1, L2, L3, 233))

L1, L2, L3 = V(u0, 157, 1009, 300), V(u0, 353, 997, 300), V(24*u0, 157, 1009, 300)
print(duree(somme_3)(L1, L2, L3, 133))

L1, L2 = V(u0, 1151, 16381, 4096), V(67*u0, 1151, 16381, 4096)
L3 = V(33*u0, 1151, 16381, 4096)
print(duree(somme_3)(L1, L2, L3, 48000))

print()

## Question 4


def somme_4(L1, L2, L3, L4, t):
    l1 = sorted(list(set(L1)))  # Croissante
    l2 = sorted(list(set(L2)), reverse=True)  # Décroissante
    l3 = sorted(list(set(L3)))  # Croissante
    l4 = sorted(list(set(L4)), reverse=True)  # Décroissante
    C1 = [L1.count(i) for i in range(max(L1)+1)]
    C2 = [L2.count(i) for i in range(max(L2)+1)]
    C3 = [L3.count(i) for i in range(max(L3)+1)]
    C4 = [L4.count(i) for i in range(max(L4)+1)]
    mg = min(L1) + min(L2)
    Mg = max(L1) + max(L2)
    md = min(L3) + min(L4)
    Md = max(L3) + max(L4)
    c = 0
    for x in range(mg, Mg+1):
        if md <= t-x <= Md:
            c += (somme_2_sorted(l1, C1, l2, C2, x) *
                  somme_2_sorted(l3, C3, l4, C4, t-x))
    return c

def somme_4_bis(L1, L2, L3, L4, t):
    s1 = set(L1)
    s2 = set(L2)
    s3 = set(L3)
    s4 = set(L4)
    C1 = [L1.count(i) for i in range(max(L1)+1)]
    C2 = [L2.count(i) for i in range(max(L2)+1)]
    C3 = [L3.count(i) for i in range(max(L3)+1)]
    C4 = [L4.count(i) for i in range(max(L4)+1)]
    mg = min(L1) + min(L2)
    Mg = max(L1) + max(L2)
    md = min(L3) + min(L4)
    Md = max(L3) + max(L4)
    c = 0
    for x in range(mg, Mg+1):
        if md <= t-x <= Md:
            c += (somme_2_coll(s1, C1, s2, C2, x) *
                  somme_2_coll(s3, C3, s4, C4, t-x))
    return c

    
L1, L2 = V(u0, 157, 1009, 100), V(u0, 353, 997, 100)
L3, L4 = V(13*u0, 157, 1009, 100), V(13*u0, 353, 997, 100)
print(duree(somme_4)(L1, L2, L3, L4, 3876))
print(duree(somme_4_bis)(L1, L2, L3, L4, 3876))

L1, L2 = V(u0, 157, 1009, 300), V(u0, 353, 997, 300)
L3, L4 = V(24*u0, 157, 1009, 300), V(24*u0, 353, 997, 300)
print(duree(somme_4)(L1, L2, L3, L4, 3899))
print(duree(somme_4_bis)(L1, L2, L3, L4, 3899))

L1, L2 = V(u0, 1151, 16381, 4096), V(14*u0, 1151, 16381, 4096)
L3, L4 = V(33*u0, 1151, 16381, 4096), V(67*u0, 1151, 16381, 4096)
print(duree(somme_4)(L1, L2, L3, L4, 65115))
print(duree(somme_4_bis)(L1, L2, L3, L4, 65115))

print()


## Question 5








print("Durée :", time.time() - t_0, "s.")