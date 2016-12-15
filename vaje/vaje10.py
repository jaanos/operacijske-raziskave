# -*- coding: utf-8 -*-
"""
Funkcije na grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
"""
from vaje9 import topoloskaUreditev

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
