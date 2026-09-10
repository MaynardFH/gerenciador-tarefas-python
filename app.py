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
            tarefas.append({
                "descricao": tarefa,
                "concluida": False
            })
            print("Tarefa adicionada!")

        elif opcao == "3":
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
                continue

            for i, tarefa in enumerate(tarefas, 1):
                status = "Concluída" if tarefa["concluida"] else "Pendente"
                print(f"{i} - {tarefa['descricao']} [{status}]")

            numero = int(input("Digite o número da tarefa: "))

            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]["concluida"] = True
                print("Tarefa concluída!")
            else:
                print("Número inválido.")

        elif opcao == "4":
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
                continue

            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i} - {tarefa['descricao']}")

            numero = int(input("Digite o número da tarefa que deseja remover: "))

            if 1 <= numero <= len(tarefas):
                tarefas.pop(numero - 1)
                print("Tarefa removida!")
            else:
                print("Número inválido.")

        elif opcao == "5":
            print("Programa encerrado.")
            break

        else:
            print("Opção ainda não implementada.")


if __name__ == "__main__":
    main()