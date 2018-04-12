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
