import time
from bibgrafo.grafo_builder import GrafoBuilder
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta

from meu_grafo_lista_adj_nao_dir import MeuGrafo

grafo = GrafoJSON.json_to_grafo("test_json/grafo_pb.json", MeuGrafo())
print(grafo)
print(grafo.bfs("J"))


"""
print(g_p_sem_paralelas)

t1 = time.perf_counter(), time.process_time()

print(g_p_sem_paralelas.ha_ciclo())

t2 = time.perf_counter(), time.process_time()
print("ha_laco()")
print(f" Real time: {t2[0] - t1[0]} seconds")
print(f" CPU time: {t2[1] - t1[1]} seconds")
"""
