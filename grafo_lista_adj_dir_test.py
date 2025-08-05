import unittest
from meu_grafo_lista_adj_dir import MeuGrafo
from bibgrafo.aresta import ArestaDirecionada
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import VerticeInvalidoError, ArestaInvalidaError
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
        self.g_p4 = GrafoJSON.json_to_grafo("test_json/grafo_pb5.json", MeuGrafo())

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
        self.g_p_sem_paralelas.adiciona_aresta("a3", "C", "P")
        self.g_p_sem_paralelas.adiciona_aresta("a4", "C", "T")
        self.g_p_sem_paralelas.adiciona_aresta("a5", "C", "M")
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
            .arestas([ArestaDirecionada("a1", v, v)])
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
            .arestas([ArestaDirecionada("asd", a, b)])
            .build()
        )

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # caminhos coonstruidos pelo algoritmo de dijkstra
        self.result_caminho_j_z = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    j := Vertice("J"),
                    c := Vertice("C"),
                    t := Vertice("T"),
                    z := Vertice("Z"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a1", j, c),
                    ArestaDirecionada("a4", c, t),
                    ArestaDirecionada("a7", t, z),
                ]
            )
            .build()
        )

        self.result_caminho_c_p = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    c := Vertice("C"),
                    p := Vertice("P"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a3", c, p),
                ]
            )
            .build()
        )

        self.result_caminho_g_c = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    j := Vertice("J"),
                    p := Vertice("P"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a3", j, p),
                ]
            )
            .build()
        )

        self.result_caminho_paralelas = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    j := Vertice("J"),
                    c := Vertice("C"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a10", j, c),
                ]
            )
            .build()
        )

        self.result_caminho_pesos = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    a := Vertice("A"),
                    b := Vertice("B"),
                    c := Vertice("C"),
                    d := Vertice("D"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a1", a, b, 5),
                    ArestaDirecionada("a2", b, c, 1),
                    ArestaDirecionada("a3", c, d, 1),
                ]
            )
            .build()
        )

        self.result_caminho_multiplo_op1 = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    a := Vertice("A"),
                    b := Vertice("B"),
                    d := Vertice("D"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a1", a, b),
                    ArestaDirecionada("a3", b, d),
                ]
            )
            .build()
        )

        self.result_caminho_multiplo_op2 = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    a := Vertice("A"),
                    c := Vertice("C"),
                    d := Vertice("D"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a2", a, c),
                    ArestaDirecionada("a4", c, d),
                ]
            )
            .build()
        )

        # grafo baseado no exemplo mostrado na vídeo-aula da univesp:
        # https://youtu.be/ovkITlgyJ2s?si=5uZsi4cQtIKnKzlR&t=534
        self.grafo_exemplo_yt = (
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

        # resultado esperado do grafo acima:
        self.result_grafo_yt = (
            GrafoBuilder()
            .tipo(MeuGrafo())
            .vertices(
                [
                    v0 := Vertice("V0"),
                    v2 := Vertice("V2"),
                    v4 := Vertice("V4"),
                    v5 := Vertice("V5"),
                ]
            )
            .arestas(
                [
                    ArestaDirecionada("a2", v0, v2, 5),
                    ArestaDirecionada("a5", v2, v4, 2),
                    ArestaDirecionada("a8", v4, v5, 6),
                ]
            )
            .build()
        )

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta("a10", "J", "C"))
        a = ArestaDirecionada(
            "zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z")
        )
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
        self.assertEqual(self.g_p.grau_saida("J"), 1)
        self.assertEqual(self.g_p.grau_entrada("J"), 0)
        self.assertEqual(self.g_p.grau_saida("C"), 2)
        self.assertEqual(self.g_p.grau_entrada("C"), 5)
        self.assertEqual(self.g_p.grau_saida("E"), 0)
        self.assertEqual(self.g_p.grau_entrada("E"), 2)
        self.assertEqual(self.g_p.grau_saida("P"), 2)
        self.assertEqual(self.g_p.grau_entrada("P"), 0)
        self.assertEqual(self.g_p.grau_saida("M"), 2)
        self.assertEqual(self.g_p.grau_entrada("M"), 0)
        self.assertEqual(self.g_p.grau_saida("T"), 2)
        self.assertEqual(self.g_p.grau_entrada("T"), 1)
        self.assertEqual(self.g_p.grau_saida("Z"), 0)
        self.assertEqual(self.g_p.grau_entrada("Z"), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau_saida("G"), 5)

        self.assertEqual(self.g_d.grau_entrada("A"), 0)
        self.assertEqual(self.g_d.grau_saida("A"), 1)
        self.assertEqual(self.g_d.grau_entrada("C"), 0)
        self.assertEqual(self.g_d.grau_saida("C"), 0)
        self.assertNotEqual(self.g_d.grau_entrada("D"), 2)
        self.assertNotEqual(self.g_d.grau_entrada("D"), 2)
        self.assertEqual(self.g_d2.grau_entrada("A"), 0)
        self.assertNotEqual(self.g_d.grau_saida("D"), 2)

        # Completos
        self.assertEqual(self.g_c.grau_entrada("J"), 0)
        self.assertEqual(self.g_c.grau_saida("J"), 3)
        self.assertEqual(self.g_c.grau_entrada("C"), 1)
        self.assertEqual(self.g_c.grau_saida("C"), 2)
        self.assertEqual(self.g_c.grau_saida("E"), 1)
        self.assertEqual(self.g_c.grau_entrada("E"), 2)
        self.assertEqual(self.g_c.grau_saida("P"), 0)
        self.assertEqual(self.g_c.grau_entrada("P"), 3)

        # Com laço.
        self.assertEqual(self.g_l1.grau_saida("A"), 2)
        self.assertEqual(self.g_l1.grau_entrada("A"), 3)
        self.assertEqual(self.g_l2.grau_entrada("B"), 2)
        self.assertEqual(self.g_l2.grau_saida("B"), 2)
        self.assertEqual(self.g_l4.grau_entrada("D"), 1)
        self.assertEqual(self.g_l4.grau_saida("D"), 1)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())  # X
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())  # X
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())  # X
        self.assertTrue(self.g_p3.ha_paralelas())
        self.assertFalse(self.g_p4.ha_paralelas())

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

    def test_dijkstra(self):
        # Teste com grafo da Paraíba
        caminho_j_z = self.g_p_sem_paralelas.dijkstra("J", "Z")
        self.assertEqual(caminho_j_z, self.result_caminho_j_z)

        caminho_c_p = self.g_p_sem_paralelas.dijkstra("C", "P")
        self.assertEqual(caminho_c_p, self.result_caminho_c_p)

        # Teste com grafo completo
        caminho_completo = self.g_c.dijkstra("J", "P")
        self.assertEqual(caminho_completo, self.result_caminho_g_c)
        self.assertEqual(
            len(caminho_completo.arestas), 1
        )  # Qualquer aresta direta serve

        # Teste com grafo desconexo (sem caminho)
        self.assertIsNone(self.g_d.dijkstra("A", "D"))
        self.assertIsNone(self.g_d2.dijkstra("A", "B"))

        # Teste com mesmo vértice para início e fim
        caminho_trivial = self.g_p_sem_paralelas.dijkstra("J", "J")
        self.assertEqual(caminho_trivial.vertices, [Vertice("J")])
        self.assertEqual(caminho_trivial.arestas, {})

        # Teste com vértices inválidos
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.dijkstra("X", "J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.dijkstra("J", "X")

        # Teste com aresta de peso negativo (deve lançar exceção)
        g_com_peso_negativo = MeuGrafo()
        g_com_peso_negativo.adiciona_vertice("A")
        g_com_peso_negativo.adiciona_vertice("B")
        g_com_peso_negativo.adiciona_aresta("a1", "A", "B", -1)
        with self.assertRaises(Exception):
            g_com_peso_negativo.dijkstra("A", "B")

        # Teste com caminho mais longo mas com peso total menor
        g_pesos = MeuGrafo()
        for v in ["A", "B", "C", "D"]:
            g_pesos.adiciona_vertice(v)
        g_pesos.adiciona_aresta("a1", "A", "B", 5)
        g_pesos.adiciona_aresta("a2", "B", "C", 1)
        g_pesos.adiciona_aresta("a3", "C", "D", 1)
        g_pesos.adiciona_aresta("a4", "A", "D", 10)  # Caminho direto mais caro

        caminho_pesos = g_pesos.dijkstra("A", "D")
        self.assertEqual(caminho_pesos, self.result_caminho_pesos)

        # Teste com grafo que tem múltiplos caminhos com mesmo peso mínimo
        g_multiplos_caminhos = MeuGrafo()
        for v in ["A", "B", "C", "D"]:
            g_multiplos_caminhos.adiciona_vertice(v)
        g_multiplos_caminhos.adiciona_aresta("a1", "A", "B", 1)
        g_multiplos_caminhos.adiciona_aresta("a2", "A", "C", 1)
        g_multiplos_caminhos.adiciona_aresta("a3", "B", "D", 1)
        g_multiplos_caminhos.adiciona_aresta("a4", "C", "D", 1)

        caminho_multiplo = g_multiplos_caminhos.dijkstra("A", "D")
        # Deve retornar um dos caminhos mínimos
        self.assertTrue(
            caminho_multiplo == self.result_caminho_multiplo_op1
            or caminho_multiplo == self.result_caminho_multiplo_op2
        )
        self.assertEqual(len(caminho_multiplo.arestas), 2)

        # Teste com grafo mais complexo:
        caminho_grafo_yt = self.grafo_exemplo_yt.dijkstra("V0", "V5")
        self.assertTrue(caminho_grafo_yt, self.result_grafo_yt)
