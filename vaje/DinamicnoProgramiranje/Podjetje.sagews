︠61cb804e-2a32-4040-a438-3b96707edc48s︠
# Pripravimo spremenljivke
x1, x2, x3, z = var('x1 x2 x3 z') # z leži na intervalu [0, 4]
res = [x1, x2, x3]

# Iščemo maksimum D3 za x3 na intervalu [0, z]
D3 = 0.6 + 0.07*x3 # linearna funkcija s pozitivnim smernim koeficientom, maksimum je na desnem robu intervala
# Maksimum je dosežen pri x3 = z
D3 = D3.subs(x3 = z)
res = [x.subs(x3 = z) for x in res]

# Iščemo maksimum D2 za x2 na intervalu [0, z]
D2 = (0.4 + 0.1*x2) * D3.subs(z = z-x2)
D2.expand() # kvadratna funkcija z negativnim vodilnim koeficientom, maksimum je na robu ali v lokalnem ekstremu
︡10f85559-5e40-4fa9-a458-c1a723622188︡{"stdout":"-0.00700000000000000*x2^2 + 0.00700000000000000*x2*z + 0.0320000000000000*x2 + 0.0280000000000000*z + 0.240000000000000\n"}︡{"done":true}︡
︠e847dd91-2339-4a37-9825-51cbbf3fafaas︠
sol2 = solve(D2.derivative(x2) == 0, x2) # poiščemo točko z ničelnim odvodom
sol2 # koeficienta sta pozitivna, točka bo zagotovo večja od 0
sz2 = (x2 <= z).subs(sol2).solve(z) # preverimo, ali točka leži v našem intervalu
sz2
sz2[0][0].rhs().n() # točka je v intervalu za vrednosti z izven območja zanimanja
︡d5f5c015-ef2a-4e7b-bd76-5ffa7085a605︡{"stdout":"[x2 == 1/2*z + 16/7]\n"}︡{"stdout":"[[z >= (32/7)]]\n"}︡{"stdout":"4.57142857142857\n"}︡{"done":true}
︠f7062351-21b1-4593-beae-0504280c0bcbs︠
# Maksimum je v desnem robu intervala pri x2 = z
D2 = D2.subs(x2 = z)
res = [x.subs(z = 0, x2 = z) for x in res]

# Iščemo maksimum D1 za x1 na intervalu [0, 4]
D1 = x1*(10-x1) * D2.subs(z = 4-x1)
D1.expand() # kubična funkcija s pozitivnim vodilnim koeficientom, maksimum je na robu ali v manjšem lokalnem ekstremu
︡c8f712a6-383a-4a21-be8b-88520e01d642︡{"stdout":"0.0600000000000000*x1^3 - 1.08000000000000*x1^2 + 4.80000000000000*x1\n"}︡{"done":true}︡
︠d223424e-3584-4e45-bf14-e35ba5a6bcb5s︠
sol1 = solve(D1.derivative(x1) == 0, x1) # poiščemo točki z ničelnim odvodom
sol1
[e.rhs().n() for e in sol1] # pogledamo, kje sta ničelna odvoda
︡ae8d6afc-4728-4c11-b342-1c59777174a7︡{"stdout":"[x1 == -2/3*sqrt(21) + 6, x1 == 2/3*sqrt(21) + 6]\n"}︡{"stdout":"[2.94494953669611, 9.05505046330389]\n"}︡{"done":true}︡
︠d7d52d48-86bc-439a-a54f-009f21beddd4s︠
# Prvi lokalni ekstrem je znotraj intervala, drugi pa zunaj
# Maksimum je torej v prvem lokalnem ekstremu
D1 = D1.subs(sol1[0])
res = [x.subs(z = 4-x1).subs(sol1[0]) for x in res]
D1.expand() # vrednost opimalne rešitve
D1.n()
︡ddd86c84-b300-4190-9f3e-f76beb45a5a9︡{"stdout":"0.746666666666666*sqrt(21) + 2.88000000000000\n"}︡{"stdout":"6.30165651890036\n"}︡{"done":true}︡
︠0e47791d-a8c7-47ca-b1f7-74d89a9c827cs︠
# Izpišimo še sredstva za vsako fazo
res
[n(x) for x in res]
︡585ec6c5-839b-43d4-beeb-d38f1930d034︡{"stdout":"[-2/3*sqrt(21) + 6, 2/3*sqrt(21) - 2, 0]\n"}︡{"stdout":"[2.94494953669611, 1.05505046330389, 0.000000000000000]\n"}︡{"done":true}
︠955b3660-bd62-46cf-a653-f4f89038388e︠









