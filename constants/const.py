import os
import sys

sys.path.append(os.path.abspath(''))
from utils.funcoes import ler_csv

PRODUTOS_CSV = ler_csv('produtos.csv')

CABECALHO = [
    'id_produto',
    'nome_produto',
    'preco',
    'quantidade_estoque'
]