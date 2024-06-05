from operacoesbd import *
opcao = -1
con = criarConexao ('127.0.0.1','root','123Yahoo*','ouvidoria')
print("BEM VINDOS A OUVIDORIA DA UNIVERSIDADE XYZ")
print()

while opcao != 7:
    print()
    print("Opções \n-1 Listar manifestações \n-2 Listar manifestações por tipo \n-3 Adicionar nova manifestação \n-4 Quantidade de manifestações \n-5 Pesquisa por manifestação \n-6 Excluir manifestação \n-7 Sair")
    print()
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        consultaListar = 'select * from manifestacoes'
        manifestacoes = listarBancoDados(con, consultaListar)

        if len(manifestacoes) == 0:
            print("-Não existem manifestações a serem exibidas!")
        else:
            print("-Lista de manifestações:")
            for item in manifestacoes:
                print('\n Código:', item[0],'\n Manifestação:',item[1],'\n Tipo:', item[2])

    elif opcao == 2:
        tipoManifestacao = int(input("Digite o tipo da manifestação (1) Reclamação 2) Elogio 3) Sugestão 4) Denúncia 5) Informação): "))

        if tipoManifestacao <= 0 and tipoManifestacao > 5:
            print("Opção Invalida")
        else:
            if tipoManifestacao == 1:
                manifestacao = 'Reclamação'
            elif tipoManifestacao == 2:
                manifestacao = 'Elogio'
            elif tipoManifestacao == 3:
                manifestacao = 'Sugestão'
            elif tipoManifestacao == 4:
                manifestacao = 'Denúncia'
            elif tipoManifestacao == 5:
                manifestacao = 'Informação'

        consultaListar = "select * from manifestacoes where tipo = '" + manifestacao + "'"
        manifestacoes = listarBancoDados(con, consultaListar)

        if len(manifestacoes) == 0:
            print("Não existem manifestações para serem exibidas pelo tipo informado!")
        else:
            print(f"Lista de manifestações do tipo {tipoManifestacao}:")
            for item in manifestacoes:
                print('\nCódigo:', item[0], '\nManifestação:', item[1], '\nTipo:', item[2])

    elif opcao == 3:
        novaManifestacao = input("Digite sua manifestação: ")
        tipoManifestacao = int(input("Digite o tipo da manifestação (1) Reclamação 2) Elogio 3) Sugestão 4) Denúncia 5) Informação): "))

        if tipoManifestacao <= 0 and tipoManifestacao > 5:
            print("Opção Invalida")
        else:
            if tipoManifestacao == 1:
                manifestacao = 'Reclamação'
            elif tipoManifestacao == 2:
                manifestacao = 'Elogio'
            elif tipoManifestacao == 3:
                manifestacao = 'Sugestão'
            elif tipoManifestacao == 4:
                manifestacao = 'Denúncia'
            elif tipoManifestacao == 5:
                manifestacao = 'Informação'

        consultaInsert = 'insert into manifestacoes (manifestação, tipo) values(%s,%s)'
        dados = [novaManifestacao, manifestacao]
        insertNoBancoDados(con,consultaInsert,dados)
        print("Manifestação adicionada com sucesso!")

    elif opcao == 4:
        consultaListar = "SELECT count(*) from manifestacoes"
        manifestacoes = listarBancoDados(con, consultaListar)
        totalManifestacoes = manifestacoes [0][0]
        print("A ouvidoria possui", totalManifestacoes,"manifestações." )

    elif opcao == 5:
        codigoPesquisa = int(input("Digite o código da manifestação: "))
        consultaListar = 'select * from manifestacoes where codigo =' + str(codigoPesquisa)
        manifestacoes = listarBancoDados(con, consultaListar)

        if len(manifestacoes) == 0:
            print("Não existem manifestações para o código informado!")
        else:
            print("Manifestação pesquisada:")
            for item in manifestacoes:
                print('\n Código:', item[0], '\n Manifestação:', item[1], '\n Tipo:', item[2])

    elif opcao == 6:
        codigoApagar = input("Digite o código da manifestação: ")
        consultaListar = "DELETE FROM manifestacoes WHERE codigo = %s"
        dados = [codigoApagar]
        manifestacoes = excluirBancoDados(con,consultaListar, dados)

        if manifestacoes:
            print("A manifestação foi excluída com sucesso.")
        else:
            print("A manifestação não existe ou já foi excluída.")

    elif opcao != 7:
        print("Opção Inválida!")

encerrarBancoDados(con)
print("Obrigado por usar a ouvidoria!")
