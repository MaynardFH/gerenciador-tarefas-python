tarefas = []


def main():
    print("================================")
    print("     GERENCIADOR DE TAREFAS")
    print("================================")

    while True:
        print("\n1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nTarefas:")
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i} - {tarefa}")

        elif opcao == "2":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada!")

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção ainda não implementada.")


if __name__ == "__main__":
    main()