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
