# -*- coding: utf-8 -*-
class Kopica:
    """
    Dvojiška kopica z najmanjšo vrednostjo na vrhu.

    Kopica je predstavljena s seznamom,
    v katerem je i-ti vnos manjši od vnosov z indeksoma 2*i+1 in 2*i+2.
    Vsak vnos je trojica (vrednost, stevec, element),
    kjer je števec določen z vrstnim redom vnašanja
    in preprečuje primerjanje neprimerljivih elementov.
    """

    def __init__(self, slovar = None):
        """
        Inicializacija kopice.

        Elemente in vrednosti iz podanega slovarja organizira v kopico tako,
        da izvede spuščanje vsakega elementa od zadnjega proti prvemu.

        Časovna zahtevnost: O(n)
        """
        if slovar is None or len(slovar) == 0:
            self.seznam = []
            self.indeksi = {}
        else:
            self.seznam = [(v, i, e) for i, (e, v)
                           in enumerate(slovar.items())]
            self.indeksi = {x[2]: i for i, x in enumerate(self.seznam)}
            for i in reversed(range(len(self.seznam)//2)):
                self.spusti(i)
        self.stevec = len(self.seznam)

    def __len__(self):
        """
        Velikost kopice.

        Časovna zahtevnost: O(1)
        """
        return len(self.seznam)

    def __repr__(self):
        """
        Znakovna predstavitev kopice.

        Časovna zahtevnost: O(n)
        """
        return '[%s]' % ', '.join("%s: %s" % (e, v) for v, s, e in self.seznam)

    def __contains__(self, element):
        """
        Preveri, ali je element v kopici.

        Časovna zahtevnost: O(1)
        """
        return element in self.indeksi

    def __getitem__(self, element):
        """
        Vrne vrednost, ki je v kopici dodeljena elementu.

        Časovna zahtevnost: O(1)
        """
        return self.seznam[self.indeksi[element]][0]

    def __setitem__(self, element, vrednost):
        """
        Nastavi vrednost elementu v kopici.

        Če element že obstaja, mu nastavi novo vrednost
        ter glede na staro vrednost ustrezno popravi kopico.
        Če element še ne obstaja,
        ga doda na konec kopice ter ga dvigne do ustreznega mesta.

        Časovna zahtevnost: O(log(n))
        """
        if element in self.indeksi:
            i = self.indeksi[element]
            v, s, e = self.seznam[i]
            self.nadomesti(i, (vrednost, s, e))
        else:
            l = len(self.seznam)
            self.indeksi[element] = l
            self.seznam.append((vrednost, self.stevec, element))
            self.stevec += 1
            self.dvigni(l)

    def __delitem__(self, element):
        """
        Odstrani element iz kopice.

        Odstrani zadnji element kopice ter z njim prepiše brisani element,
        nato pa glede na vrednosti ustrezno popravi kopico.

        Časovna zahtevnost: O(log(n))
        """
        i = self.indeksi.pop(element)
        vnos = self.seznam.pop()
        if i < len(self.seznam):
            self.nadomesti(i, vnos)

    def nadomesti(self, i, vnos):
        """
        Nadomesti vnos na mestu i z novim vnosom.

        Glede na vrednosti v starem in novem vnosu
        slednjega bodisi spusti ali dvigne do ustreznega mesta.

        Časovna zahtevnost O(log(i) + log(n-i))
        """
        star = self.seznam[i]
        self.seznam[i] = vnos
        self.indeksi[vnos[2]] = i
        if star < vnos:
            self.spusti(i)
        else:
            self.dvigni(i)

    def vrh(self):
        """
        Vrne element na vrhu kopice in njegovo vrednost.

        Časovna zahtevnost: O(1)
        """
        vrednost, stevec, element = self.seznam[0]
        return (element, vrednost)

    def poberi(self):
        """
        Odstrani in vrne element na vrhu kopice in njegovo vrednost.

        Časovna zahtevnost: O(log(n))
        """
        vrednost, stevec, element = self.seznam[0]
        del self[element]
        return (element, vrednost)

    def dvigni(self, i):
        """
        Dvigne element na mestu i do ustreznega mesta.

        Časovna zahtevnost: O(log(i))
        """
        j = (i-1)//2
        while i > 0 and self.seznam[j] > self.seznam[i]:
            self.seznam[i], self.seznam[j] = self.seznam[j], self.seznam[i]
            self.indeksi[self.seznam[i][2]] = i
            self.indeksi[self.seznam[j][2]] = j
            i = j
            j = (i-1)//2

    def spusti(self, i):
        """
        Spusti element na mestu i do ustreznega mesta.

        Časovna zahtevnost: O(log(n-i))
        """
        l = len(self.seznam)
        j = 2*i + 1
        while j < l:
            k = j + 1
            if k < l and self.seznam[j] > self.seznam[k]:
                j = k
            if self.seznam[i] < self.seznam[j]:
                return
            self.seznam[i], self.seznam[j] = self.seznam[j], self.seznam[i]
            self.indeksi[self.seznam[i][2]] = i
            self.indeksi[self.seznam[j][2]] = j
            i = j
            j = 2*i + 1
