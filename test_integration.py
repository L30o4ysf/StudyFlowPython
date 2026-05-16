import unittest
import os
from main import StudyFlow

class TestStudyFlowIntegration(unittest.TestCase):
    def setUp(self):
        """Executado antes de cada teste: cria um ambiente isolado"""
        self.filename_teste = "dados_teste.json"
        self.app = StudyFlow(filename=self.filename_teste)

    def tearDown(self):
        """Executado após cada teste: limpa os arquivos temporários gerados"""
        if os.path.exists(self.filename_teste):
            os.remove(self.filename_teste)

    def test_api_conexao_sucesso(self):
        """Valida se o método consegue consultar a API real e retornar a estrutura correta"""
        resultado = self.app.buscar_frase_motivacional()
        
        self.assertIsInstance(resultado, str)
        
        self.assertTrue(resultado.startswith("💡 Pílula de Foco:"))
        
        frase_offline = "💡 Pílula de Foco: Faça o seu melhor hoje, um passo de cada vez!"
        self.assertNotEqual(resultado, frase_offline, "O sistema usou a frase padrão offline. A conexão com a API falhou.")

if __name__ == "__main__":
    unittest.main()