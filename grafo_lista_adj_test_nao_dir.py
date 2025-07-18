import unittest
from meu_grafo_lista_adj_nao_dir import *
import gerar_grafos_teste
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo("test_json/grafo_pb.json", MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo("test_json/grafo_pb2.json", MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo("test_json/grafo_pb3.json", MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo("test_json/grafo_pb4.json", MeuGrafo())

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta("a1", "J", "C")
        self.g_p_sem_paralelas.adiciona_aresta("a2", "C", "E")
        self.g_p_sem_paralelas.adiciona_aresta("a3", "P", "C")
        self.g_p_sem_paralelas.adiciona_aresta("a4", "T", "C")
        self.g_p_sem_paralelas.adiciona_aresta("a5", "M", "C")
        self.g_p_sem_paralelas.adiciona_aresta("a6", "M", "T")
        self.g_p_sem_paralelas.adiciona_aresta("a7", "T", "Z")

        # Grafos completos
        self.g_c = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(["J", "C", "E", "P"])
            .arestas(True)
            .build()
        )

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()).vertices(3).arestas(True).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()).vertices(1).build()

        # Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo("test_json/grafo_l1.json", MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo("test_json/grafo_l2.json", MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo("test_json/grafo_l3.json", MeuGrafo())

        self.g_l4 = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices([v := Vertice("D")])
            .arestas([Aresta("a1", v, v)])
            .build()
        )

        self.g_l5 = (
            GrafoBuilder().tipo(MeuGrafo()).vertices(3).arestas(3, lacos=1).build()
        )

        # Grafos desconexos
        self.g_d = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [a := Vertice("A"), b := Vertice("B"), Vertice("C"), Vertice("D")]
            )
            .arestas([Aresta("asd", a, b)])
            .build()
        )

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()

        # Grafos esperados no BFS:

        # grafo da paraíba padrão
        self.bfs_grafo_pb = MeuGrafo()
        for v in ["J", "C", "E", "P", "T", "M", "Z"]:
            self.bfs_grafo_pb.adiciona_vertice(v)

        self.bfs_grafo_pb.adiciona_aresta("a1", "J", "C")
        self.bfs_grafo_pb.adiciona_aresta("a2", "C", "E")
        self.bfs_grafo_pb.adiciona_aresta("a4", "P", "C")
        self.bfs_grafo_pb.adiciona_aresta("a6", "T", "C")
        self.bfs_grafo_pb.adiciona_aresta("a7", "M", "C")
        self.bfs_grafo_pb.adiciona_aresta("a9", "T", "Z")

        # grafo paraíba sem paralelas
        self.bfs_pb_sem_paralelas = MeuGrafo()
        for v in ["J", "C", "E", "P", "M", "T", "Z"]:
            self.bfs_pb_sem_paralelas.adiciona_vertice(v)

        self.bfs_pb_sem_paralelas.adiciona_aresta("a1", "J", "C")
        self.bfs_pb_sem_paralelas.adiciona_aresta("a2", "C", "E")
        self.bfs_pb_sem_paralelas.adiciona_aresta("a3", "P", "C")
        self.bfs_pb_sem_paralelas.adiciona_aresta("a4", "T", "C")
        self.bfs_pb_sem_paralelas.adiciona_aresta("a5", "M", "C")
        self.bfs_pb_sem_paralelas.adiciona_aresta("a7", "T", "Z")

        # grafo completo
        self.bfs_g_completo = MeuGrafo()
        vertices = ["J", "C", "E", "P"]
        for v in vertices:
            self.bfs_g_completo.adiciona_vertice(v)

        self.bfs_g_completo.adiciona_aresta("a1", "J", "C")
        self.bfs_g_completo.adiciona_aresta("a2", "J", "E")
        self.bfs_g_completo.adiciona_aresta("a3", "J", "P")

        # grafo desconexo
        self.bfs_desconexo = MeuGrafo()
        self.bfs_desconexo.adiciona_vertice("A")
        self.bfs_desconexo.adiciona_vertice("B")
        self.bfs_desconexo.adiciona_aresta("asd", "A", "B")

        # grafo com laço
        self.bfs_laco = MeuGrafo()
        self.bfs_laco.adiciona_vertice("C")
        self.bfs_laco.adiciona_vertice("A")
        self.bfs_laco.adiciona_aresta("a1", "C", "A")

        # Grafos esperados no DFS:

        # grafo da paraíba padrão
        self.dfs_grafo_pb = MeuGrafo()
        for v in ["J", "C", "E", "P", "T", "M", "Z"]:
            self.dfs_grafo_pb.adiciona_vertice(v)

        self.dfs_grafo_pb.adiciona_aresta("a1", "J", "C")
        self.dfs_grafo_pb.adiciona_aresta("a2", "C", "E")
        self.dfs_grafo_pb.adiciona_aresta("a4", "P", "C")
        self.dfs_grafo_pb.adiciona_aresta("a6", "T", "C")
        self.dfs_grafo_pb.adiciona_aresta("a8", "M", "T")
        self.dfs_grafo_pb.adiciona_aresta("a9", "T", "Z")

        # grafo paraíba sem paralelas
        self.dfs_pb_sem_paralelas = MeuGrafo()
        for v in ["J", "C", "E", "P", "M", "T", "Z"]:
            self.dfs_pb_sem_paralelas.adiciona_vertice(v)

        self.dfs_pb_sem_paralelas.adiciona_aresta("a1", "J", "C")
        self.dfs_pb_sem_paralelas.adiciona_aresta("a2", "C", "E")
        self.dfs_pb_sem_paralelas.adiciona_aresta("a3", "P", "C")
        self.dfs_pb_sem_paralelas.adiciona_aresta("a4", "T", "C")
        self.dfs_pb_sem_paralelas.adiciona_aresta("a6", "M", "T")
        self.dfs_pb_sem_paralelas.adiciona_aresta("a7", "T", "Z")

        # grafo completo
        self.dfs_g_completo = MeuGrafo()
        vertices = ["J", "C", "E", "P"]
        for v in vertices:
            self.dfs_g_completo.adiciona_vertice(v)

        self.dfs_g_completo.adiciona_aresta("a1", "J", "C")
        self.dfs_g_completo.adiciona_aresta("a4", "C", "E")
        self.dfs_g_completo.adiciona_aresta("a6", "E", "P")

        # grafo desconexo
        self.dfs_desconexo = MeuGrafo()
        self.dfs_desconexo.adiciona_vertice("A")
        self.dfs_desconexo.adiciona_vertice("B")
        self.dfs_desconexo.adiciona_aresta("asd", "A", "B")

        # grafo com laço
        self.dfs_laco = MeuGrafo()
        self.dfs_laco.adiciona_vertice("D")

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta("a10", "J", "C"))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta("b1", "", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta("b1", "A", "C"))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta("")
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta("aa-bb")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta("x", "J", "V")
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta("a1", "J", "C")

    def test_remove_vertice(self):
        self.assertIsNone(self.g_r.remove_vertice("A"))
        self.assertFalse(self.g_r.existe_rotulo_vertice("A"))
        self.assertFalse(self.g_r.existe_rotulo_aresta("1"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice("A")
        self.assertFalse(self.g_r.get_aresta("1"))
        self.assertEqual(self.g_r.arestas_sobre_vertice("B"), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(
            self.g_p.vertices_nao_adjacentes(),
            {
                "J-E",
                "J-P",
                "J-M",
                "J-T",
                "J-Z",
                "C-Z",
                "E-P",
                "E-M",
                "E-T",
                "E-Z",
                "P-M",
                "P-T",
                "P-Z",
                "M-Z",
            },
        )
        self.assertEqual(
            self.g_d.vertices_nao_adjacentes(), {"A-C", "A-D", "B-C", "B-D", "C-D"}
        )
        self.assertEqual(
            self.g_d2.vertices_nao_adjacentes(),
            {"A-B", "A-C", "A-D", "B-C", "B-D", "C-D"},
        )
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau("J"), 1)
        self.assertEqual(self.g_p.grau("C"), 7)
        self.assertEqual(self.g_p.grau("E"), 2)
        self.assertEqual(self.g_p.grau("P"), 2)
        self.assertEqual(self.g_p.grau("M"), 2)
        self.assertEqual(self.g_p.grau("T"), 3)
        self.assertEqual(self.g_p.grau("Z"), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau("G"), 5)

        self.assertEqual(self.g_d.grau("A"), 1)
        self.assertEqual(self.g_d.grau("C"), 0)
        self.assertNotEqual(self.g_d.grau("D"), 2)
        self.assertEqual(self.g_d2.grau("A"), 0)

        # Completos
        self.assertEqual(self.g_c.grau("J"), 3)
        self.assertEqual(self.g_c.grau("C"), 3)
        self.assertEqual(self.g_c.grau("E"), 3)
        self.assertEqual(self.g_c.grau("P"), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau("A"), 5)
        self.assertEqual(self.g_l2.grau("B"), 4)
        self.assertEqual(self.g_l4.grau("D"), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice("J"), {"a1"})
        self.assertEqual(
            self.g_p.arestas_sobre_vertice("C"),
            {"a1", "a2", "a3", "a4", "a5", "a6", "a7"},
        )
        self.assertEqual(self.g_p.arestas_sobre_vertice("M"), {"a7", "a8"})
        self.assertEqual(self.g_l2.arestas_sobre_vertice("B"), {"a1", "a2", "a3"})
        self.assertEqual(self.g_d.arestas_sobre_vertice("C"), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice("A"), {"asd"})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice("A")

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_bfs(self):
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.bfs("A"))

        # grafo da paraíba padrão
        bfs_result = self.g_p.bfs("J")
        self.assertEqual(bfs_result, self.bfs_grafo_pb)

        # grafo pb sem paralelas
        pb_sem_paralelas = self.g_p_sem_paralelas.bfs("J")
        self.assertEqual(self.bfs_pb_sem_paralelas, pb_sem_paralelas)

        # grafo completo
        g_comp = self.g_c.bfs("J")
        self.assertEqual(g_comp, self.bfs_g_completo)

        # grafo desconexo
        g_desconexo = self.g_d.bfs("A")
        self.assertEqual(g_desconexo, self.bfs_desconexo)

        # grafo com laço
        g_laco = self.g_l3.bfs("C")
        self.assertEqual(g_laco, self.bfs_laco)

    def test_dfs(self):
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.dfs("A"))

        # grafo da paraíba padrão
        dfs_result = self.g_p.dfs("J")
        self.assertEqual(dfs_result, self.dfs_grafo_pb)

        # grafo pb sem paralelas
        pb_sem_paralelas = self.g_p_sem_paralelas.dfs("J")
        self.assertEqual(self.dfs_pb_sem_paralelas, pb_sem_paralelas)

        # grafo completo
        g_comp = self.g_c.dfs("J")
        self.assertEqual(g_comp, self.dfs_g_completo)

        # grafo desconexo
        g_desconexo = self.g_d.dfs("A")
        self.assertEqual(g_desconexo, self.dfs_desconexo)

        # grafo com laço
        g_laco = self.g_l3.dfs("D")
        self.assertEqual(g_laco, self.dfs_laco)


    def test_eh_conexo(self):
        # Grafo da Paraíba é conexo
        self.assertTrue(self.g_p.eh_conexo())

        # Grafo sem paralelas também é conexo
        self.assertTrue(self.g_p_sem_paralelas.eh_conexo())

        # Grafo desconexo
        self.assertFalse(self.g_d.eh_conexo())
        self.assertFalse(self.g_d2.eh_conexo())

        # Grafo com 1 vértice é considerado conexo
        self.assertTrue(self.g_c3.eh_conexo())

    def test_ha_ciclo(self):
        # Grafo com ciclo (g_p tem paralelas e ciclo)
        self.assertTrue(self.g_p.ha_ciclo())

        # Grafo sem paralelas e sem ciclo
        self.assertFalse(self.g_p_sem_paralelas.ha_ciclo())

        # Grafo completo (tem ciclos)
        self.assertTrue(self.g_c.ha_ciclo())
        self.assertTrue(self.g_c2.ha_ciclo())

        # Grafo com 1 vértice sem arestas não tem ciclo
        self.assertFalse(self.g_c3.ha_ciclo())

        # Grafo com laço é um ciclo
        self.assertTrue(self.g_l1.ha_ciclo())
        self.assertTrue(self.g_l4.ha_ciclo())

        # Grafo desconexo com aresta única — sem ciclo
        self.assertFalse(self.g_d.ha_ciclo())
        self.assertFalse(self.g_d2.ha_ciclo())

    def test_eh_arvore(self):
        # Grafo válido como árvore
        folhas = self.g_p_sem_paralelas.eh_arvore()
        self.assertIsInstance(folhas, list)
        self.assertEqual(set(folhas), {'J', 'E', 'P', 'Z'})  # grau 1

        # Grafo com ciclo — não é árvore
        self.assertFalse(self.g_p.eh_arvore())
        self.assertFalse(self.g_c.eh_arvore())
        self.assertFalse(self.g_l1.eh_arvore())

        # Grafo desconexo — não é árvore
        self.assertFalse(self.g_d.eh_arvore())
        self.assertFalse(self.g_d2.eh_arvore())

        # Grafo com 1 vértice e sem aresta é uma árvore com 1 "folha"
        self.assertEqual(self.g_c3.eh_arvore(), ['A'])

    def test_eh_bipartido(self):
        # Grafo sem paralelas (em forma de árvore) é bipartido
        self.assertTrue(self.g_p_sem_paralelas.eh_bipartido())

        # Grafo da Paraíba tem paralelas e ciclo ímpar — não bipartido
        self.assertFalse(self.g_p.eh_bipartido())

        # Grafo completo com 3 vértices — tem ciclo ímpar — não bipartido
        self.assertFalse(self.g_c2.eh_bipartido())

        # Grafo com laço — não pode ser bipartido
        self.assertFalse(self.g_l1.eh_bipartido())
        self.assertFalse(self.g_l4.eh_bipartido())

        # Grafo com 1 vértice é bipartido
        self.assertTrue(self.g_c3.eh_bipartido())

        # Grafo desconexo com vértices isolados — ainda é bipartido
        self.assertTrue(self.g_d2.eh_bipartido())

        # Grafo com uma aresta (2 vértices) — é bipartido
        self.assertTrue(self.g_r.eh_bipartido())
