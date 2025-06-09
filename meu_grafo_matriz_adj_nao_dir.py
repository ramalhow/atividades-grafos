from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import VerticeInvalidoError


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        nao_adj = set()

        for linhas in self.matriz:
            for dicio in linhas:

                if len(dicio) == 0:
                    for aresta in dicio:
                        v1 = aresta.v1.rotulo
                        v2 = aresta.v2.rotulo
                        par = frozenset((v1, v2))

                        if par not in nao_adj:
                            nao_adj.add(f"{v1}-{v2}")

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        
        for vert in self.vertices:
            index = self.indice_do_vertice(self.get_vertice(vert.rotulo))
            dicio = self.matriz[index][index]

            if len(dicio) > 0:
                return True
            
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        index = self.indice_do_vertice(self.get_vertice(V))
        grau = 0

        for dicio in self.matriz[index]:
            for aresta in dicio:
                v1 = dicio[aresta].v1.rotulo
                v2 = dicio[aresta].v2.rotulo

                if V == v1:
                    grau += 1
                if V == v2:
                    grau += 1

        return grau


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for linhas in self.matriz:
            for dicio in linhas:
                if len(dicio) > 1:
                    return True
            
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        
        index = self.indice_do_vertice(self.get_vertice(V))
        rotulos = list()

        for dicio in self.matriz[index]:
            for aresta in dicio:
                rotulos.append(aresta)

        return rotulos

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.ha_paralelas():
            return False
        
        num_verts = len(self.vertices)
        num_arestas = 0

        for linhas in self.matriz:
            for dicio in linhas:
                num_arestas += len(dicio)

        arestas_esperadas = (num_verts * (num_verts - 1)) // 2
        return num_arestas == arestas_esperadas