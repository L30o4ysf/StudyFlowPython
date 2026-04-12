import json
import os


class StudyFlow:
    def __init__(self):
        self.arquivo_dados = "dados.json"
        self.materias = self.carregar_dados()

    def carregar_dados(self):
        """RF03: Carrega as matérias do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def salvar_dados(self):
        """RF03: Salva o inventário no disco"""
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(self.materias, f, indent=4, ensure_ascii=False)

    def adicionar_materia(self, nome, prioridade):
        """RF01: Cadastra nova disciplina com validações"""
        if any(m['nome'].lower() == nome.lower() for m in self.materias):
            print("\n❌ Erro: Esta matéria já está no seu inventário.")
            return

        if prioridade not in [1, 2, 3]:
            print("\n❌ Erro: Prioridade deve ser 1, 2 ou 3.")
            return

        if len(nome) > 30:
            print("\n❌ Erro: O nome deve ter no máximo 30 caracteres.")
            return

        self.materias.append({"nome": nome, "prioridade": prioridade})
        self.salvar_dados()
        print(f"\n✅ '{nome}' adicionada com sucesso!")

    def obter_foco_diario(self):
        """RF02: Algoritmo de priorização (Top 3)"""
        ordenadas = sorted(
            self.materias, key=lambda x: x['prioridade'], reverse=True
        )
        return ordenadas[:3]


def exibir_menu():
    app = StudyFlow()

    while True:
        print("\n--- 📝 STUDYFLOW CLI ---")
        print("1. Cadastrar Matéria")
        print("2. Ver Foco do Dia")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da matéria: ")
            try:
                prio = int(input("Prioridade (1-Baixa, 3-Alta): "))
                app.adicionar_materia(nome, prio)
            except ValueError:
                print("\n❌ Erro: Digite um número válido.")

        elif opcao == "2":
            foco = app.obter_foco_diario()
            print("\n--- 🎯 MATÉRIAS PARA HOJE ---")
            if not foco:
                print("Seu inventário está vazio.")
            else:
                for i, m in enumerate(foco, 1):
                    print(f"{i}. {m['nome']} (Peso: {m['prioridade']})")

        elif opcao == "3":
            print("Encerrando... Bons estudos!")
            break
        else:
            print("\n❌ Opção inválida.")


if __name__ == "__main__":
    exibir_menu()
