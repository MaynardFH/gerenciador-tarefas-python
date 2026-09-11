import unittest
import app


class TestGerenciadorDeTarefas(unittest.TestCase):

    def setUp(self):
        app.tarefas.clear()

    def test_adicionar_tarefa(self):
        app.tarefas.append({
            "descricao": "Estudar Docker",
            "concluida": False
        })

        self.assertEqual(len(app.tarefas), 1)
        self.assertEqual(app.tarefas[0]["descricao"], "Estudar Docker")
        self.assertFalse(app.tarefas[0]["concluida"])

    def test_concluir_tarefa(self):
        app.tarefas.append({
            "descricao": "Estudar GitHub Actions",
            "concluida": False
        })

        app.tarefas[0]["concluida"] = True

        self.assertTrue(app.tarefas[0]["concluida"])


if __name__ == "__main__":
    unittest.main()