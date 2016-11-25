# -*- coding: utf-8 -*-
def loncki(n, k = 2):
    """
    Optimalna strategija metanja lončkov za določitev najvišjega nadstropja,
    da se lonček ne razbije, če imamo n nadstropij in imamo na voljo k lončkov.

    Vrne par, ki vsebuje
    - največje število potrebnih metov z vrnjeno strategijo, in
    - strategijo, ki je podana s seznamom:
        - v seznamu so pari, ki določajo:
            - številko nadstropja, iz katerega naj vržemo lonček,
              če se v prejšnjem metu ni razbil, in
            - strategijo metanja, če se lonček ob metu razbije;
        - na zadnjem mestu seznama je številka najvišjega nadstropja,
          iz katerega lahko vržemo lonček, ne da bi se razbil
          (ob pogoju, da se ni razbil pri prejšnjih metih iz seznama).

    Časovna zahtevnost: O(kn^2)
    """
    assert n >= 0 and k > 0
    if n == 0:
        return (0, [0])
    V = dict([((0, j), (0, None)) for j in range(k)] +
             [((1, j), (1, 1)) for j in range(k)] +
             [((i, 0), (i, 1)) for i in range(2, n+1)])
    for j in range(1, k):
        for i in range(2, n+1):
            v, r = min((max(V[h-1, j-1], V[i-h, j])[0], h)
                       for h in range(1, i+1))
            V[i, j] = (v+1, r)
    def resitev(i, j, dno = 0):
        """
        Sestavi strategijo metanja,
        če smo rešitev omejili na i nadstropij nad nadstropjem dno
        in imamo na voljo še j+1 lončkov.

        Časovna zahtevnost: O(i)
        """
        if j < 0:
            return [dno]
        l = []
        r = V[i, j][1]
        while r is not None:
            l.append((dno + r, resitev(r-1, j-1, dno)))
            i -= r
            dno += r
            r = V[i, j][1]
        l.append(dno + i)
        return l
    return (V[n, k-1][0], resitev(n, k-1))

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
