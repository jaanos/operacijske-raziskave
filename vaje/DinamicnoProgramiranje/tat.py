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
