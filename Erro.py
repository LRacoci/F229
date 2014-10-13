v = [[], []]
v[0] = symbols("a I r")
v[1] = symbols("Ea EI Er")
pi = symbols("pi")

a, I, r = v[0]

Ea, EI, Er = v[1]


G = (8*pi*a*I)/(r**4)

def Erro(v, G):
	expr = 0
	for i in range(len(v[1])):
		expr += (diff(G, v[0][i]) * v[1][i])**2
	return sqrt(expr)

Erro(v, G)

#http://live.sympy.org/