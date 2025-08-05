from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import VerticeInvalidoError


class MeuGrafo(GrafoListaAdjacenciaDirecionado):
    def vertices_nao_adjacentes(self):
        """
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        """
        pass  # Apague essa instrução e inicie seu código aqui

    def ha_laco(self):
        """
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        """
        pass

    def grau_entrada(self, V=""):
        """
        Provê o grau de entrada do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        """
        pass

    def grau_saida(self, V=""):
        """
        Provê o grau de saída do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        """
        pass

    def ha_paralelas(self):
        """
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        """
        pass

    def arestas_sobre_vertice(self, V):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        rotulos_arestas = {
            rotulo
            for rotulo, aresta in self.arestas.items()
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V
        }

        return rotulos_arestas

    def eh_completo(self):
        """
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        """
        pass

    def dijkstra(self, inicio="", fim=""):
        if not self.existe_rotulo_vertice(inicio) or not self.existe_rotulo_vertice(
            fim
        ):
            raise VerticeInvalidoError

        for rotulo in self.arestas:
            if self.arestas[rotulo].peso < 0:
                raise Exception(
                    "Não é possível calcular o menor caminho, há arestas com peso negativo."
                )

        # Inicialização
        distancias = {v.rotulo: float("inf") for v in self.vertices}
        distancias[inicio] = 0
        precedentes = {v.rotulo: None for v in self.vertices}
        nao_visitados = {v.rotulo for v in self.vertices}

        while nao_visitados:
            # Encontra o vértice não visitado com menor distância
            atual = min(nao_visitados, key=lambda v: distancias[v])

            # Remove o vértice atual do conjunto de não visitados
            nao_visitados.remove(atual)

            # Se chegamos ao destino, podemos parar
            if atual == fim:
                break

            # Se a menor distância é infinita, os vértices restantes são inalcançáveis
            if distancias[atual] == float("inf"):
                break

            # Atualiza as distâncias dos vizinhos (apenas arestas de saída)
            for aresta_rotulo in self.arestas_sobre_vertice(atual):
                aresta = self.arestas[aresta_rotulo]

                # Considera apenas arestas que saem do vértice atual (direcionado)
                if aresta.v1.rotulo == atual:
                    vizinho = aresta.v2.rotulo
                    distancia_candidata = distancias[atual] + aresta.peso
                    if distancia_candidata < distancias[vizinho]:
                        distancias[vizinho] = distancia_candidata
                        precedentes[vizinho] = atual

        # Reconstrução do caminho se existir
        if precedentes[fim] is None and inicio != fim:
            return None

        # Cria o grafo do caminho mínimo
        caminho = MeuGrafo()
        atual = fim

        # Adiciona todos os vértices do caminho (na ordem inversa)
        vertices_caminho = []
        while atual is not None:
            vertices_caminho.append(atual)
            atual = precedentes[atual]
        vertices_caminho.reverse()

        for v in vertices_caminho:
            caminho.adiciona_vertice(v)

        # Adiciona as arestas do caminho (na ordem correta)
        for i in range(len(vertices_caminho) - 1):
            origem = vertices_caminho[i]
            destino = vertices_caminho[i + 1]

            # Encontra a aresta entre origem e destino
            for aresta_rotulo in self.arestas_sobre_vertice(origem):
                aresta = self.arestas[aresta_rotulo]
                if aresta.v1.rotulo == origem and aresta.v2.rotulo == destino:
                    caminho.adiciona_aresta(aresta)
                    break

        return caminho
