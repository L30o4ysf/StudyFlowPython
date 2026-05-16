import json
import os
import urllib.request

class StudyFlow:
    def __init__(self, filename="dados.json"):
        self.filename = filename
        self.materias = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def salvar_dados(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.materias, f, ensure_ascii=False, indent=4)

    def cadastrar_materia(self, nome, prioridade):
        if not (1 <= len(nome) <= 30):
            print("X Erro: O nome da matéria deve ter entre 1 e 30 caracteres.")
            return False
        
        # RN02: Bloqueio de duplicados
        for mat in self.materias:
            if mat['nome'].lower() == nome.lower():
                print("X Erro: Esta matéria já está no seu inventário.")
                return False

        self.materias.append({"nome": nome, "prioridade": prioridade})
        self.salvar_dados()
        print(f"'{nome}' adicionada com sucesso!")
        return True

    def buscar_frase_motivacional(self):
        """Busca um conselho de uma API pública externa (Adviceslip)"""
        try:
            url = "https://api.adviceslip.com/advice"
            with urllib.request.urlopen(url, timeout=0.8) as response:
                dados = json.loads(response.read().decode('utf-8'))
                return f"💡 Pílula de Foco: \"{dados['slip']['advice']}\""
        except Exception:
            return "💡 Pílula de Foco: Faça o seu melhor hoje, um passo de cada vez!"

    def ver_foco_do_dia(self):
        if not self.materias:
            print("\nNenhuma matéria cadastrada ainda.")
            return

        print("\n--- 🧠 MATÉRIAS PARA HOJE ---")
        materias_ordenadas = sorted(self.materias, key=lambda x: x['prioridade'], reverse=True)
        
        for i, mat in enumerate(materias_ordenadas[:3], start=1):
            print(f"{i}. {mat['nome']} (Peso: {mat['prioridade']})")
        
        print("-" * 40)
        frase = self.buscar_frase_motivacional()
        print(frase)
        print("-" * 40)

def exibir_menu():
    print("\n--- 📑 STUDYFLOW CLI ---")
    print("1. Cadastrar Matéria")
    print("2. Ver Foco do Dia")
    print("3. Sair")

def main():
    app = StudyFlow()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Nome da matéria: ").strip()
            if not nome:
                print("X Erro: O nome não pode ser vazio.")
                continue
                
            prioridade_in = input("Prioridade (1-Baixa, 3-Alta): ").strip()
            # RN01: Validação de pesos numéricos 1, 2 ou 3
            if prioridade_in not in ["1", "2", "3"]:
                print("X Erro: Somente pesos numéricos (1, 2 ou 3) são aceitos.")
                continue
                
            app.cadastrar_materia(nome, int(prioridade_in))
            
        elif opcao == "2":
            app.ver_foco_do_dia()
            
        elif opcao == "3":
            print("Encerrando... Bons estudos!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()