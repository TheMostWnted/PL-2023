import re


def frequencia_processos_por_ano_regex(arquivo):
    # Abre o arquivo para leitura
    with open(arquivo, 'r') as f:
        # Cria um dicionário para armazenar as frequências de processos por ano
        frequencias = {}

        # Compila a expressão regular para extrair o ano do primeiro campo de cada linha
        regex = re.compile(r'^\d+::(\d{4})')

        # Loop pelas linhas do arquivo
        for linha in f:
            # Obtém o ano do processo a partir da linha usando regex
            match = regex.match(linha)
            if match:
                ano = match.group(1)

                # Incrementa a frequência do ano no dicionário correspondente
                if ano in frequencias:
                    frequencias[ano] += 1
                else:
                    frequencias[ano] = 1

        # Retorna o dicionário de frequências
        print (frequencias)



frequencia_processos_por_ano_regex("processos.txt");


from collections import Counter

def frequencia_nomes_e_apelidos_por_seculo():
    # Define as expressões regulares para encontrar nomes próprios e apelidos
    nome_regex = r'[A-Z][a-z]+'
    apelido_regex = r'[A-Z][a-z]+$'

    # Define um dicionário para armazenar a frequência de nomes e apelidos por século
    nomes_por_seculo = {}
    apelidos_por_seculo = {}

    with open('processos.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            # Extrai o ano da data da linha
            ano = re.search(r'^\d+::(\d{4})-', linha).group(1)

            # Extrai o nome próprio e o apelido da linha usando regex
            nome = re.search(nome_regex, linha).group()
            apelido = re.search(apelido_regex, linha).group()

            # Define o século a partir do ano
            seculo = (int(ano) - 1) // 100 + 1

            # Incrementa a contagem de nomes e apelidos por século
            nomes_por_seculo[seculo] = Counter(nomes_por_seculo.get(seculo, {})) + Counter({nome: 1})
            apelidos_por_seculo[seculo] = Counter(apelidos_por_seculo.get(seculo, {})) + Counter({apelido: 1})

    # Imprime os 5 nomes próprios mais frequentes por século
    print("Nomes próprios mais frequentes por século:")
    for seculo, nomes in nomes_por_seculo.items():
        nomes_mais_frequentes = nomes.most_common(5)
        nomes_formatados = ', '.join([f'{nome} ({frequencia})' for nome, frequencia in nomes_mais_frequentes])
        print(f"Século {seculo}: {nomes_formatados}")

    # Imprime os 5 apelidos mais frequentes por século
    print("Apelidos mais frequentes por século:")
    for seculo, apelidos in apelidos_por_seculo.items():
        apelidos_mais_frequentes = apelidos.most_common(5)
        apelidos_formatados = ', '.join([f'{apelido} ({frequencia})' for apelido, frequencia in apelidos_mais_frequentes])
        print(f"Século {seculo}: {apelidos_formatados}")



#frequencia_nomes_e_apelidos_por_seculo()


def calcular_frequencia_relacoes(arquivo):
    # Abre o arquivo e lê as linhas
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    # Define as expressões regulares para cada tipo de relação
    regexes = {
        'irmao': r'irma[oã] de',
        'sobrinho': r'sobrinh[oa] de',
        'tio': r'tio[a] de',
        'primo': r'primo[a] de',
        'avo': r'av[oô] de',
        'neto': r'net[oa] de',
    }

    # Inicializa um dicionário para contar as frequências
    frequencias = {rel: 0 for rel in regexes.keys()}

    # Itera pelas linhas do arquivo e procura por padrões de relação
    for linha in linhas:
        for rel, regex in regexes.items():
            if re.search(regex, linha):
                frequencias[rel] += 1

    # Retorna as frequências ordenadas por ordem decrescente
    print( {k: v for k, v in sorted(frequencias.items(), key=lambda item: item[1], reverse=True)})



calcular_frequencia_relacoes("processos.txt")


with open("processos.txt", "r") as f:
    linhas = f.readlines()

regex_irmao = r"irma[oã] de"
regex_sobrinho = r"sobrinh[oa] de"
regex_tio = r"tio[a] de"
regex_primo = r"primo[a] de"
regex_avo = r"av[oô] de"
regex_neto = r"net[oa] de"

for linha in linhas:
    if re.search(regex_irmao, linha):
        print("Padrão de irmão encontrado:", linha)
    if re.search(regex_sobrinho, linha):
        print("Padrão de sobrinho encontrado:", linha)
    if re.search(regex_tio, linha):
        print("Padrão de tio encontrado:", linha)
    if re.search(regex_primo, linha):
        print("Padrão de primo encontrado:", linha)
    if re.search(regex_avo, linha):
        print("Padrão de avô encontrado:", linha)
    if re.search(regex_neto, linha):
        print("Padrão de neto encontrado:", linha)


# Abre o arquivo e lê as linhas
with open('processos.txt', 'r') as f:
    linhas = f.readlines()

# Inicializa uma lista para armazenar os registros processados
registros = []

# Define a expressão regular para cada campo do registro
id_regex = r'^(\d+)::'
data_regex = r'::(\d{4}-\d{2}-\d{2})::'
autor_regex = r'::([A-Za-z ]+)::'
reu_regex = r'::([A-Za-z ]+)::'
relacao_regex = r'::([A-Za-z ]*)::'

# Itera pelas linhas do arquivo e processa os registros
for linha in linhas[:20]:
    registro = {}

    # Procura por padrões de expressões regulares e armazena os campos correspondentes no registro
    id_match = re.search(id_regex, linha)
    if id_match:
        registro['id'] = int(id_match.group(1))

    data_match = re.search(data_regex, linha)
    if data_match:
        registro['data'] = data_match.group(1)

    autor_match = re.search(autor_regex, linha)
    if autor_match:
        registro['autor'] = autor_match.group(1)

    reu_match = re.search(reu_regex, linha)
    if reu_match:
        registro['reu'] = reu_match.group(1)

    relacao_match = re.search(relacao_regex, linha)
    if relacao_match:
        registro['relacao'] = relacao_match.group(1)

    # Adiciona o registro à lista de registros
    registros.append(registro)

# Escreve os registros no arquivo de saída no formato JSON
with open('registros.json', 'w') as f:
    json.dump(registros, f, indent=4)

