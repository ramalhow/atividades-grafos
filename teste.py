from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta

from meu_grafo_matriz_adj_nao_dir import MeuGrafo

grafo = GrafoBuilder().tipo(MeuGrafo()).vertices(3).arestas(True).build()
tam = len(grafo.matriz)

for linhas in grafo.matriz:
    for dicio in range(tam):

        if len(dicio) == 0:
            for aresta in dicio:
                v1 = aresta.v1.rotulo
                v2 = aresta.v2.rotulo
                par = frozenset((v1, v2))

                if par not in nao_adj:
                    nao_adj.add(f"{v1}-{v2}")
        tam = tam - 1