from csv import (
    DictReader,
    DictWriter
)

def ler_csv(nome_arquivo) -> list:
    with open (nome_arquivo) as arquivo:
        csv = DictReader(arquivo)
        
        return [linha for linha in csv]
    

def escrita_csv(nome_arquivo, cabecalho, id, nome, preco, quantidade):
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
    

def matricula() -> int:
    ids = []
    for linha in ler_csv('produtos.csv'):
        ids.append(int(linha.get('id_produto')))

    nova_matricula = max(ids)
    nova_matricula += 1

    return nova_matricula
