from csv import (
    DictReader,
    DictWriter
)
from unicodedata import normalize

def ler_csv(nome_arquivo) -> list:
    with open (nome_arquivo) as arquivo:
        csv = DictReader(arquivo)
        
        return [linha for linha in csv]
    

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

def matricula() -> int:
    ids = []
    for linha in ler_csv('produtos.csv'):
        ids.append(int(linha.get('id_produto')))

    nova_matricula = max(ids)
    nova_matricula += 1

    return nova_matricula


def remover_acentos(item) -> str:
    sem_acento = normalize('NFD', item.lower()).encode('ascii', 'ignore')
    return sem_acento.decode('utf-8')