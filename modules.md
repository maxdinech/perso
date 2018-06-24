# Modules utiles

## 1. `itertools`

```Python
import itertools
```

# Itérateurs infinis

```Python
itertools.count(start [,step])
>>> count(10)  >>>  10 11 12 13 14 ...
```

```Python
itertools.cycle(p)
cycle('ABCD')  >>>  A B C D A B C D ...
```

```Python
itertools.repeat(elem [,n])
repeat(10, 3)  >>>  10 10 10
```

# Itérateurs terminant sur la séquence la plus courte

```Python
itertools.accumulate(p [,func])
>>> accumulate([1,2,3,4,5])  >>>  1 3 6 10 15
```

```Python
itertools.chain(p, q, ...)
>>> chain('ABC', 'DEF')  >>>  A B C D E F
```

```Python
itertools.chain.from_iterable(p, q, ...)
>>> chain.from_iterable(['ABC', 'DEF'])  >>>  A B C D E F
```

```Python
itertools.compress(data, selectors)
>>> compress('ABCDEF', [1,0,1,0,1,1])  >>>  A C E F
```

```Python
itertools.zip_longest(p, q, ...)
>>> zip_longest('ABCD', 'xy', fillvalue='-')  >>>  Ax By C- D-
```

# Itérateurs combinatoires

```Python
itertools.product(p, q, ... [,repeat=1])
>>> product('AB', 'CD')  >>>  AC AD BC BD
>>> product('ABC', repeat=2)  >>>  AA AB AC BA BB BC CA CB CC
```

```Python
itertools.permutations(p [,r])
>>> permutations('ABCD', 2)  >>>  AB AC AD BA BC BD CA CB CD DA DB DC
```

```Python
itertools.combinations(p, r)
>>> combinations('ABCD', 2)  >>>  AB AC AD BC BD CD
```

```Python
itertools.combinations_with_replacement(p, r)
>>> combinations_with_replacement('ABCD', 2)  >>>  AA AB AC AD BB BC BD CC CD DD
```


## 2. `functools`

```Python
import functools
```

### Décorateur pour memoïzer facilement

```Python
@functools.lru_cache(maxsize=128)
```

### `it_list` en Python

```Python
functools.reduce(function, iterable [,initializer])
>>> reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])  >>>  ((((1+2)+3)+4)+5)  >>>  15
```

## 3. `collections`

```Python
import collections
```

### Tuples avec des noms

```Python
collections.namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
>>> Point = namedtuple('Point', 'x y z')
>>> P = Point(3, 5, 1)
>>> P.x  >>>  3
```

Bonus : ces tuples sont mutables !

```Python
>>> P._replace(x=5)
>>> P.x  >>>  5
```

### Dictionnaires spéciaux pour compter des trucs

Utile car dispose de fonctions plus poussées que str.count('c') :

```Python
collections.Counter(iterable)
>>> Counter('abracadabra').most_common(3)  >>>  [('a', 5), ('r', 2), ('b', 2)]
```

## 4. `fractions`

```Python
import fractions
```

### Rationnels en précision complète

```Python
>>> from fractions import Fraction
>>> f = Fraction(2, 5)
>>> f /2
Fraction(1, 5)
```