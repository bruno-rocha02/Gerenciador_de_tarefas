import json
from datetime import datetime

# Variáveis globais (já existentes)
tarefas = []
arquivo_tarefas = "tarefas.json"

# =============================================
# FUNÇÕES EXISTENTES (NÃO MODIFICAR)
# =============================================

def carregar_tarefas():
    """Função existente - não modificar"""
    global tarefas
    try:
        with open(arquivo_tarefas, 'r', encoding='utf-8') as f:
            tarefas = json.load(f)
        print(f"📂 {len(tarefas)} tarefas carregadas!")
    except FileNotFoundError:
        print("📝 Arquivo não encontrado. Começando com lista vazia.")
        tarefas = []
    except Exception as e:
        print(f"❌ Erro ao carregar tarefas: {e}")
        tarefas = []

def salvar_tarefas():
    """Função existente - não modificar"""
    try:
        with open(arquivo_tarefas, 'w', encoding='utf-8') as f:
            json.dump(tarefas, f, ensure_ascii=False, indent=2)
        print("💾 Tarefas salvas com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar tarefas: {e}")

def criar_tarefa():
    """Função existente - não modificar"""
    try:
        print("\n" + "="*40)
        print("CRIAR NOVA TAREFA")
        print("="*40)
        
        titulo = input("Título da tarefa: ").strip()
        if not titulo:
            print("❌ O título é obrigatório!")
            return None
        
        descricao = input("Descrição: ").strip()
        if not descricao:
            descricao = "Sem descrição"
        
        while True:
            data_str = input("Data de vencimento (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(data_str, "%Y-%m-%d")
                break
            except ValueError:
                print("❌ Formato de data inválido! Use YYYY-MM-DD")
        
        nova_tarefa = {
            "id": len(tarefas) + 1,
            "titulo": titulo,
            "descricao": descricao,
            "data_vencimento": data_str,
            "concluida": False
        }
        
        tarefas.append(nova_tarefa)
        print(f"✅ Tarefa '{titulo}' adicionada com sucesso! (ID: {nova_tarefa['id']})")
        salvar_tarefas()
        return nova_tarefa
        
    except Exception as e:
        print(f"❌ Erro ao criar tarefa: {e}")
        return None

# =============================================
# NOVAS FUNÇÕES (ADICIONAR ABAIXO)
# =============================================

def listar_tarefas():
    """
    Lista todas as tarefas com opção de filtro por status
    """
    print("\n" + "="*60)
    print("LISTA DE TAREFAS")
    print("="*60)
    
    if not tarefas:
        print("📭 Nenhuma tarefa encontrada!")
        return
    
    # Opção de filtro
    filtro = input("Filtrar por (1-Todas, 2-Pendentes, 3-Concluídas): ").strip()
    
    for tarefa in tarefas:
        # Aplicar filtro
        if filtro == "2" and tarefa["concluida"]:
            continue
        if filtro == "3" and not tarefa["concluida"]:
            continue
        
        status = "✅" if tarefa["concluida"] else "⏳"
        print(f"{status} ID: {tarefa['id']} | {tarefa['titulo']}")
        print(f"   Descrição: {tarefa['descricao']}")
        print(f"   Vencimento: {tarefa['data_vencimento']}")
        print("-" * 40)

def concluir_tarefa():
    """
    Marca uma tarefa como concluída
    """
    listar_tarefas()
    
    if not tarefas:
        return
    
    try:
        id_tarefa = int(input("\nID da tarefa a concluir: ").strip())
        
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                if tarefa["concluida"]:
                    print("ℹ️  Esta tarefa já estava concluída!")
                else:
                    tarefa["concluida"] = True
                    print(f"✅ Tarefa '{tarefa['titulo']}' concluída!")
                    salvar_tarefas()
                return
        
        print("❌ Tarefa não encontrada!")
        
    except ValueError:
        print("❌ ID deve ser um número!")
    except Exception as e:
        print(f"❌ Erro: {e}")

def remover_tarefa():
    """
    Remove uma tarefa da lista
    """
    listar_tarefas()
    
    if not tarefas:
        return
    
    try:
        id_tarefa = int(input("\nID da tarefa a remover: ").strip())
        
        for i, tarefa in enumerate(tarefas):
            if tarefa["id"] == id_tarefa:
                confirmacao = input(f"Tem certeza que deseja remover '{tarefa['titulo']}'? (s/n): ").strip().lower()
                if confirmacao == 's':
                    tarefa_removida = tarefas.pop(i)
                    print(f"🗑️  Tarefa '{tarefa_removida['titulo']}' removida!")
                    salvar_tarefas()
                return
        
        print("❌ Tarefa não encontrada!")
        
    except ValueError:
        print("❌ ID deve ser um número!")
    except Exception as e:
        print(f"❌ Erro: {e}")

def menu_principal():
    """
    Menu interativo principal
    """
    while True:
        print("\n" + "="*40)
        print("🎯 GERENCIADOR DE TAREFAS")
        print("="*40)
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("👋 Saindo do programa... Até logo!")
            break
        else:
            print("❌ Opção inválida! Escolha de 1 a 5.")

# =============================================
# EXECUÇÃO PRINCIPAL
# =============================================

if __name__ == "__main__":
    carregar_tarefas()
    menu_principal()