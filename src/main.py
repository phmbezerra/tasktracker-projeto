tarefas = []


def cadastrar_tarefa():
    print("\n=== CADASTRAR NOVA TAREFA ===")

    while True:
        titulo = input("Título: ").strip()

        if titulo:
            break

        print("Erro: o título não pode estar vazio.")

    descricao = input("Descrição: ").strip()

    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip()

        prioridades_validas = {
            "alta": "Alta",
            "média": "Média",
            "media": "Média",
            "baixa": "Baixa"
        }

        if prioridade.lower() in prioridades_validas:
            prioridade = prioridades_validas[prioridade.lower()]
            break

        print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")

    data_limite = input("Data limite: ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n=== TAREFAS CADASTRADAS ===")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def exibir_menu():
    print("\n=== TASKTRACKER ===")
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicação")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa()

        elif opcao == "2":
            visualizar_tarefas()

        elif opcao == "3":
            print("\nEncerrando o TaskTracker...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()