opcao = -1
manifestacoes = []
print("BEM VINDOS A OUVIDORIA DA UNIVERSIDADE XYZ")
print()

while opcao != 6:
    print("1 Listar, 2 Adicionar, 3 Quantidade, 4 Pesquisar, 5 Excluir, 6 Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        if len(manifestacoes) > 0:
            print("Lista de reclamações")
            for i in range(len(manifestacoes)):
                print(str(i + 1) + ")", manifestacoes[i])
        else:
            print("Não existem reclamações disponíveis")

    elif opcao == 2:
        novaManifestacao = input("Digite sua reclamação: ")
        manifestacoes.append(novaManifestacao)
        print("Reclamação adicionada com sucesso!")

    elif opcao == 3:
        print("Temos", len(manifestacoes), "reclamações cadastradas no sistema")

    elif opcao == 4:
        codigo = int(input("Digite o código da reclamação: "))

        if codigo > 0 and codigo <= len(manifestacoes):
            print("A reclamação pesquisada foi:", manifestacoes[codigo - 1])
        else:
            print("Código informado inválido!")

    elif opcao == 5:
        codigo = int(input("Digite o código da reclamação: "))

        if codigo > 0 and codigo <= len(manifestacoes):
            manifestacoes.pop(codigo - 1)
            print("Reclamação removida com sucesso:")

        else:
            print("Reclamação não encontrada")


    elif opcao != 6:
        print("Opção Inválida!")

print("Obrigado por usar a ouvidoria!")