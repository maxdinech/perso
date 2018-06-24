import collections
import functools
import itertools
import time
import math

memoize = functools.lru_cache(maxsize=None)

def duree(f):
    def f_bis(*args):
        t0 = time.time()
        res = f(*args)
        print("durée :", time.time() - t0)
        return res
    return f_bis

t_0 = time.time()

# Constantes
u_0 = 42
m = 2**31 - 1

## Question 1

if 'u_tab' not in locals() or u(0) != u_0:
    u_tab = [u_0]

def u(n):
    n_max = len(u_tab) - 1
    if n > n_max:
        for i in range(n_max, n):
            u_tab.append((16_807 * u_tab[-1] + 17) % m)
    return u_tab[n]


for n in [5, 100, 997]:
    print(u(n) % 101)
print()


## Question 2

@memoize
def v(k, n):
    r = 2**k
    return (u(n) % r) + r


for k in [5, 30, 61]:
    print(v(k, 97 * k % 997) % 101)
print()


## Question 3

def x(p):
    return pow(2, pow(2, p))

def l(n):
    return len(bin(n)) - 2

# Décomposition : n = g + x(p) * d
# Avec 0 <= g < x(p) et 0 < d < x(p)

def Sig(n):
    if n == 0:
        return 0
    if n == 1:
        return u(10) % 97
    # Déterminer p : maximal tel que x(p) <= n
    p = int(math.log2(math.log2(n)))
    d, g = divmod(n, x(p))
    if p % 2 == 0:
        return (Sig(g) + u(30) * Sig(d)) % 97
    else:
        return (Sig(g) + u(20) * Sig(d)) % 97
    
print(Sig(v(1, 10)))
print(Sig(v(2, 20)))
print(Sig(v(32, 30)))
print(Sig(v(61, 40)))
print()


## Question 4

# Parité de h(k) :
# x est toujours pair. Donc parité opposée à celle de k !

def Sig_h(n):
    if n == 0:
        return Sig(1)
    else:
        s = Sig_h(n-1)
        if k % 2 == 0:  # h(k) impair
            return (s + u(20) * s) % 97
        else:
            return (s + u(30) * s) % 97

for k in [0, 2, 4, 8]:
    print(Sig_h(v(k, 7*k)))
print()


## Question 5

#     2 ↑↑ 0 = 1
# 2 ↑↑ (n+1) = 2 ^ (2 ↑↑ n)

@memoize
def gen(k, n):
    if k == 0:
        if u(n) % 7 == 0:
            return (0,)
        else:
            return (1,)
    else:
        k_bis = max(0, k - 1 - (u(n) % 2))
        g = gen(k_bis, (n+1) % 997)
        p = v(k_bis, n)
        d = gen(k_bis, (n+2) % 997)
        if d == 0:
            return (g,)
        else:
            return (g, p, d)

@memoize
def Sig_arbre(a):
    if len(a) == 1:
        f = a[0]
        if f == 0 or f == 1:
            return Sig(f)
        else:
            return Sig_arbre(f)
    else:
        g, p, d = a
        if p % 2 == 0:
            return (Sig_arbre(g) + u(30) * Sig_arbre(d)) % 97
        else:
            return (Sig_arbre(g) + u(20) * Sig_arbre(d)) % 97

print(Sig_arbre(gen(6, 35)))
print(Sig_arbre(gen(8, 45)))
print(Sig_arbre(gen(10, 55)))
print(Sig_arbre(gen(12, 65)))
print(Sig_arbre(gen(14, 75)))
print()


## Question 6

@memoize
def x_bis_dec(p):
    if p == 0:
        return 1,
    else:
        q = dec(p)
        xx = x_bis_dec(q)
        return (xx, q, xx)

@memoize
def dec(a):
    if len(a) == 1:
        if a[0] == 1:
            return 0,
        else:
            raise "réduction de zéro impossible"
    else:
        g, p, d = a
        if g != 0:
            return (dec(g), p, d)
        elif g == 0 and d == 1:
            return x_bis_dec(p)
        elif g == 0 and d != 1:
            return (x_bis_dec(p), p, dec(d))

for k in [6, 16, 26]:
    print(Sig_arbre(dec(gen(k, 19*k % 997))))
print()


## Question 6


@memoize
def inc(a, p_sup=float('inf')):
    if len(a) == 1:
        if a[0] == 0:
            return 1,
        if a[0] == 1:
            return ((0,), 0, (1,))
    else:
        g, p, d = a
        try:
            g_bis = inc(g, p)
            return (g_bis, p, d)
        except:
            try:
                d_bis = inc(d, p)
                return (g, p, d_bis)
            except:
                if p+1 < p_sup:
                    return ((0,), p+1, (1,))
                else:
                    raise "pas possible"

def arbr(n):
    a = 0,
    for i in range(n):
        a = inc(a)
    return a

for k in [6, 7, 16]:
    print(Sig_arbre(inc(gen(k, 17*k % 997))))
print()


## Question 8

def compare(a1, a2):
    if len(a1) == len(a2) == 1:
        return 1 if a1[0] > a2[0] else (0 if a1[0] == a2[0] else -1)
    else:
        if len(a1) < len(a2):
            return -1
        elif len(a1) > len(a2):
            return 1
        else:
            g1, p1, d1 = a1
            g2, p2, d2 = a2
            # Comparaison de p
            delta = 1 if p1 > p2 else (0 if p1 == p2 else -1)
            if delta != 0:
                return delta
            # Comparaison de d
            delta = compare(d1, d2)
            if delta != 0:
                return delta
            # Comparaison de d
            # Comparaison de g
            delta = compare(g1, g2)
            return delta

for k in [6, 8, 16]:
    print(compare(gen(k, 29*k % 997), gen(k, 31*k % 997)))
print()





















print("\nDurée totale :", time.time() - t_0, "sec")

