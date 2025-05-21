from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

   def vertices_nao_adjacentes(self):
       '''
       Provê um conjunto de vértices não adjacentes no grafo.
       O conjunto terá o seguinte formato: {X-Z, X-W, ...}
       Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
       :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
       '''
       nao_adjacentes = set()
       adjacentes = set()

       # pre processa as arestas já existentes
       for aresta in self.arestas.values():
           par = frozenset((aresta.v1.rotulo, aresta.v2.rotulo))
           adjacentes.add(par)

       n = len(self.vertices)
       for i in range(n):
           for j in range(i + 1, n):
               v1 = self.vertices[i].rotulo
               v2 = self.vertices[j].rotulo
               par = frozenset((v1, v2))

               if par not in adjacentes:
                   nao_adjacentes.add(f"{v1}-{v2}")

       return nao_adjacentes

   def ha_laco(self):
       '''
       Verifica se existe algum laço no grafo.
       :return: Um valor booleano que indica se existe algum laço.
       '''

       for aresta in self.arestas.values():
           if aresta.v1 == aresta.v2:
               return True
       return False


   def grau(self, V=''):
       '''
       Provê o grau do vértice passado como parâmetro
       :param V: O rótulo do vértice a ser analisado
       :return: Um valor inteiro que indica o grau do vértice
       :raises: VerticeInvalidoError se o vértice não existe no grafo
       '''
       grau = 0

       if not self.existe_rotulo_vertice(V):
           raise VerticeInvalidoError()

       for aresta in self.arestas.values():
           if aresta.v1.rotulo == V:
               grau += 1
           if aresta.v2.rotulo == V:
               grau += 1
       return grau

   def ha_paralelas(self):
       '''
       Verifica se há arestas paralelas no grafo
       :return: Um valor booleano que indica se existem arestas paralelas no grafo.
       '''
       arestas_visitadas = set()

       for aresta in self.arestas.values():
           par = f"{aresta.v1.rotulo}-{aresta.v2.rotulo}"

           if par in arestas_visitadas:
               return True

           arestas_visitadas.add(par)

       return False


   def arestas_sobre_vertice(self, V):
       '''
       Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
       :param V: Um string com o rótulo do vértice a ser analisado
       :return: Uma lista os rótulos das arestas que incidem sobre o vértice
       :raises: VerticeInvalidoException se o vértice não existe no grafo
       '''

       if not self.existe_rotulo_vertice(V):
           raise VerticeInvalidoError()

       rotulos_arestas = {
           rotulo for rotulo, aresta in self.arestas.items()
           if aresta.v1.rotulo == V or aresta.v2.rotulo == V
       }

       return rotulos_arestas


   def eh_completo(self):
       '''
       Verifica se o grafo é completo.
       :return: Um valor booleano que indica se o grafo é completo
       '''

       if self.ha_laco() or self.ha_paralelas():
           return False

       completos = []
       n = len(self.vertices)
       a = len(self.arestas)

       arestas_esperadas = (n * (n-1)) // 2

       return a == arestas_esperadas
   
   def dfs(self, V=""):
        if not self.existe_rotulo_vertice(V):
           raise VerticeInvalidoError
       
        arvore_dfs = MeuGrafo()

        def search_dfs(V="") -> None:
            if not arvore_dfs.existe_rotulo_vertice(V):
                arvore_dfs.adiciona_vertice(V)
                print("add vertice: ", V)

            arestas_ord = sorted(self.arestas_sobre_vertice(V))
            print(f"arestas sobre o vertice {V}: ", arestas_ord)

            for aresta in arestas_ord:
                if (not arvore_dfs.existe_rotulo_aresta(aresta)) :
                    print("aresta nova + vertice não visitado!") 

                    v1 = self.arestas[aresta].v1.rotulo
                    v2 = self.arestas[aresta].v2.rotulo

                    vert_oposto = v1 if v1 != V else v2
                    
                    # evita laços 
                    if not arvore_dfs.existe_rotulo_vertice(vert_oposto):
                        print(f"vert oposto a {V}: ", vert_oposto)
                        arvore_dfs.adiciona_vertice(vert_oposto)

                        #Aresta(aresta, self.arestas[aresta].v1, self.arestas[aresta].v2)
                        arvore_dfs.adiciona_aresta(self.arestas[aresta])
                        print(f"add aresta: {aresta}")
                        
                        print(f"indo para vert oposto: {vert_oposto}")
                        print("avançando na recursão")
                        search_dfs(vert_oposto)
                    else:
                        print(f"o vertice {vert_oposto}")
                else:
                    print(f"ja viu a aresta {aresta}")    
        search_dfs(V)
        return arvore_dfs
   
   def bfs(self, V=""):
        if not self.existe_rotulo_vertice(V):
           raise VerticeInvalidoError
       
        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(V)
        
        fila = [V]
        visitados = []
        
        while fila:
            vert_atual = fila.pop(0)
            arestas_ord = sorted(self.arestas_sobre_vertice(vert_atual))
              
            for aresta in arestas_ord:
                v1 = self.arestas[aresta].v1.rotulo
                v2 = self.arestas[aresta].v2.rotulo

                vert_oposto = v1 if v1 != vert_atual else v2
                    
                if (vert_oposto not in visitados):
                    visitados.append(self.vertices[vert_oposto])
                    
                
                