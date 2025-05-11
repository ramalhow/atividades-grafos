from meu_grafo_lista_adj_nao_dir import *
from bibgrafo.grafo_json import GrafoJSON

g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

print(g_p)