# -*- coding: utf-8 -*-
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
    V = [(c[0], True)]
    if c[1] > c[0]:
        v, s = c[1], True
    else:
        v, s = c[0], False
    V.append((v, s))
    for i in range(2, len(c)):
        if s:
            vv = V[-2][0] + c[i]
            s = vv > v
            if s:
                v = vv
        else:
            v += c[i]
            s = True
        V.append((v, s))
    l = []
    i = len(V) - 1
    while i >= 0:
        if V[i][1]:
            l.append(i)
            i -= 2
        else:
            i -= 1
    return V[-1][0], list(reversed(l))
