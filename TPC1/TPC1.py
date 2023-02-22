# TPC1

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(',')]
        for line in lines[1:]:
            values = [x.strip() for x in line.split(',')]
            record = {header[i]: values[i] for i in range(len(header))}
            data.append(record)
    print( data )

read_csv_file('myheart.csv')

#Esta função lê um arquivo CSV, linha por linha, e cria um dicionário para cada registo.
# Em seguida, os dicionários são armazenados numa lista que é retornada como resultado da função.

def distribuicao_por_sexo(filename):
    # Inicializa contadores
    contadores = {"M": 0, "F": 0}

    with open(filename, "r") as file:
        # Ignora a primeira linha (cabeçalho)
        next(file)

        # Percorre as linhas do arquivo
        for line in file:
            # Divide a linha em colunas
            colunas = line.strip().split(",")

            # Pega no valor do sexo (segunda coluna)
            sexo = colunas[1]

            # Incrementa o contador apropriado
            contadores[sexo] += 1

    # Retorna o resultado como um dicionário
    print(contadores)
    return contadores

distribuicao_por_sexo("myheart.csv")


# função que devolve a maior idade existente no csv para definir o último escalão etário

def maior_idade(filename):
    # Inicializa a maior idade com um valor pequeno
    maior_idade = -1

    with open(filename, "r") as file:
        # Ignora a primeira linha (cabeçalho)
        next(file)

        # Percorre as linhas do arquivo
        for line in file:
            # Divide a linha em colunas
            colunas = line.strip().split(",")

            # Pega o valor da idade (primeira coluna)
            idade = int(colunas[0])

            # Verifica se a idade é maior que a maior idade atual
            if idade > maior_idade:
                maior_idade = idade

    # Retorna a maior idade encontrada
    print(maior_idade)


maior_idade("myheart.csv")


def distribuicao_doencas_por_idade(file_name):
    faixas_etarias = ["[30-34]", "[35-39]", "[40-44]", "[45-49]", "[50-54]", "[55-59]", "[60-64]", "[65-69]", "[70-74]",
                      "[75-77]"]
    distribuicao = {}
    for faixa in faixas_etarias:
        distribuicao[faixa] = 0

    with open(file_name, 'r') as file:
        linhas = file.readlines()
        # Ignorar a primeira linha, que contém o cabeçalho
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            idade = int(valores[0])
            doenca = valores[-1]
            # Verificar em qual faixa etária a idade se enquadra
            if idade < 30:
                continue
            elif idade > 77:
                faixa_etaria = "[75+]"
            else:
                indice_faixa = (idade - 30) // 5
                faixa_etaria = faixas_etarias[indice_faixa]
            distribuicao[faixa_etaria] += 1 if doenca == "1" else 0

    print(distribuicao)
    return distribuicao


distribuicao_doencas_por_idade("myheart.csv")



def distribuicao_doencas_por_colesterol(filename):
    # inicializar o dicionário que irá conter a distribuição de doenças por níveis de colesterol
    distribuicao = {}

    # criar as chaves do dicionário para cada intervalo de colesterol de 10 em 10
    for i in range(0, 610, 10):
        chave = f"{i}-{i+9}"
        distribuicao[chave] = 0

    # abrir o arquivo e percorrer as linhas
    with open(filename, 'r') as f:
        # ignorar a primeira linha com o cabeçalho
        next(f)

        # percorrer as linhas do arquivo
        for line in f:
            # remover os espaços em branco e quebrar a linha em uma lista de valores
            valores = line.strip().split(',')
            # pegar o valor de colesterol e convertê-lo em inteiro
            colesterol = int(valores[3])

            # incrementar o contador para o intervalo de colesterol correspondente
            for chave in distribuicao:
                inicio, fim = chave.split('-')
                if int(inicio) <= colesterol <= int(fim):
                    distribuicao[chave] += 1
                    break

    # retornar a distribuição de doenças por níveis de colesterol
    print(distribuicao)
    return distribuicao

distribuicao_doencas_por_colesterol("myheart.csv")



def tabela_distribuicao_por_idade(distribuicao):
    # Cria uma lista com as idades e outra com os números de doentes correspondentes
    idades = sorted(list(distribuicao.keys()))
    doentes = [distribuicao[idade] for idade in idades]

    # Encontra o comprimento da maior idade e do maior número de doentes
    tam_idade = max(len(str(idade)) for idade in idades)
    tam_doentes = max(len(str(doente)) for doente in doentes)

    # Imprime a tabela
    print("Distribuição de Doenças por Idades")
    print(f"{'Idade':<{tam_idade}} | {'Doentes':<{tam_doentes}}")
    print("-" * (tam_idade + tam_doentes + 3))
    for idade, doente in zip(idades, doentes):
        print(f"{idade:<{tam_idade}} | {doente:<{tam_doentes}}")


distribuicao = distribuicao_doencas_por_idade('myheart.csv')
tabela_distribuicao_por_idade(distribuicao)


def tabela_distribuicao_doencas_por_colesterol(distribuicao):
    print("Distribuição de Doenças por Níveis de Colesterol")
    print("-----------------------------------------------")
    print("  Intervalo de Colesterol   |   Número de Doentes ")
    print("----------------------------|-------------------")

    for intervalo, num_doentes in distribuicao.items():
        print(f"    {intervalo:>15}      |        {num_doentes:>6}")

dist_colesterol = distribuicao_doencas_por_colesterol('myheart.csv')
tabela_distribuicao_doencas_por_colesterol(dist_colesterol)


def tabela_distribuicao_por_sexo(filename):
    distribuicao = distribuicao_por_sexo(filename)

    table = "+-------+-----------+\n"
    table += "| Sexo  | Doentes   |\n"
    table += "+-------+-----------+\n"
    table += "| Homem | {:<10}|\n".format(str(distribuicao['M']))
    table += "| Mulher| {:<10}|\n".format(str(distribuicao['F']))
    table += "+-------+-----------+\n"

    print(table)


tabela_distribuicao_por_sexo('myheart.csv')