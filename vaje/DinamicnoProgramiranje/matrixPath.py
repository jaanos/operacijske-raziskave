# -*- coding: utf-8 -*-
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
