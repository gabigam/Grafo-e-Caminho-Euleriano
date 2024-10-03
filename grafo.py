def insere_vertice(vertice):
    if vertice in grafo:
        print(vertice,"esta presente no grafo")
    else:
        grafo[vertice]=[]

def delete_vertice(vertice):
   if vertice not in grafo:
        print(vertice,"nao esta presente no grafo")
   else:
       grafo.pop(vertice)
       for i in grafo:
           lista = grafo[i]
           if vertice in lista:
               lista.remove(vertice)

def insere_aresta(v1,v2):
    if v1 not in grafo:
        print(v1,"nao esta presente no grafo")
    elif v2 not in grafo:
        print(v2, "nao esta presente no grafo")
    else:
            grafo[v1].append(v2)
            grafo[v2].append(v1)

def delete_aresta(v1,v2):
    if v1 not in grafo:
        print(v1,"nao esta presente no grafo")
    elif v2 not in grafo:
        print(v2,"nao esta presente no grafo")
    else:
        if v2 in grafo[v1]:
            grafo[v1].remove(v2)
            grafo[v2].remove(v1)

def grau_vert(vertice):
    if vertice not in grafo:
        print(vertice, "nao esta presente no grafo")
    else:
        grau=len(grafo.pop(vertice))
        return grau

def det_viz(v1,v2):
    if v2 in grafo[v1]:
        print("os vertices",v1,v2,"sao vizinhos")
    else:
        print("os vertices",v1,v2, "nao sao vizinhos")

grafo = {}
insere_vertice(1)
insere_vertice(2)
insere_vertice(3)
insere_vertice(4)
insere_vertice(5)
insere_vertice(6)
delete_vertice(1)
insere_vertice(1)
insere_aresta(2,3)
insere_aresta(2,4)
insere_aresta(3,5)
insere_aresta(3,6)
insere_aresta(4,5)
insere_aresta(1,5)
delete_aresta(1,5)


print("O grafo:")
print(grafo)
det_viz(1,2)
det_viz(2,3)
print("o grau do vertice 1 é:")
print(grau_vert(1))
print("o grau do vertice 2 é:")
print(grau_vert(2))
print("o grau do vertice 3 é:")
print(grau_vert(3))
print("o grau do vertice 4 é:")
print(grau_vert(4))
print("o grau do vertice 5 é:")
print(grau_vert(5))
print("o grau do vertice 6 é:")
print(grau_vert(6))











