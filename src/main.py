tarefas = []


def cadastrar_tarefa():
    print("\n=== CADASTRAR NOVA TAREFA ===")
    print("Funcionalidade de cadastro será implementada em seguida.")


def visualizar_tarefas():
    print("\n=== TAREFAS CADASTRADAS ===")
    print("Funcionalidade de visualização será implementada em seguida.")


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