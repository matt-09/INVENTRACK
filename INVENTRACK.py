ativos = []

def menu():
    print("\n===== INVENTRACK =====")
    print("1 - Cadastrar ativo")
    print("2 - Listar ativos")
    print("3 - Transferir ativo")
    print("4 - Remover ativo")
    print("5 - Consultar patrimônio")
    print("6 - Sair")

    opcao = input("\nQual opção desejada? ")

    global ativos

    match opcao:

        case "1":

            patrimonio = input("Número do patrimônio: ")

            for item in ativos:
                if item[0] == patrimonio:
                    print("Patrimônio já cadastrado!")
                    break

            else:
                descricao = input("Descrição do ativo: ")
                responsavel = input("Responsável: ")
                setor = input("Setor: ")

                ativos.append([
                    patrimonio,
                    descricao,
                    responsavel,
                    setor
                ])

                print("Ativo cadastrado com sucesso!")

        case "2":

            if not ativos:
                print("Nenhum ativo cadastrado.")

            else:

                print("\n===== ATIVOS CADASTRADOS =====")

                for item in ativos:

                    print(
                        f"Patrimônio: {item[0]} | "
                        f"Descrição: {item[1]} | "
                        f"Responsável: {item[2]} | "
                        f"Setor: {item[3]}"
                    )

        case "3":

            patrimonio = input(
                "Qual patrimônio deseja transferir? "
            )

            for item in ativos:

                if item[0] == patrimonio:

                    novo_resp = input(
                        "Novo responsável: "
                    )

                    item[2] = novo_resp

                    
                    Novo_Setor = input(
                         "Setor:"   
                    )
                    item[3] = Novo_Setor
                    print(
                        "Patrimonio transferido com sucesso!"
                    )
                    break
                    
            else:
                print("Patrimônio não encontrado.")

        case "4":

            patrimonio = input(
                "Qual patrimônio deseja remover? "
            )

            for item in ativos:

                if item[0] == patrimonio:

                    ativos.remove(item)

                    print(
                        "Ativo removido com sucesso!"
                    )

                    break

            else:
                print("Patrimônio não encontrado.")

        case "5":

            patrimonio = input(
                "Informe o patrimônio: "
            )

            for item in ativos:

                if item[0] == patrimonio:

                    print("\n===== DADOS DO ATIVO =====")

                    print(
                        f"Patrimônio: {item[0]}"
                    )

                    print(
                        f"Descrição: {item[1]}"
                    )

                    print(
                        f"Responsável: {item[2]}"
                    )

                    print(
                        f"Setor: {item[3]}"
                    )

                    break

            else:
                print("Patrimônio não encontrado.")

        case "6":

            print("Programa encerrado!")
            exit()

        case _:

            print("Opção inválida!")

if __name__ == "__main__":

    while True:

        menu()