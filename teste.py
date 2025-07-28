from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta

from meu_grafo_matriz_adj_nao_dir import MeuGrafo

grafo = GrafoBuilder().tipo(MeuGrafo()) \
    .vertices([
    a := Vertice("A"),
    b := Vertice("B"),
    c := Vertice("C"),
    d := Vertice("D"),
]) \
    .arestas([
    Aresta("a1", a, b),
    Aresta("a2", b, c),
    Aresta("a3", c, d),
    Aresta("a4", d, a),

]) \
    .build()
'''
size = len(grafo.matriz)
start = 1
for linha in range(size):
    for coluna in range(start, size):
        print(f"coords: {linha}-{coluna}")
        print(len(grafo.matriz[linha][coluna]))

    start = start + 1
'''

print(grafo)

nao_adj = set()
for linha in grafo.matriz:
    for dicio in linha:
        print(dicio)

        if len(dicio) == 0:
            for aresta in dicio:
                v1 = aresta.v1.rotulo
                v2 = aresta.v2.rotulo
                nao_adj.add(f"{v1}-{v2}")


print(nao_adj)
'''
s = grafo.vertices_nao_adjacentes()
print(s)
'''
