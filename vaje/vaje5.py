# -*- coding: utf-8 -*-
def plakati(x, v, d):
    """
    Optimalna postavitev plakatov na mestih iz urejenega seznama x
    z donosnostmi iz seznama v, če morata biti dva plakata na razdalji vsaj d.

    Časovna zahtevnost: O(n),
    kjer je n dolžina seznamov x in v.
    """
    n = len(x)
    assert n == len(v)
    assert all(x[i-1] < x[i] for i in range(1, n))
    j = 0
    s = []
    for i, xi in enumerate(x):
        while xi - x[j] >= d:
            j += 1
        if j == 0:
            p = 0
            r = None
        else:
            p = s[j-1][0]
            r = j - 1
        p += v[i]
        if i > 0 and p < s[i-1][0]:
            p = s[i-1][0]
            r = i - 1
            b = False
        else:
            b = True
        s.append((p, r, b))
    p, r, b = s[-1]
    l = []
    if b:
        l.append(n - 1)
    while r is not None:
        c = r
        _, r, b = s[r]
        if b:
            l.append(c)
    return (p, list(reversed(l)))

def matrixPath(M):
    """
    Pot od M[0][0] do M[m-1][n-1] z maksimalno vsoto
    in možnimi koraki M[i][j] -> M[i+1][j], M[i][j+1],
    kjer je M matrika dimenzij m × n.

    Časovna zahtevnost: O(mn)
    """
    m = len(M)
    n = len(M[0])
    assert all(len(r) == n for r in M)
    D = {}
    P = {}
    for i, r in enumerate(M):
        for j, x in enumerate(r):
            c = []
            if i > 0:
                c.append((D[i-1, j], (i-1, j)))
            if j > 0:
                c.append((D[i, j-1], (i, j-1)))
            if len(c) == 0:
                q, r = 0, None
            else:
                q, r = min(c)
            D[i, j] = q + M[i][j]
            P[i, j] = r
    l = []
    i, j = m-1, n-1
    while P[i, j] is not None:
        l.append((i, j))
        i, j = P[i, j]
    l.append((0, 0))
    return (D[m-1, n-1], list(reversed(l)))

def palindrom(s):
    """
    Najdaljši palindromski strnjen podniz.

    Časovna zahtevnost: O(n^2),
    kjer je n dolžina vhodnega niza

    Za algoritem, ki teče v času O(n), glej
    https://en.wikipedia.org/wiki/Longest_palindromic_substring
    """
    n = len(s)
    V = {(i, i+1): True for i in range(n)}
    for i in range(1, n):
        V[i-1, i+1] = s[i-1] == s[i]
    for j in range(2, n):
        for i in range(n-j):
            V[i, i+j+1] = V[i+1, i+j] and s[i] == s[i+j]
    l, i = max((j-i, i) for (i, j), b in V.items() if b)
    return (i, s[i:i+l])
