import os
import sys

# Pega o caminho do diretório pai
sys.path.append(os.path.abspath('.'))
from utils.funcoes import ler_csv

# Variável para ler arquivo produtos.csv
PRODUTOS_CSV = ler_csv('produtos.csv')

# Cabeçalho do arquivo produtos.csv
CABECALHO = [
    'id_produto',
    'nome_produto',
    'preco',
    'quantidade_estoque'
]
