# -*- coding: utf-8 -*-
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
