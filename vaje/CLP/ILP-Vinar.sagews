p = MixedIntegerLinearProgram(maximization = True)
x = p.new_variable(binary = True)

p.set_objective(2000*x[1,1] + 10000*x[1,2] + 5000*x[1,3] +
                2200*x[2,1] + 5500*x[2,2] + 5500*x[2,3] +
                750*(x[3,1] + x[3,2] + x[3,3]) +
                1800*(x[4,1] + x[4,2] + x[4,3]))

for i in [1,2,3,4]:
    p.add_constraint(sum(x[i,j] for j in [1,2,3]) <= 1)
for j in [1,2,3]:
    p.add_constraint(sum(x[i,j] for i in [1,2,3,4]) <= 1)
p.add_constraint(x[4,1] + x[4,2] == 0)
p.add_constraint(x[1,2] - x[2,1] <= 0)
p.add_constraint(sum(x[3,j] + x[4,j] - x[1,j] for j in [1,2,3]) >= 0)
p.add_constraint(x[1,1] + x[2,2] + sum(x[i,3] for i in [1,2,4]) <= 2)

p.solve()
︡43eed5c3-6f6f-43a2-8b4b-abc9e6596b7f︡
res = p.get_values(x)
{i: j for (i, j), v in res.items() if v > 0}









