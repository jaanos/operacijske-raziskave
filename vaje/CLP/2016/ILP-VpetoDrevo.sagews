︠71a66a40-4818-4fc9-8a9e-9952493c1979︠
def utez(u, v):
    """Funkcija uteži"""
    return u + v
︡954d63fd-dfe5-41fc-81f9-9fad9ff19b80︡
︠ced6aa7e-69e7-4ce3-9218-d13238b82d58︠
G = graphs.PetersenGraph()
D = DiGraph(G)
n = G.order()

for u, v in D.edges(labels = False):
    D.set_edge_label(u, v, utez(u, v))

p = MixedIntegerLinearProgram(maximization = False)
w = p.new_variable()
x = p.new_variable(binary = True)

p.set_objective(sum(t * x[u, v] for u, v, t in D.edges(labels = True)))
p.add_constraint(sum(x[u, v] for u, v in D.edges(labels = False)) == n - 1)

for u in G.vertices():
    p.add_constraint(sum([x[u, v] for v in D.neighbors_out(u)]) <= 1)

for u, v in D.edges(labels = False):
    p.add_constraint(w[v] - w[u] - n * x[u, v] >= 1 - n)

p.solve()
︡8b7c9575-3309-40ca-bac6-d2f2a05143da︡
edges = p.get_values(x)
edges
cols = {'red': [k for k, v in edges.items() if v > 0]}
D.plot(edge_colors = cols, edge_labels = True)









