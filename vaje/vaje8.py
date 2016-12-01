# -*- coding: utf-8 -*-
"""
Funkcije na grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
"""

def nothing(u, v = None):
    """
    Visit funkcija, ki ne naredi nič.

    Časovna zahtevnost: O(1)
    """
    return True

class Graf:
    """
    Abstraktni razred za grafe.
    """

    def __init__(self):
        """
        Inicializacija - ni implementirana.
        """
        raise NotImplementedError("Ni mogoče narediti objekta abstraktnega razreda!")

    def __len__(self):
        """
        Število vozlišč v grafu.

        Časovna zahtevnost: O(1)
        """
        return self.n

    def premer(self):
        """
        Premer grafa.

        Časovna zahtevnost: O(n) iskanj v širino.
        """
        inf = float('inf')
        return max(max(inf if x is None else x
                       for x in self.BFS(koreni = [u])[1].values())
                   for u in self.vozlisca())

class Digraf(Graf):
    """
    Abstraktni razred za digrafe.
    """

    def izhodniSosedi(self, u):
        """
        Seznam izhodnih sosedov obstoječega vozlišča.
        """
        return self.sosedi(u)

    def utezeniIzhodniSosedi(self, u):
        """
        Slovar uteži povezav iz obstoječega vozlišča.
        """
        return self.utezeniSosedi(u)

class MatricniGraf(Graf):
    """
    Graf, predstavljen z matriko sosednosti.

    Prostorska zahtevnost: O(n^2)
    """

    def __init__(self):
        """
        Inicializacija prazenga grafa.

        Časovna zahtevnost: O(1)
        """
        self.voz = []
        self.indeksi = {}
        self.A = []
        self.n = 0

    def __repr__(self):
        """
        Znakovna predstavitev grafa.

        Časovna zahtevnost: O(n^2)
        """
        if self.n == 0:
            return "Prazen graf"
        return '\n'.join('%s\t[%s]' %
            (self.voz[i], ' '.join('*' if x is None else str(x)
                                   for x in r)) for i, r in enumerate(self.A))

    def dodajVozlisce(self, u):
        """
        Dodajanje novega vozlišča (če še ne obstaja).

        Časovna zahtevnost: O(n)
        """
        if u in self.indeksi:
            raise ValueError("Vozlišče že obstaja!")
        self.voz.append(u)
        self.indeksi[u] = self.n
        self.n += 1
        for r in self.A:
            r.append(None)
        self.A.append([None] * self.n)

    def dodajPovezavo(self, u, v, utez = 1):
        """
        Dodajanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        assert utez is not None, "Utež mora biti določena!"
        i = self.indeksi[u]
        j = self.indeksi[v]
        self.A[i][j] = utez
        self.A[j][i] = utez

    def tezaPovezave(self, u, v):
        """
        Teža povezave med podanima vozliščema.
        """
        return self.A[self.indeksi[u]][self.indeksi[v]]

    def brisiPovezavo(self, u, v):
        """
        Brisanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        i = self.indeksi[u]
        j = self.indeksi[v]
        self.A[i][j] = None
        self.A[j][i] = None

    def brisiVozlisce(self, u):
        """
        Brisanje obstoječega vozlišča.

        Časovna zahtevnost: O(n)
        """
        i = self.indeksi[u]
        del self.indeksi[u]
        del self.voz[i]
        del self.A[i]
        for r in self.A:
            del r[i]
        for v, j in self.indeksi.items():
            if j > i:
                self.indeksi[v] -= 1
        self.n -= 1

    def sosedi(self, u):
        """
        Seznam sosedov obstoječega vozlišča.

        Časovna zahtevnost: O(n)
        """
        return [self.voz[j] for j, x in enumerate(self.A[self.indeksi[u]])
                if x is not None]

    def utezeniSosedi(self, u):
        """
        Slovar uteži povezav na obstoječem vozlišču.

        Časovna zahtevnost: O(n)
        """
        return {self.voz[j]: x for j, x in enumerate(self.A[self.indeksi[u]])
                if x is not None}

    def vozlisca(self):
        """
        Vrne seznam vozlišč grafa.

        Časovna zahtevnost: O(n)
        """
        return self.voz[:]

    def trikotnik(self):
        """
        Določi, ali ima graf trikotnik.

        Časovna zahtevnost: O(mn)
        """
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.A[i][j] is not None:
                    for h in range(j+1, self.n):
                        if self.A[j][h] is not None and \
                                self.A[h][i] is not None:
                            return [self.voz[k] for k in (i, j, h)]
        return None

    def BFS(self, koreni = None, visit = nothing):
        """
        Iskanje v globino.

        Časovna zahtevnost: O(n^2) + O(n) klicev funkcije visit
        """
        if koreni is None:
            koreni = range(self.n)
        else:
            koreni = [self.indeksi[u] for u in koreni]
        globina = [None] * self.n
        stars = [None] * self.n
        uspeh = True
        for h in koreni:
            if globina[h] is not None:
                continue
            nivo = [h]
            globina[h] = 0
            stars[h] = None
            d = 1
            while len(nivo) > 0:
                naslednji = []
                for i in nivo:
                    s = None if stars[i] is None else self.voz[stars[i]]
                    if not visit(self.voz[i], s):
                        uspeh = False
                        break
                    for j, x in enumerate(self.A[i]):
                        if x is None:
                            continue
                        if globina[j] is None:
                            globina[j] = d
                            stars[j] = i
                            naslednji.append(j)
                nivo = naslednji
                d += 1
        return (uspeh, {u: globina[i] for u, i in self.indeksi.items()},
                {u: None if stars[i] is None else self.voz[stars[i]]
                 for u, i in self.indeksi.items()})

class MatricniDigraf(MatricniGraf, Digraf):
    """
    Graf, predstavljen z matriko sosednosti.

    Prostorska zahtevnost: O(n^2)
    """

    def dodajPovezavo(self, u, v, utez = 1):
        """
        Dodajanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        assert utez is not None, "Utež mora biti določena!"
        self.A[self.indeksi[u]][self.indeksi[v]] = utez

    def brisiPovezavo(self, u, v):
        """
        Brisanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        self.A[self.indeksi[u]][self.indeksi[v]] = None

    def vhodniSosedi(self, u):
        """
        Seznam vhodnih sosedov obstoječega vozlišča.

        Časovna zahtevnost: O(n)
        """
        i = self.indeksi[u]
        return [self.voz[j] for j, r in enumerate(A)
                if r[i] is not None]

    def utezeniVhodniSosedi(self, u):
        """
        Slovar uteži povezav v obstoječe vozlišče.

        Časovna zahtevnost: O(n)
        """
        i = self.indeksi[u]
        return {self.voz[j]: r[i] for j, r in enumerate(A)
                if r[i] is not None}

    def zvezda(self):
        """
        Poišče zvezdno vozlišče, če obstaja.

        Časovna zahtevnost: O(n^2)
        """
        z = None
        for i, r in enumerate(self.A):
            if all((x is None) == (i == j) for j, x in enumerate(r)):
                z = self.voz[i]
            elif not all(x is None for x in r):
                return None
        return z

class MnozicniGraf(Graf):
    """
    Graf, predstavljen z množicami sosedov.

    Prostorska zahtevnost: O(m)
    """

    def __init__(self):
        """
        Inicializacija prazenga grafa.

        Časovna zahtevnost: O(1)
        """
        self.sos = {}
        self.n = 0

    def __repr__(self):
        """
        Znakovna predstavitev grafa.

        Časovna zahtevnost: O(m)
        """
        return str(self.sos)

    def dodajVozlisce(self, u):
        """
        Dodajanje novega vozlišča (če še ne obstaja).

        Časovna zahtevnost: O(1)
        """
        if u in self.sos:
            return
        self.n += 1
        self.sos[u] = {}

    def dodajPovezavo(self, u, v, utez = 1):
        """
        Dodajanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        assert utez is not None, "Utež mora biti določena!"
        self.sos[u][v] = utez
        self.sos[v][u] = utez

    def brisiPovezavo(self, u, v):
        """
        Brisanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        del self.sos[u][v]
        del self.sos[v][u]

    def brisiVozlisce(self, u):
        """
        Brisanje obstoječega vozlišča.

        Časovna zahtevnost: O(d(u))
        """
        for v in self.sos[u]:
            del self.sos[v][u]
        del self.sos[u]
        self.n -= 1

    def sosedi(self, u):
        """
        Seznam sosedov obstoječega vozlišča.

        Časovna zahtevnost: O(d(u))
        """
        return self.sos[u].keys()

    def utezeniSosedi(self, u):
        """
        Slovar uteži povezav na obstoječem vozlišču.

        Časovna zahtevnost: O(d(u))
        """
        return dict(self.sos[u])

    def vozlisca(self):
        """
        Vrne seznam vozlišč grafa.

        Časovna zahtevnost: O(n)
        """
        return self.sos.keys()

    def trikotnik(self):
        """
        Določi, ali ima graf trikotnik.

        Časovna zahtevnost: O(mD),
        kjer je D največja stopnja vozlišča v grafu.
        """
        for u, a in self.sos.items():
            for v in a:
                for w in self.sos[v]:
                    if u in self.sos[w]:
                        return [u, v, w]
        return None

    def BFS(self, koreni = None, visit = nothing):
        """
        Iskanje v globino.

        Časovna zahtevnost: O(m) + O(n) klicev funkcije visit
        """
        if koreni is None:
            koreni = self.vozlisca()
        globina = {}
        stars = {}
        uspeh = True
        for w in koreni:
            if w in globina:
                continue
            nivo = [w]
            globina[w] = 0
            stars[w] = None
            i = 1
            while len(nivo) > 0:
                naslednji = []
                for u in nivo:
                    if not visit(u, stars[u]):
                        uspeh = False
                        break
                    for v in self.sos[u]:
                        if v not in globina:
                            globina[v] = i
                            stars[v] = u
                            naslednji.append(v)
                nivo = naslednji
                i += 1
        for u in self.sos:
            if u not in globina:
                globina[u] = None
                stars[u] = None
        return (uspeh, globina, stars)

class MnozicniDigraf(MnozicniGraf):
    """
    Digraf, predstavljen z množicami sosedov.

    Prostorska zahtevnost: O(m)
    """

    def dodajPovezavo(self, u, v, utez = 1):
        """
        Dodajanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        assert utez is not None, "Utež mora biti določena!"
        self.sos[u][v] = utez

    def brisiPovezavo(self, u, v):
        """
        Brisanje povezave med obstoječima vozliščema.

        Časovna zahtevnost: O(1)
        """
        del self.sos[u][v]

    def brisiVozlisce(self, u):
        """
        Brisanje obstoječega vozlišča.

        Časovna zahtevnost: O(n)
        """
        del self.sos[u]
        for v, a in self.sos.items():
            if u in a:
                del a[u]
        self.n -= 1

    def vhodniSosedi(self, u):
        """
        Seznam vhodnih sosedov obstoječega vozlišča.

        Časovna zahtevnost: O(n)
        """
        return [v for v, a in self.sos.items() if u in a]

    def utezeniVhodniSosedi(self, u):
        """
        Slovar uteži povezav v obstoječe vozlišče.

        Časovna zahtevnost: O(n)
        """
        return {v: a[u] for v, a in self.sos.items() if u in a}

    def zvezda(self):
        """
        Poišče zvezdno vozlišče, če obstaja.

        Časovna zahtevnost: O(n)
        """
        z = None
        for u, a in self.sos.items():
            if len(a) == self.n - 1 and u not in a:
                z = u
            elif len(a) != 0:
                return None
        return z
