# -*- coding: utf-8 -*-
"""
Funkcije na grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
Podane časovne zahtevnosti veljajo za predstavitev grafa s seznami sosedov.
"""
from kopica import Kopica

def dijkstra(G, u):
    """
    Poišče najkrajše razdalje od vozlišča u do ostalih vozlišč.

    Časovna zahtevnost: O(m log n)
    """
    inf = float('inf')
    K = Kopica({v: 0 if v == u else inf for v in G.vozlisca()})
    razdalje = {}
    p = {u: None}
    while len(K) > 0:
        v, d = K.poberi()
        razdalje[v] = d
        for w, t in G.utezeniSosedi(v).items():
            if w in razdalje:
                continue
            r = d + t
            if r < K[w]:
                K[w] = r
                p[w] = v
    return razdalje, p

def obstajaPot(G, s, t, L):
    """
    Poišče pot od s do t v neusmerjenem grafu,
    v kateri je dolžina najdaljše povezave največ L.

    Časovna zahtevnost: O(m)
    """
    H = G.__class__()
    for u in G.vozlisca():
        H.dodajVozlisce(u)
    for u in G.vozlisca():
        for v, l in G.utezeniSosedi(u).items():
            if l <= L:
                H.dodajPovezavo(u, v)
    _, g, p = H.BFS(koreni = [t])
    if g[s] is None:
        return False
    pot = []
    while s is not None:
        pot.append(s)
        s = p[s]
    return pot

def minNajdaljsaPovezava(G, s, t):
    """
    Poišče pot od s do t, ki minimizira dolžino najdaljše povezave.

    Časovna zahtevnost: O(m log n)
    """
    inf = float('inf')
    K = Kopica({v: 0 if v == t else inf for v in G.vozlisca()})
    dolzine = {}
    p = {t: None}
    while len(K) > 0:
        v, d = K.poberi()
        dolzine[v] = d
        if v == s:
            break
        for w, r in G.utezeniSosedi(v).items():
            if w in dolzine:
                continue
            if r < d:
                r = d
            if r < K[w]:
                K[w] = r
                p[w] = v
    pot = []
    u = s
    while u is not None:
        pot.append(u)
        u = p[u]
    return (dolzine[s], pot)

def dvojniDijkstra(G, s, t):
    """
    Iskanje najkrajše poti od s do t v neusmerjenem grafu G
    z uporabo Dijkstrovega algoritma z začetkoma v s in t.

    Algoritem uporablja eno samo kopico,
    kjer vsak vnos ustreza paru (vozlišče, začetno vozlišče).
    Iskanje se konča, ko se neko vozlišče drugič odstrani iz kopice.
    Najkrajša pot potem poteka bodisi skozi najdeno vozlišče,
    bodisi skozi katero drugo vozlišče izmed vozlišč,
    doseženih od enega od s in t, ki so sosedna kateremu od vozlišč,
    doseženih iz drugega začetnega vozlišča.
    Za vozlišče na najkrajši poti sta tako razdalji do s in t že določeni.

    Časovna zahtevnost: O(m log n)
    """
    inf = float('inf')
    K = Kopica(dict([((v, 0), (0 if v == s else inf)) for v in G.vozlisca()] +
                    [((v, 1), (0 if v == t else inf)) for v in G.vozlisca()]))
    r = [{}, {}]
    p = [{s: None}, {t: None}]
    while len(K) > 0:
        (v, i), d = K.poberi()
        if v in r[1-i]:
            d += r[1-i][v]
            break
        r[i][v] = d
        for w, l in G.utezeniSosedi(v).items():
            if w in r[i]:
                continue
            l += d
            if l < K[w, i]:
                K[w, i] = l
                p[i][w] = v
    if len(r[i]) > 0:
        d, v = min((d, v), min((l + K[w, 1-i], w) for w, l in r[i].items()))
    u = v
    qs, qt = [], []
    while u is not None:
        qs.append(u)
        u = p[0][u]
    while v != t:
        v = p[1][v]
        qt.append(v)
    return (d, list(reversed(qs)) + qt)

def bellmanFord(G, u):
    """
    Poišče najkrajše razdalje od vozlišča u do ostalih vozlišč.

    Časovna zahtevnost: O(mn)
    """
    inf = float('inf')
    razdalje = {v: 0 if v == u else inf for v in G.vozlisca()}
    p = {u: None}
    naslednji = {u}
    for i in range(len(G)):
        if len(naslednji) == 0:
            break
        trenutni, naslednji = naslednji, set()
        for v in trenutni:
            d = razdalje[v]
            for w, r in G.utezeniSosedi(v).items():
                r += d
                if r < razdalje[w]:
                    razdalje[w] = r
                    p[w] = v
                    naslednji.add(w)
    else:
        if len(naslednji) > 0:
            raise ValueError("graf ima negativen cikel")
    return (razdalje, p)

def floydWarshall(G):
    """
    Poišče najkrajše razdalje za vsak par vozlišč.

    Časovna zahtevnost: O(n^3)
    """
    inf = float('inf')
    razdalje = {(u, v): 0 if u == v else inf for u in G.vozlisca() for v in G.vozlisca()}
    p = {(u, u): None for u in G.vozlisca()}
    for u in G.vozlisca():
        for v, r in G.utezeniSosedi(u).items():
            razdalje[u, v] = r
            p[u, v] = u
    for w in G.vozlisca():
        for u in G.vozlisca():
            if razdalje[u, w] + razdalje[w, u] < 0:
                raise ValueError("graf ima negativen cikel")
            for v in G.vozlisca():
                r = razdalje[u, w] + razdalje[w, v]
                if r < razdalje[u, v]:
                    razdalje[u, v] = r
                    p[u, v] = p[w, v]
    return (razdalje, p)
