import sys

sys.setrecursionlimit(1_000_000)

def duree(f):
    def f_bis(*args):
        import time
        t0 = time.time()
        res = f(*args)
        print(time.time() - t0, "s")
        return res
    return f_bis 




class memoize:
    def __init__(self, f):
        self.f = f
        self.dict = {}
    def __call__(self, *args):
        if not args in self.dict:
            self.dict[args] = self.f(*args)
        return self.dict[args]

@memoize
def binome(a, b):
    if a == 0:
        return 1
    elif b == 0:
        return 0
    return binome(a-1, b-1) + binome(a, b-1)


from functools import lru_cache


if 'fibo_tab' not in locals():
    fibo_tab = [1, 1]  # Valeurs d'initialisation de la récurrence

def fibo(n):
    n_max = len(fibo_tab) - 1  # Indice maximal présent
    if n > n_max:
        for i in range(n_max, n):
            fibo_tab.append(fibo_tab[i] + fibo_tab[i-1])
    return fibo_tab[n]


u_0 = 42

if 'u_tab' not in locals() or u(0) != u_0:
    u_tab = [u_0]  # Valeurs d'initialisation de la récurrence

f = lambda x: pow(x, 3, 1298469)

def u(n):
    n_max = len(u_tab) - 1  # Indice maximal présent dans la liste
    if n > n_max:
        for i in range(n_max, n):  # Remplissage jusqu'à la case n
            u_tab.append(f(u_tab[i]))
    return u_tab[n]


from collections import Iterable

est_noeud = lambda e: isinstance(e, Iterable)

def somme_feuilles(arbre):
    if est_noeud(arbre):
        return sum([somme_feuilles(a) for a in arbre])
    else:
        return arbre

import time

l = list(range(10_000))

f = lambda x: x**3 + x**x

import numpy as np

t0 = time.time()
newlist = [np.cumsum(item) for item in range(10000)]
print(time.time() - t0)
t0 = time.time()
newlist = map(np.cumsum, range(10000))
print(time.time() - t0)


























