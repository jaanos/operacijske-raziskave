# -*- coding: utf-8 -*-
def razporeditev(p, op = lambda x, y: x+y, opt = max):
    """
    Razporeditev sredstev po kategorijah.
    p[i][j] označuje korist ob dodelitvi i sredstev h kategoriji j.
    Mogoče je nastaviti način računanja koristi (privzeto je seštevanje)
    ter tip optimuma (privzet je maksimum).

    Časovna zahtevnost: O(m^2 n),
    kjer je n število kategorij
    in m največje število sredstev v posamezni kategoriji.
    """
    m = len(p)
    assert m > 0
    n = len(p[0])
    assert all(len(r) == n for r in p)
    if n == 1:
        return (p[-1][0], [m])
    V = [[(p[i][0], i) for i in range(m)]]
    for j in range(1, n-1):
        c = []
        V.append(c)
        for i in range(m):
            c.append(opt((op(v, p[i-h][j]), i-h)
                     for h, (v, _) in enumerate(V[j-1][:i+1])))
    x, y = opt((op(v, p[m-h-1][-1]), m-h-1) for h, (v, _) in enumerate(V[-1]))
    z = m - 1
    l = [y]
    for j in reversed(range(n-1)):
        z -= y
        y = V[j][z][1]
        l.append(y)
    return (x, list(reversed(l)))
