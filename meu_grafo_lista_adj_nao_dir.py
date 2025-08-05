from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import VerticeInvalidoError
from bibgrafo.vertice import Vertice


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):
    def vertices_nao_adjacentes(self):
        """
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        """
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
        """
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        """

        for aresta in self.arestas.values():
            if aresta.v1 == aresta.v2:
                return True
        return False

    def grau(self, V=""):
        """
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        """
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
        """
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        """
        arestas_visitadas = set()

        for aresta in self.arestas.values():
            par = f"{aresta.v1.rotulo}-{aresta.v2.rotulo}"

            if par in arestas_visitadas:
                return True

            arestas_visitadas.add(par)

        return False

    def arestas_sobre_vertice(self, V):
        """
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        """

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

        if self.ha_laco() or self.ha_paralelas():
            return False

        n = len(self.vertices)
        a = len(self.arestas)

        arestas_esperadas = (n * (n - 1)) // 2

        return a == arestas_esperadas

    def dfs(self, V=""):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arvore_dfs = MeuGrafo()

        def search_dfs(V="") -> None:
            if not arvore_dfs.existe_rotulo_vertice(V):
                arvore_dfs.adiciona_vertice(V)

            arestas_ord = sorted(self.arestas_sobre_vertice(V))

            for aresta in arestas_ord:
                if not arvore_dfs.existe_rotulo_aresta(aresta):
                    v1 = self.arestas[aresta].v1.rotulo
                    v2 = self.arestas[aresta].v2.rotulo

                    vert_oposto = v1 if v1 != V else v2

                    # evita laços
                    if not arvore_dfs.existe_rotulo_vertice(vert_oposto):
                        arvore_dfs.adiciona_vertice(vert_oposto)
                        arvore_dfs.adiciona_aresta(self.arestas[aresta])
                        search_dfs(vert_oposto)

        search_dfs(V)
        return arvore_dfs

    def bfs(self, V=""):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(V)

        fila = [V]
        visitados = [V]

        while fila:
            vert_atual = fila.pop(0)
            arestas_ord = sorted(self.arestas_sobre_vertice(vert_atual))

            for aresta in arestas_ord:
                v1 = self.arestas[aresta].v1.rotulo
                v2 = self.arestas[aresta].v2.rotulo

                vert_vizinho = v1 if v1 != vert_atual else v2

                if vert_vizinho not in visitados:
                    fila.append(vert_vizinho)
                    visitados.append(vert_vizinho)

                    if not arvore_bfs.existe_rotulo_vertice(vert_vizinho):
                        arvore_bfs.adiciona_vertice(vert_vizinho)

                    if not arvore_bfs.existe_rotulo_aresta(aresta):
                        arvore_bfs.adiciona_aresta(self.arestas[aresta])

        return arvore_bfs

    def eh_conexo(self):
        dfs = self.dfs(self.vertices[0].rotulo)
        return len(self.vertices) == len(dfs.vertices)

    # usando o algoritmo Union-Find
    def ha_ciclo(self):
        pais = {v.rotulo: v.rotulo for v in self.vertices}
        ranks = {v.rotulo: 0 for v in self.vertices}

        def find(x):
            if pais[x] != x:
                pais[x] = find(pais[x])
            return pais[x]

        ha_ciclo = False

        for aresta in self.arestas.values():
            v1 = aresta.v1.rotulo
            v2 = aresta.v2.rotulo

            # find
            pai_v1 = find(v1)
            pai_v2 = find(v2)

            if pai_v1 == pai_v2:
                ha_ciclo = True
                break

            if ranks[pai_v1] < ranks[pai_v2]:
                pais[pai_v1] = pai_v2

            elif ranks[pai_v1] > ranks[pai_v2]:
                pais[pai_v2] = pai_v1

            else:
                pais[pai_v2] = pai_v1
                ranks[pai_v1] += 1

        return ha_ciclo

    def eh_arvore(self):
        num_verts = len(self.vertices)
        num_arestas = len(self.arestas)

        # por definição, as arvores devem obdecer as seguintes condições:
        # - ser acíclico
        # - ser conexo
        # - o mínimo de arestas deve ser n-1, com n = número de vertices
        is_valid = (
            (not self.ha_ciclo())
            and (self.eh_conexo())
            and (num_arestas >= (num_verts - 1))
        )

        if not is_valid:
            return False

        folhas = list()
        for vert in self.vertices:
            if self.grau(vert.rotulo) == 1:
                folhas.append(vert.rotulo)

        return folhas

    def eh_bipartido(self):
        if (not self.vertices) or (not self.arestas):
            return False

        verts = [v.rotulo for v in self.vertices]
        for v in verts:
            cor = {}
            cor[v[0]] = 0

            fila = [v[0]]

            while fila:
                vert = fila.pop(0)

                for aresta in self.arestas_sobre_vertice(vert):
                    a = self.arestas[aresta]

                    # escolhendo o vertice adjacent/vizinho manualmente
                    if a.v1.rotulo == vert:
                        vizinho = a.v2.rotulo

                    elif a.v2.rotulo == vert:
                        vizinho = a.v1.rotulo

                    # atribuindo a cor oposto no vertice vizinho, se el já não foi adicionado
                    if vizinho not in cor:
                        cor[vizinho] = 1 - cor[vert]
                        fila.append(vizinho)
                    elif cor[vizinho] == cor[vert]:
                        return False

        return True

    def vertices_adjacentes(self, V=""):
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas_adj = self.arestas_sobre_vertice(V)
        vertices = []

        for aresta in arestas_adj:
            a = self.arestas[aresta]

            if a.v1.rotulo == V:
                vertices.append(a.v2.rotulo)
            else:
                vertices.append(a.v1.rotulo)

        return sorted(vertices)

    def dijkstra(self, inicio="", fim=""):
        if not self.existe_rotulo_vertice(inicio) or not self.existe_rotulo_vertice(fim):
            raise VerticeInvalidoError

        for rotulo in self.arestas:
            if self.arestas[rotulo].peso < 0:
                raise Exception(
                    "Não é possível calcular o menor caminho, há arestas com peso negativo."
                )

        # define todas as estimativas de distancias como "infinito",
        # exceto a distancia do v inicial para ele mesmo
        distancias = {v.rotulo: float("inf") for v in self.vertices}
        distancias[inicio] = 0
        
        # inicializa os precendetes com um valor inválido
        precedentes = {v.rotulo: None for v in self.vertices}
        
        # marca todos os vertices como abertos inicialmente
        aberto = {v.rotulo for v in self.vertices}
        fechado = set()

        while aberto:
            # escolha o menor valor de todo o grafo, desde que esteja aberto o vertice
            menor_vertice = min(aberto, key=lambda v: distancias[v])
            
            # atualiza as listas de vertices abertos e fechados
            aberto.remove(menor_vertice)
            fechado.add(menor_vertice)

            # se chegamos ao destino, podemos parar
            if menor_vertice == fim:
                break

            # atualiza distâncias dos vizinhos
            for aresta_rotulo in self.arestas_sobre_vertice(menor_vertice):
                aresta = self.arestas[aresta_rotulo]
                
                # acha o vertice vizinho
                if aresta.v1.rotulo == menor_vertice:
                    vizinho = aresta.v2.rotulo
                else:
                    vizinho = aresta.v1.rotulo

                # Ignora vértices já fechados
                if vizinho in fechado:
                    continue

                dist_total = distancias[menor_vertice] + aresta.peso
                if dist_total < distancias[vizinho]:
                    distancias[vizinho] = dist_total
                    precedentes[vizinho] = menor_vertice

        # conferindo se existe menor caminho
        if precedentes[fim] is None and inicio != fim:
            return None  # Não há caminho

        caminho = MeuGrafo()
        atual = fim

        # incluí os vertices no caminho
        while atual is not None:
            caminho.adiciona_vertice(atual)
            atual = precedentes[atual]

        # incluía as arestas no caminho
        atual = fim
        while precedentes[atual] is not None:
            anterior = precedentes[atual]
            
            # Encontra a aresta entre atual e anterior
            aresta_encontrada = None
            for aresta_rotulo in self.arestas_sobre_vertice(atual):
                aresta = self.arestas[aresta_rotulo]
                if (aresta.v1.rotulo == atual and aresta.v2.rotulo == anterior) or (
                    aresta.v1.rotulo == anterior and aresta.v2.rotulo == atual
                ):
                    aresta_encontrada = aresta
                    break

            if aresta_encontrada:
                caminho.adiciona_aresta(aresta_encontrada)
            atual = anterior

        return caminho
