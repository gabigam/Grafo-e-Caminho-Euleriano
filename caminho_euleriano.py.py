def Cad_eul_fec(adj):

    if len(adj) == 0:
        return

    c_atual = [0]
    cad = []

    while c_atual:
        v_atual = c_atual[-1]

        if adj[v_atual]:
            prox_v = adj[v_atual].pop()
            c_atual.append(prox_v)
        else:
            cad.append(c_atual.pop())

    for i in range(len(cad) - 1, -1, -1):
        print(cad[i], end="")
        if i:
            print(" -> ", end="")


if __name__ == "__main__":


	adj1 = [0] * 8
	for i in range(8):
		adj1[i] = []

	adj1[0].append(1)
	adj1[1].append(2)
	adj1[2].append(3)
	adj1[2].append(6)
	adj1[3].append(4)
	adj1[4].append(5)
	adj1[5].append(2)
	adj1[6].append(7)
	adj1[7].append(0)
	Cad_eul_fec(adj1)
	print()

	adj2 = [0] * 9
	for i in range(9):
		adj2[i] = []

	adj2[0].append(2)
	adj2[1].append(2)
	adj2[2].append(4)
	adj2[2].append(6)
	adj2[3].append(5)
	adj2[4].append(6)
	adj2[5].append(7)
	adj2[6].append(3)
	adj2[6].append(8)
	adj2[7].append(0)
	adj2[8].append(1)
	Cad_eul_fec(adj2)
	print()

	adj3 = [0] * 10
	for i in range(10):
		adj3[i] = []


	adj3[0].append(6)
	adj3[1].append(0)
	adj3[2].append(1)
	adj3[3].append(4)
	adj3[4].append(6)
	adj3[5].append(7)
	adj3[6].append(2)
	adj3[6].append(7)
	adj3[7].append(8)
	adj3[7].append(9)
	adj3[8].append(9)
	adj3[9].append(3)
	adj3[9].append(5)
	Cad_eul_fec(adj3)
	print()


