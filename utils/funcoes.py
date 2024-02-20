from csv import (
    DictReader,
    DictWriter
)
from unicodedata import normalize

# Função que retorna cada linha do arquivo produtos.csv
def ler_csv(nome_arquivo) -> list:
    with open (nome_arquivo) as arquivo:
        csv = DictReader(arquivo)
        
        return [linha for linha in csv]
    

# Adiciona um novo produto no arquivo produtos.csv
def cadastrar_produto_csv(nome_arquivo, cabecalho, id, nome, preco, quantidade):
    with open(nome_arquivo, 'a') as arquivo:
        csv = DictWriter(arquivo, fieldnames=cabecalho)
        csv.writerow(
            {
                'id_produto': id,
                'nome_produto': nome,
                'preco': preco,
                'quantidade_estoque': quantidade
            }
        )
    

# Função para escrever no arquivo produtos.csv
def fechar_carrinho_csv(nome_arquivo, cabecalho, lista):
    with open(nome_arquivo, 'w') as arquivo:
        csv = DictWriter(arquivo, fieldnames=cabecalho)
        csv.writeheader()
        for linha in lista:
            csv.writerow(
                {
                    'id_produto': linha.get('id_produto'),
                    'nome_produto': linha.get('nome_produto'),
                    'preco': linha.get('preco'),
                    'quantidade_estoque': linha.get('quantidade_estoque')
                }
            )


# Função para criar a matricula do produto
def matricula() -> int:
    ids = []

    # Faz um for no arquivo produtos.csv
    for linha in ler_csv('produtos.csv'):

        # Adiciona na lista e converte para int todos os ids dos produtos
        ids.append(int(linha.get('id_produto')))

    # Pega o valor do ultimo id
    nova_matricula = max(ids)

    # Adiciona mais um ao id
    nova_matricula += 1

    # Retorna o id
    return nova_matricula


# Função para remover acentos de strings
def remover_acentos(item) -> str:
    sem_acento = normalize('NFD', item.lower()).encode('ascii', 'ignore')
    
    return sem_acento.decode('utf-8')