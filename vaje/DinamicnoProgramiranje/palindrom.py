# -*- coding: utf-8 -*-
def palindrom(s):
    """
    Najdaljši palindromski strnjen podniz.

    Časovna zahtevnost: O(n^2),
    kjer je n dolžina vhodnega niza

    Za algoritem, ki teče v času O(n), glej
    https://en.wikipedia.org/wiki/Longest_palindromic_substring
    """
    n = len(s)
    V = {(i, i+1): True for i in range(n)}
    for i in range(1, n):
        V[i-1, i+1] = s[i-1] == s[i]
    for j in range(2, n):
        for i in range(n-j):
            V[i, i+j+1] = V[i+1, i+j] and s[i] == s[i+j]
    l, i = max((j-i, i) for (i, j), b in V.items() if b)
    return (i, s[i:i+l])
