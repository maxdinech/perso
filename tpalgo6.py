import itertools
from collections import namedtuple

u0 = 42
m = 2**31 - 1

## Question 1

if 'u_tab' not in locals() or u(0) != u0:
    u_tab = [u0]

def u(n):
    n_max = len(u_tab) -1
    if n > n_max:
        for i in range(n_max, n):
            u_tab.append(16_807 * u_tab[-1] % m)
    return u_tab[n]

print(u(10) % 1234)
print(u(10_000) % 1234)
print(u(1_000_000) % 1234)
print()


## Question 2

Turing = namedtuple("Turing", "Q delta")

def T(n, t):
    Q = list(range(n))
    delta = {}
    for q, x in itertools.product(Q, {0, 1}):
        z = t + 8*q + 4*x
        q_bis = None if u(z+1) % n == 0 else u(z) % n
        delta[(q, x)] = (q_bis, u(z+2) % 2, 2 * (u(z+3) % 2) - 1)
    return Turing(Q, delta)


print(T(2, 2).delta)
print(T(2, 3).delta)
print(T(3, 4).delta)
print()


## Question 3

def terminales(k):
    C = 0
    for t in range(1_000):
        c = 0
        delta = T(4, t).delta
        for x in delta.values():
            if x[0] == None:
                c += 1
            if c > k:
                break
        else:
            if c == k:
                C += 1
    return C

print(terminales(0))
print(terminales(1))
print(terminales(3))
print()

## Question 4

from collections import defaultdict

Config = namedtuple("Config", "B p q")

def Opt(M, C):
    if C.q == None:
        return None
    else:
        q_bis, y, d = M.delta[(C.q, C.B[C.p])]
        B_bis = C.B.copy()
        B_bis[C.p] = y
        return Config(B_bis, C.p + d, q_bis)
    
def E(M, K):
    C = Config(defaultdict(lambda: 0, {}), 0, 0)
    etapes = 0
    while C != None:
        C = Opt(M, C)
        etapes += 1
        if etapes > K:
            return 0, C
    return 1, None
    
def moins_de(K):
    c = 0
    for t in range(1_000):
        c += E(T(4, t), K)[0]
    return c

print(moins_de(2))
# print(moins_de(10))
# print(moins_de(100))
print()

## Question 5

def L(T):
    n = len(T.Q)
    delta = T.delta
    mauvais = set()
    l = -1
    while len(mauvais) > l:
        l = len(mauvais)
        for x, y in delta.copy().items():
            if x[0] not in mauvais:
                if y[0] == None or y[0] in mauvais:
                    mauvais.add(x[0])
                    del delta[x]
    return set(range(n)) - mauvais

def ab(n, M):
    c_a, c_b = 0, 0
    for t in range(M):
        if t % 100 == 0:
            print(t, '/', M, '', end='\r')
        c_a += 0 in L(T(n, t))
        c_b += len(L(T(n, t))) == n//2
    print()
    return c_a, c_b


print(ab(4, 1_000))
# print(ab(8, 10_000))
# print(ab(32, 100_000))
print()

## Question 6

def fbi(n ,M, K):
    c_f, c_b, c_i = 0, 0, 0
    for t in range(M):
        termine, conf = E(T(n, t), K)
        if termine:
            c_f += 1
        elif conf != None:
            c_b += (Opt(T(n, t), conf).q in L(T(n, t)))
    c_i = M - c_f - c_b
    return (c_f, c_b, c_i)
    
print(fbi(2, 1_000, 20))
print(fbi(3, 5_000, 50))
print(fbi(4, 10_000, 200))
print()











