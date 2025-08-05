from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.vertice import Vertice
from bibgrafo.aresta import ArestaDirecionada
from meu_grafo_lista_adj_dir import MeuGrafo

# grafo baseado no exemplo mostrado na vídeo-aula da univesp:
# https://youtu.be/ovkITlgyJ2s?si=5uZsi4cQtIKnKzlR&t=534
grafo_exemplo_yt = (
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
            ArestaDirecionada("a1", v0, v1, 10),
            ArestaDirecionada("a2", v0, v2, 5),
            ArestaDirecionada("a3", v1, v3, 1),
            ArestaDirecionada("a4", v2, v3, 8),
            ArestaDirecionada("a5", v2, v4, 2),
            ArestaDirecionada("a6", v3, v4, 4),
            ArestaDirecionada("a7", v3, v5, 4),
            ArestaDirecionada("a8", v4, v5, 6),
        ]
    )
    .build()
)

caminho_grafo_yt = grafo_exemplo_yt.dijkstra("V0", "V5")

print(caminho_grafo_yt)