# -*- coding: utf-8 -*-
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
