from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta

from meu_grafo_lista_adj_nao_dir import MeuGrafo

# grafo baseado no exemplo mostrado na vídeo-aula da univesp:
# https://youtu.be/ovkITlgyJ2s?si=5uZsi4cQtIKnKzlR&t=534
grafo = (
    GrafoBuilder()
    .tipo(MeuGrafo())
    .vertices(
        [
            v0 := Vertice("V0"),
            v1 := Vertice("V1"),
            v2 := Vertice("V2"),
            v3 := Vertice("V3"),
            v4 := Vertice("V4"),
            v5 := Vertice("V5"),
        ]
    )
    .arestas(
        [
            Aresta("a1", v0, v1, 10),
            Aresta("a2", v0, v2, 5),
            Aresta("a3", v1, v3, 1),
            Aresta("a4", v2, v3, 8),
            Aresta("a5", v2, v4, 2),
            Aresta("a6", v3, v4, 4),
            Aresta("a7", v3, v5, 4),
            Aresta("a8", v4, v5, 6),
        ]
    )
    .build()
)
print(grafo)

print(grafo.dijkstra("V0", "V3"))