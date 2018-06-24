# Astuces Python à retenir

## Méméoïzation facile avec un décorateur

```Python
class memoize:
    def __init__(self, f):
        self.f = f
        self.dict = {}
    def __call__(self, *args):
        if not args in self.dict:
            self.dict[args] = self.f(*args)
        return self.dict[args]

@memoize
def fibo(n):
    if 0 <= n <= 1 :
        return 1
    return fibo(n-1) + fibo(n-2)
```

Remarque : possible avec functools.lru_cache directement

```Python
>>> memoize = functools.lru_cache(maxsize=None)
```

## Mémoïzation dans un tableau

Avantages : un poil plus rapide, survit à un F5, moins violent sur la RAM, gère le changement de u_0

```Python
u_0 = 42

if 'u_tab' not in locals() or u(0) != u_0:
    u_tab = [u_0]  # Valeurs d'initialisation de la récurrence

def u(n):
    n_max = len(u_tab) - 1  # Indice maximal présent dans la liste
    if n > n_max:
        for i in range(n_max, n):  # Remplissage jusqu'à la case n
            u_tab.append(f(u_tab[i]))
    return u_tab[n]
```

## Benchmark d'une fonction

```Python
def duree(f):
    def f_bis(*args):
        import time
        t0 = time.time()
        res = f(*args)
        print(time.time() - t0, "s")
        return res
    return f_bis

>>> duree(f)(*args)
```

## Arbres en python

Noeuds = iterables (ex: tuples ou listes)

Feuilles = non iterables (ex: flottants ou entiers)

```Python
>>> from collections import Iterable

>>> est_noeud = lambda e: isinstance(e, Iterable)

>>> def somme_feuilles(arbre):
...     if est_noeud(arbre):
...         return sum([somme_feuilles(a) for a in arbre])
...     else:
...         return arbre
```

## La puissance de eval

Premier usage : convertit depuis une base

```Python
>>> eval(bin(12))
12
```

Deuxieme usage : lance le code dans un str

```Python
>>> f = lambda x: x**2
>>> eval('f(3)')
9
```

## Conversion vers une base avec int

```Python
>>> int('1010', 2)
10
>>> int(0b1010)
10
```

## Exponentiation rapide

```Python
>>> pow(3, 4)
81
>>> pow(23, 133321, 97)  # % 97
76
```

## String représentant un objet

```Python
>>> repr({1, 2, 3})
'{1, 2, 3}'
```

## Tri selon une fonction sur les élements

```Python
>>> sorted(list, key=f [,reverse=False])
```

Possibilité d'inverser le tri

## Arbres en python

```Python
>>> from collections import defaultdict
>>> def tree(): return defaultdict(tree)
```

Un arbre est un `defaultdict` contenant des arbres ! -> les feuilles sont des `defaultdict`

# Conversion en dict simple pour un meilleur parcours:

```Python
>>> def dicts(t): return {k: dicts(t[k]) for k in t}
```

## Compter et remplaver des élements facilement

```Python
>>> 'aihfajakjv'.count("a")
3
>>> 'aihfajakjv'.replace("a", "b")
'bihfbjbkjv'
```

Marche avec chaînes, listes, tuples...

## Opérateur splat

```Python
>>> def f(x, y):
...    print(x, y)

>>> point = (3, 2)
>>> f(*point)
3 2
>>> point = {'y': 2, 'x': 3}
>>> f(**point)
3 2
```

## Existence d'une variable

```Python
>>>'var' in locals()
False
>>> var = 0
>>>'var' in locals()
True
```

## Déplier une liste

```Python
>>> sum([[1, 2, 3],[4, 5, 6]], [])
[1, 2, 3, 4, 5, 6]
```

L'argument de droite sert car `sum` aditionne avec 0 par défaut -> erreur.

Autre possibilité :

```Python
>>> functools.reduce(operator.add, [[1, 2, 3],[4, 5, 6]])
[1, 2, 3, 4, 5, 6]
```

## Itérer avec le numéro de l'élement en plus

```Python
>>> for i, x in enumerate(l, depart(=0)):
```

## Opérations sur les ensembles

```Python
>>> A = {1, 2, 3, 3}
>>> B = {3, 4, 5, 6, 7}
>>> A | B
{1, 2, 3, 4, 5, 6, 7}
>>> A & B
{3}
>>> A - B
{1, 2}
>>> B - A
{4, 5, 6, 7}
>>> A ^ B
{1, 2, 4, 5, 6, 7}
>>> (A ^ B) == ((A - B) | (B - A))
True
>>> A <= B
False
>>> (A & B) <= B
True
```

## Conditions sur tout un générateur / liste

```Python
>>> any([x > 3 for x in range(5)])
True
>>> all([x > 3 for x in range(5)])
False
```

## Itérer sur deux trucs en même temps

```Python
>>> for i, j in zip(l1, l2):
```

S'arrête tout seul quand le premier est fini
Astuce : combiner avec un génerateur pour avois seulement n élements

```Python
>>> for i, _ in zip(gen, range(n)):
```

## L'infini

```Python
>>> float('inf')
inf
>>> float('inf') == math.inf
True
```

## Chaîner les comparateurs !

```Python
>>> 0 < 1 < 2 < 5
True
```

## Mot clé else en dehors de if

```Python
>>> for x in l:
...     if machin:
...         break
... else:  # Si pas eu de break
...     print("pas de break")
```

## _ contient la dernière sortie sur le shell

```Python
>>> 3
3
>>> _
3
```

## Assigner et supprimer à des slice d'un coup

```Python
>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[:5] = [42]
>>> a
[42, 5, 6, 7, 8, 9]
>>> a[:1] = range(5)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del a[::2]
>>> a
[1, 3, 5, 7, 9]
>>> a[::2] = a[::-2]
>>> a
[9, 3, 5, 7, 1]
```

## Transposer avec zip !

```Python
>>> mat = [[1, 2, 3], [4, 5, 6]]
>>> list(zip(*mat))
[(1, 4), (2, 5), (3, 6)]
```

(le splat passe une liste d'arguments en arguments distincts)

## Diviser une liste en groupes de n avec zip

```Python
>>> l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
>>> list(zip(*[iter(l)] * 3))
[(3, 1, 4), (1, 5, 9), (2, 6, 5), (3, 5, 8)]
```

## Concaténer une liste de chaînes

```Python
>>> "".join(liste)
```

Beaucoup (beaucoup) plus rapide que sum ou reduce

## Supprimer les doublons avec set()

```Python
>>> list(set([4, 3, 5, 6, 5, 43, 4]))
[3, 4, 5, 6, 43]
```

## Intersection de listes avec set()

```Python
>>> a = [1, 2, 3, 'a']
>>> b = ['a', 'b', 'c', 3, 4, 5]
>>> list(set(a).intersection(b))
['a', 3]
```

## Distance euclidienne avec abs()

```Python
>>> x1, y1 = 3, 5
>>> x2, y2 = 7, 1
>>> abs((x1-x2) + 1j*(y1-y2))
5.656854249492381
```

## Ternaires

```Python
>>> 3 if 2 > 4 else 5
5
```

## Création rapide de dictionnaire

```Python
>>> keys = (1, 2, 3)
>>> vals = (10, 20, 30)
>>> dict (zip(keys,vals))
{1: 10, 2: 20, 3: 30}
```
