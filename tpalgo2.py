import sys
sys.setrecursionlimit(1_000_000)

u_0 = 42

class memoize:
    def __init__(self, f):
        self.f = f
        self.dict = {}
    def __call__(self, *args):
        if not args in self.dict:
            self.dict[args] = self.f(*args)
        return self.dict[args]

def duree(f):
    def f_bis(*args):
        import time
        t0 = time.time()
        res = f(*args)
        print(time.time() - t0, "s")
        return res
    return f_bis

@memoize
def u(n):
    u_i = u_0
    for i in range(n):
        u_i = (7951 * u_i) % 123457
    return u_i

@memoize
def v(n):
    v_i = u_0
    for i in range(n):
        v_i = (2971 * v_i) % 345679
    return v_i

    
def Sig(s):
    return sum((u(i) * x) % v(i) for i, x in enumerate(s, 1))
    
    
print(Sig((1, 2, 3, 4, 5)))
print(Sig((6, 7, 8, 9, 10)))
print(Sig((11, 12, 13, 14, 15)))
print()


def suivants(solution, n):
    k = len(solution)
    if k == n:
        raise "Grille complète"
    col_libres = set(range(n)).difference(set(solution))
    for i in range(len(solution)):
        d = solution[i]
        if d + (k - i) in col_libres:
            col_libres.remove(d + (k - i))
        if d - (k - i)  in col_libres:
            col_libres.remove(d - (k - i))
    tab = []
    for c in col_libres:
        tab.append(solution + [c])
    return tab




def dames_rec(n):
    solutions = []
    def etape(s, k):
        if k == 0:
            solutions.append(s)
        else:
            for suiv in suivants(s, n):
                etape(suiv, k-1)
    etape([], n)
    return solutions

import copy

def dames_it(n):
    dico = dict()
    conv = lambda i: chr(i + 97)
    def suivants_dict(solution, n):
        key = "".join(list(map(conv, solution)))
        l = len(solution)
        if l > 1 and key[:-1] in dico:
            grille = copy.deepcopy(dico[key[:-1]])
        else:
            grille = [[True for i in range(n)] for i in range (n)]
        for i in range(n):
            grille[l-1][i] = False
        d = solution[-1]
        for i in range(l, n):
            grille[i][d] = False
            if d + (i - l + 1) < n:
                grille[i][d + (i - l + 1)] = False
            if d - (i - l + 1) >= 0:
                grille[i][d - (i - l + 1)] = False
        dico[key] = grille
        return [i for i in range(n) if grille[l][i]]
    solutions = []
    options = [list(range(n))]
    chemin_courant = []  # Toujours avec un temps de retard sur les options
    while True:
        # print(chemin_courant, options, "", sep='\n')
        profondeur = len(chemin_courant)
        if options == []:  # L'arbre est vide : fin de l'algorithme
            break
        elif profondeur == n - 1:  # Noeud juste avant les feuilles
            for feuille in options[-1]:
                solutions.append(chemin_courant + [feuille])
            del options[-1]  # On supprimme le noeud exploré
            del chemin_courant[-1]  # On supprime la correspondance dans le chemin courant
        elif len(options[profondeur]) == 0:  # Noeud vide : on remonte
            del options[-1]  # On supprime le noeud
            if len(chemin_courant) > 0:
                del chemin_courant[-1]
        else:
            chemin_courant.append(options[profondeur][-1])
            options.append(suivants_dict(chemin_courant, n))
            del options[profondeur][-1]  # Supression du père avant d'explorer les fils
    return solutions
        

def compte_sig_paires(solutions):
    c = 0
    for s in solutions:
        c += 1*(Sig(s) % 2 == 0)
    return c

    
def comparaison(n):
    t0 = time.time()
    print(compte_sig_paires(dames_rec(n)))
    t1 = time.time()
    print(compte_sig_paires(dames_it(n)))
    t2 = time.time()
    print("Récursif :", round(t1 - t0, 2), "- Itératif :", round(t2 - t1, 2))
    

dico = dict()
conv = lambda i: chr(i + 97)
def suivants_dict(solution, n):
    key = "".join(list(map(conv, solution)))
    l = len(solution)
    if l > 1 and key[:-1] in dico:
        prev = dico[key[:-1]]
        grille = [[True for i in range(n)] for i in range (n)]
        for i in range(n):
            for j in range(n):
                grille[i][j] = prev[i][j]
    else:
        grille = [[True for i in range(n)] for i in range (n)]
    for i in range(n):
        grille[l-1][i] = False
    d = solution[-1]
    for i in range(l, n):
        grille[i][d] = False
        if d + (i - l + 1) < n:
            grille[i][d + (i - l + 1)] = False
        if d - (i - l + 1) >= 0:
            grille[i][d - (i - l + 1)] = False
    dico[key] = grille
    return [i for i in range(n) if grille[l][i]]
