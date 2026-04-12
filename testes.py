from main import StudyFlow
import os

def testar_sistema():
    print("🧪 Iniciando Testes Automatizados...")
    app = StudyFlow()
    app.materias = []

    app.adicionar_materia("Matemática", 3)
    assert len(app.materias) == 1
    print("✅ Teste 1: Cadastro realizado.")

    app.adicionar_materia("História", 1)
    app.adicionar_materia("Física", 3)
    app.adicionar_materia("Português", 2)
    
    foco = app.obter_foco_diario()
    assert len(foco) == 3 # RF02: Limite de 3 [cite: 40]
    assert foco[0]['prioridade'] == 3 # Matemática ou Física devem vir primeiro [cite: 61]
    print("✅ Teste 2: Algoritmo de Foco (Top 3) validado.")

    tamanho_antes = len(app.materias)
    app.adicionar_materia("Matemática", 2) # Tentativa duplicada
    assert len(app.materias) == tamanho_antes
    print("✅ Teste 3: Bloqueio de duplicidade validado.")

    print("\n🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")

if __name__ == "__main__":
    testar_sistema()