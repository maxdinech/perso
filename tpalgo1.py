u0 = 42

m = 1_073_741_783

def u(n):
    u_i = u0
    for i in range(n):
        u_i = (42 * u_i + 17) % m
    return u_i


def calc_u_tab(n):
    tab = [u0]
    for i in range(n):
        tab.append((42 * tab[-1] + 17) % m)
    return tab

# u_tab = calc_u_tab(10_000_000)

# for k in [5, 10000, 2000000]:
    # print(u_tab[k] % 1000)
# print()


G = [0, 1, 4, 5]
K = [1, 4, 6]
R = [0, 1, 2, 3, 4, 5, 6, 7]
T = [0, 2, 4, 6]

def U(k):
    return list(set([R[u_tab[i] % 8] for i in range(k, k+7)]))
    
def compte(P, l):
    c = 0
    card = len(P)
    P_u_l = P[u_tab[l] % card]
    for h in range(l):
        c += 1*(P[u_tab[h] % card] == P_u_l)
    return c

# print(compte(K, 10) % 1000)
# print(compte(G, 2_000_000) % 1000)
# print()


# for k in [0, 10, 20]:
#     print(U(k), U(k)[17 % len(U(k))])


def V(i, j):
    if i < 0 or j < 0:
        raise "i et j doivent être positifs"
    if i == 0 and j == 0:
        return [0, 1, 2]
    elif i == 0:
        return [0, 1, 2, 6, 7]
    elif j == 0:
        return [0, 1, 2, 3, 4]
    else:
        return R

def x(n):
    if n in [7, 0, 1]:
        return 1
    elif n in [3, 4, 5]:
        return -1
    else:
        return 0

def y(n):
    if n in [1, 2, 3]:
        return 1
    elif n in [5, 6, 7]:
        return -1
    else:
        return 0

def B(P, s, n):
    b_x = [0]
    b_y = [0]
    for k in range(n):
        ens = list(set(P).intersection(set(V(b_x[-1], b_y[-1]))))
        l = len(ens)
        b_x.append(b_x[-1] + x(ens[u_tab[s+k] % l]))
        b_y.append(b_y[-1] + y(ens[u_tab[s+k] % l]))
    return [(i, j) for (i, j) in zip(b_x, b_y)]


def d(A):
    return max([i + j for (i, j) in A])


def moy_dB(P, n):
    somme = 0
    for s in range(100):
        somme += d(B(P, s*n, n))
    print()
    return somme / 100.

# print(B(R, 0, 10)[-1])
# print(B(G, 0, 10)[-1])
# print(B(R, 0, 1_000_000)[-1])
# print(B(G, 0, 1_000_000)[-1])

# print(moy_dB(K, 10))
# print(moy_dB(G, 12))
# print(moy_dB(T, 14))
# print(moy_dB(K, 100_000))
# print(moy_dB(G, 100_000))
# print(moy_dB(T, 100_000))

def pas(p):
    return (x(p), y(p))

def marches(P, n):
    tab = []
    def etape(marche, paas, k):
        pos = (marche[-1][0] + paas[0], marche[-1][1] + paas[1])
        if pos[0] >= 0 and pos [1] >= 0:
            marche = marche + [pos]
            if k == 0:
                tab.append(marche)
            else:
                for p in P:
                    etape(marche, pas(p), k-1)
    for p in P:
        etape([(0, 0)], pas(p), n-1)
    return tab


def depile3(mat):
    return [c for a in mat for b in a for c in b]


def depile2(mat):
    return [b for a in mat for b in a]


def marches_dyn(P, n):
    prev = [[[] for i in range(n+1)] for j in range (n+1)]
    prev[0][0] = [[(0, 0)]]  # Liste de chemins (liste de liste de tuples)
    for i in range(1, n+1):  # Boucle sur la profondeur
        curr = [[[] for i in range(n+1)] for j in range (n+1)]
        for a in range(n+1):
            for b in range(n+1):
                print(i, a, b)
                for p in P:
                    X = a+x(p)
                    Y = b+y(p)
                    if X >= 0 and X <= n and Y >= 0 and Y <= n:
                        for c in prev[a][b]:  # Pour chaque chemin
                            curr[X][Y].append(c + [(X, Y)])
        prev = list(curr)
    return curr

def somme(l1, l2):
    return [i + j for (i, j) in zip(l1, l2)]


def w_dyn(P, i, j, n):
    prev = [[0 for j in range(n+1)] for k in range (n+1)]
    prev[0][0] = 1
    for i in range(1, n+1):  # Boucle sur la profondeur
        curr = [[0 for j in range(n+1)] for k in range (n+1)]
        for a in range(n+1):
            for b in range(n+1):
                for p in P:
                    X = a+x(p)
                    Y = b+y(p)
                    if X >= 0 and X <= n and Y >= 0 and Y <= n:
                        curr[X][Y] += prev[a][b]
        prev = list(curr)
    return curr[i][j]


def W_dyn(P, n):
    prev = [[0 for j in range(n+1)] for k in range (n+1)]
    prev[0][0] = 1
    for i in range(1, n+1):  # Boucle sur la profondeur
        curr = [[0 for j in range(n+1)] for k in range (n+1)]
        for a in range(n+1):
            for b in range(n+1):
                for p in P:
                    X = a+x(p)
                    Y = b+y(p)
                    if X >= 0 and X <= n and Y >= 0 and Y <= n:
                        curr[X][Y] += prev[a][b]
        prev = list(curr)
    s = 0
    for i in range(n+1):
        for j in range(n+1):
            s += curr[i][j]
    return s



def marches_dyn_moy_d(P, n):
    prev = [[[0 for i in range(2*n+1)] for j in range(n+1)] for k in range (n+1)]
    prev[0][0][0] = 1
    for i in range(1, n+1):  # Boucle sur la profondeur
        curr = [[[0 for i in range(2*n+1)] for j in range(n+1)] for k in range (n+1)]
        for a in range(n+1):
            for b in range(n+1):
                # print(i, a, b)
                for p in P:
                    X = a+x(p)
                    Y = b+y(p)
                    if X >= 0 and X <= n and Y >= 0 and Y <= n:
                        curr[X][Y] = somme(prev[a][b], curr[X][Y])
                        if X + Y == a + b + 1:
                            curr[X][Y][X + Y] += curr[X][Y][X + Y - 1]
                            curr[X][Y][X + Y - 1] = 0
                        if X + Y == a + b + 2:
                            curr[X][Y][X + Y] += curr[X][Y][X + Y - 2]
                            curr[X][Y][X + Y] += curr[X][Y][X + Y - 1]
                            curr[X][Y][X + Y - 2] = 0
                            curr[X][Y][X + Y - 1] = 0
        prev = list(curr)
    l = depile2(curr)
    s = 0
    for case in l:
        s += sum([i*case[i] for i in range(2*n + 1)])
    return s / sum(depile3(curr))


def marches_dyn_somme_u_d(P, n):
    prev = [[[0 for i in range(2*n+1)] for j in range(n+1)] for k in range (n+1)]
    prev[0][0][0] = 1
    for i in range(1, n+1):  # Boucle sur la profondeur
        curr = [[[0 for i in range(2*n+1)] for j in range(n+1)] for k in range (n+1)]
        for a in range(n+1):
            for b in range(n+1):
                # print(i, a, b)
                for p in P:
                    X = a+x(p)
                    Y = b+y(p)
                    if X >= 0 and X <= n and Y >= 0 and Y <= n:
                        curr[X][Y] = somme(prev[a][b], curr[X][Y])
                        if X + Y == a + b + 1:
                            curr[X][Y][X + Y] += curr[X][Y][X + Y - 1]
                            curr[X][Y][X + Y - 1] = 0
                        if X + Y == a + b + 2:
                            curr[X][Y][X + Y] += curr[X][Y][X + Y - 2]
                            curr[X][Y][X + Y] += curr[X][Y][X + Y - 1]
                            curr[X][Y][X + Y - 2] = 0
                            curr[X][Y][X + Y - 1] = 0
        prev = list(curr)
    l = depile2(curr)
    s = 0
    for case in l:
        s += sum([u_tab[i]*case[i] for i in range(2*n + 1)])
    return s

def u_d_A_marches(mat):
    s = 0
    n = len(mat) - 1
    for a in range(n+1):
        for b in range(n+1):
            for A in mat[a][b]:
                s += u_tab[d(A)]
    return s
    
            
# for P, n in [(R, 3), (K, 10)]:  #, (G, 12), (T, 14)]:
#     tab = marches(P, n)
#     l = len(tab)
#     print(P, n)
#     print(l)
#     print(sum([d(A) for A in tab]) / l)
#     print(sum([u_tab[d(A)] % 1000 for A in tab]) % 1000)
#     print()

























