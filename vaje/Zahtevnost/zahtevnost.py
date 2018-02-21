# -*- coding: utf-8 -*-
def zrcaliMatriko(A):
    """
    Prezrcali vsebino matrike A dimenzij n×n pod diagonalo
    na ustrezno mesto nad diagonalo.

    Originalna vsebina nad diagonalo se izgubi.
    Po izvajanju je A simetrična matrika.

    Časovna zahtevnost: O(n^2)
    """
    n = len(A)
    assert all(len(l) == n for l in A)
    for i in range(n):
        for j in range(i+1, n):
            A[i][j] = A[j][i]

def stetje(n):
    """
    Simulira potek spreminjanja binarnega števca od 0 do 2^n-1.

    Časovna zahtevnost: O(2^n)
    """
    l = [0] * n
    i = 0
    print(l)
    while i < n:
        l[i] = 1 - l[i]
        if l[i] == 1:
            print(l)
            i = 0
        else:
            i += 1

def bubbleSort(l):
    """
    Algoritem mehurčnega urejanja seznama l z n elementi.

    Časovna zahtevnost: O(n^2) (povprečna in najslabša)
    """
    z = len(l)
    while z > 1:
        y = 0
        for i in range(1, z):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
                y = i
        z = y

def mergeSort(l):
    """
    Algoritem urejanja z zlivanjem seznama l z n elementi.

    Časovna zahtevnost: O(n log n)
    """
    n = len(l)
    if n <= 1:
        return l
    l1 = mergeSort(l[:n//2])
    l2 = mergeSort(l[n//2:])
    l = []
    i, j = 0, 0
    n1, n2 = len(l1), len(l2)
    while i < n1 and j < n2:
        if l1[i] < l2[j]:
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    l.extend(l1[i:])
    l.extend(l2[j:])
    return l
