︠534e3910-b94d-4af8-948a-834b0230f52e︠
pr = [
    [1, 0.8, 0.7, 0.4], # 0:  taščica 1
    [1, 0.8, 0.6, 0.4], # 1:  taščica 2
    [1, 0.9, 0.8, 0.5], # 2:  vrtna penica 1
    [1, 0.8, 0.8, 0.6], # 3:  vrtna penica 2
    [1, 0.8, 0.8, 0.5], # 4:  vrtna penica 3
    [1, 0.9, 0.7, 0.6], # 5:  vrtna penica 4
    [1, 0.8, 0.7, 0.4], # 6:  travniška cipa 1
    [1, 0.8, 0.8, 0.4], # 7:  travniška cipa 2
    [1, 0.7, 0.7, 0.5], # 8:  travniška cipa 3
    [1, 0.7, 0.5, 0.4], # 9:  bela pastirica 1
    [1, 0.7, 0.7, 0.4], # 10: bela pastirica 2
    [1, 0.6, 0.4, 0.1]  # 11: sova
]
n = len(pr)
m = len(pr[0])
︡0b1b78ff-8d88-4687-91ff-4c0536432619︡
︠90b4e5de-3854-40b6-a083-b0efcc21927d︠
p = MixedIntegerLinearProgram(maximization = True)
x = p.new_variable(binary = True)

p.set_objective(sum(sum(j*pr[i][j]*x[i, j] for j in range(1, m)) for i in range(n)))
p.add_constraint(sum(sum(j*x[i, j] for j in range(1, m)) for i in range(n)) == 16)
p.add_constraint(sum(sum(x[i, j]*j for j in range(1, m)) for i in [0, 1]) >= sum(sum(x[i, j]*j for j in range(1, m)) for i in [9, 10]) + 1)
p.add_constraint(sum(sum(x[i, j] for j in range(1, m)) for i in [2, 3, 4, 5]) >= 1)
p.add_constraint(sum(sum(x[i, j] for j in range(1, m)) for i in [6, 7, 8]) >= 1)
p.add_constraint(sum(sum(x[i, j] for j in range(1, m)) for i in [9, 10]) >= 1)
p.add_constraint(x[11, 1] + x[11, 2] + x[11, 3] >= 1)
p.add_constraint(x[0, 2] + x[0, 3] + x[10, 1] + x[10, 2] + x[10, 3] <= 1)

for i in range(n):
    p.add_constraint(x[i, 1] + x[i, 2] + x[i, 3] <= 1)

p.solve()
︡ee233dff-274f-4620-97ff-31ad0200c20f︡
res = p.get_values(x)
kuk = {i: j for (i, j), v in res.items() if v > 0}
kuk
sum(j*pr[i][j] for i, j in kuk.items())









