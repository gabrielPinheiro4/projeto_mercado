import os
import sys

sys.path.append(os.path.abspath('.'))
from utils.funcoes import ler_csv

PRODUTOS_CSV = ler_csv('produtos.csv')

CABECALHO = [
    'id_produto',
    'nome_produto',
    'preco',
    'quantidade_estoque'
]

HEADER_MAIN = (
    '=======================================\n'
    '============ Super Mercado ============\n'
    '=======================================\n'
)

OPCAO_HEADER = (
    'Selecione uma das opções abaixo:\n'
    '1 - Cadastrar produto\n'
    '2 - Listar produto\n'
    '3 - Comprar produto\n'
    '4 - Visualizar carrinho\n'
    '5 - Fechar pedido\n'
    '6 - Sair do sistema\n'
)
