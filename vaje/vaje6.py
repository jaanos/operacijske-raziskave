# -*- coding: utf-8 -*-
def submatrixSum(M):
    """
    Strnjena podmatrika z največjo vsoto komponent.

    Časovna zahtevnost: O(m^2 n),
    kjer je m × n dimenzija vhodne matrike.
    """
    m = len(M)
    assert m > 0
    n = len(M[0])
    assert n > 0 and all(len(l) == n for l in M)
    s = {(-1, h): 0 for h in range(n)}
    V = {}
    for j in range(m):
        for h in range(n):
            s[j, h] = s[j-1, h] + M[j][h]
        for i in range(j+1):
            V[i, j, 0] = (s[j, 0] - s[i-1, 0], 0)
            for h in range(1, n):
                v, k = V[i, j, h-1]
                x = s[j, h] - s[i-1, h]
                if v < 0:
                    v = x
                    k = h
                else:
                    v += x
                V[i, j, h] = (v, k)
    (v, k), (i, j, h) = max((y, x) for x, y in V.items())
    return (v, (i, k), [r[k:h+1] for r in M[i:j+1]])

def kovanci(c, v):
    """
    Izplačilo vsote c z najmanjšim številom kovancev iz nabora v.

    Časovna zahtevnost: O(cn),
    kjer je n velikost seznama v.
    """
    assert 1 in v
    V = [(0, [0]*len(v))]
    for i in range(1, c+1):
        d = []
        for j, x in enumerate(v):
            if x > i:
                continue
            n, s = V[i-x]
            s = s[:]
            s[j] += 1
            d.append((n, s))
        n, s = min(d)
        V.append((n+1, s))
    return V[-1]

def tat(c):
    """
    Maksimalni izplen iz vrstnih hiš s premoženjem iz seznama c,
    če ne smemo oropati dveh sosednjih hiš.

    Časovna zahtevnost: O(n),
    kjer je n dolžina seznama c
    """
    assert all(x >= 0 for x in c)
    if len(c) == 0:
        return [0, []]
    elif len(c) == 1:
        return [c[0], [0]]
    V = [(c[0], [0])]
    if c[1] > c[0]:
        v, s = c[1], [1]
    else:
        v, s = V[0]
    V.append((v, s))
    for i in range(2, len(c)):
        if s[-1] == i-1:
            vv, ss = V[-2]
            vv += c[i]
            if vv > v:
                v = vv
                s = ss + [i]
        else:
            v += c[i]
            s = s + [i]
        V.append((v, s))
    return V[-1]

def hlod(x, l):
    """
    Optimalno rezanje hloda dolžine l na mestih iz urejenega seznama x,
    če je cena posameznega rezanja enaka dolžini hloda, ki ga režemo.

    Časovna zahtevnost: O(n^3),
    kjer je n dolžina seznama x.
    """
    n = len(x)
    if n == 0:
        return (0, [])
    assert all(x[i-1] < x[i] for i in range(1, n))
    assert 0 < x[0] and x[-1] < l
    x = [0] + x + [l]
    V = dict([((i, i+1), (0, None)) for i in range(n+1)] +
             [((i, i+2), (x[i+2] - x[i], i+1)) for i in range(n)])
    for h in range(3, n+2):
        for i in range(n-h+2):
            v, k = min((V[i, i+j][0] + V[i+j, i+h][0], j) for j in range(1, h))
            V[i, i+h] = (v + x[i+h] - x[i], i+k)
    q = [(0, n+1)]
    l = []
    for h in range(2*n+1):
        i, j = q[h]
        k = V[i, j][1]
        if k is not None:
            l.append(x[k])
            q.append((i, k))
            q.append((k, j))
    return (V[0, n+1][0], l)
