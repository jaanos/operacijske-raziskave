# -*- coding: utf-8 -*-
"""
Funkcije na grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
Podane časovne zahtevnosti veljajo za predstavitev grafa s seznami sosedov.
"""

def topoloskaUreditev(G):
    """
    Topološko urejanje usmerjenega acikličnega grafa z odstranjevanjem izvorov.

    Časovna zahtevnost: O(m)
    """
    stopnje = {u: 0 for u in G.vozlisca()}
    for u in stopnje:
        for v in G.izhodniSosedi(u):
            stopnje[v] += 1
    s = []
    for u, d in stopnje.items():
        if d == 0:
            s.append(u)
    topord = []
    while len(s) > 0:
        v = s.pop()
        topord.append(v)
        for u in G.izhodniSosedi(v):
            stopnje[u] -= 1
            if stopnje[u] == 0:
                s.append(u)
    if len(topord) < len(stopnje):
        raise ValueError("Graf ima cikle!")
    return topord

def najkrajsaPotDAG(G, s, t):
    """
    Poišče najkrajšo pot od s do t v usmerjenem acikličnem grafu G.

    Časovna zahtevnost: O(m)
    """
    topord = topoloskaUreditev(G)
    d = {u: None for u in G.vozlisca()}
    p = {u: None for u in G.vozlisca()}
    d[s] = 0
    for i in range(topord.index(s), topord.index(t)):
        u = topord[i]
        l = d[u]
        for v, r in G.utezeniIzhodniSosedi(u).items():
            if d[v] is None or d[v] > l+r:
                d[v] = l+r
                p[v] = u
    pot = []
    u = t
    while u is not None:
        pot.append(u)
        u = p[u]
    return (d[t], list(reversed(pot)))

def najdaljsaPotDAG(G, s, t):
    """
    Poišče najdaljšo pot od s do t v usmerjenem acikličnem grafu G.

    Časovna zahtevnost: O(m)
    """
    topord = topoloskaUreditev(G)
    d = {u: None for u in G.vozlisca()}
    p = {u: None for u in G.vozlisca()}
    d[s] = 0
    for i in range(topord.index(s), topord.index(t)):
        u = topord[i]
        l = d[u]
        for v, r in G.utezeniIzhodniSosedi(u).items():
            if d[v] is None or d[v] < l+r:
                d[v] = l+r
                p[v] = u
    pot = []
    u = t
    while u is not None:
        pot.append(u)
        u = p[u]
    return (d[t], list(reversed(pot)))

def steviloPoti(G, s, t):
    """
    Za usmerjen acikličen graf G z utežmi,
    ki predstavljajo število načinov, kako lahko sledimo povezavi,
    določi število načinov, kako lahko pridemo od vozlišča s do vozlišča t.

    Časovna zahtevnost: O(m)
    """
    st = {u: 1 if u == s else 0 for u in G.vozlisca()}
    for u in topoloskaUreditev(G):
        for v, d in G.utezeniIzhodniSosedi(u).items():
            st[v] += st[u] * d
    return st[t]

def vecTopoUreditev(G):
    """
    Ugotovi, ali ima usmerjen acikličen graf več kot eno topološko ureditev.

    Časovna zahtevnost: O(m)
    """
    stopnje = {u: 0 for u in G.vozlisca()}
    for u in stopnje:
        for v in G.izhodniSosedi(u):
            stopnje[v] += 1
    s = []
    for u, d in stopnje.items():
        if d == 0:
            s.append(u)
    out = False
    n = len(G)
    for i in range(n):
        if len(s) == i:
            return False
        if len(s) > i+1:
            out = True
        for u in G.izhodniSosedi(s[i]):
            stopnje[u] -= 1
            if stopnje[u] == 0:
                s.append(u)
    return out
