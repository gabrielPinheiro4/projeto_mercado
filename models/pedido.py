import os
import sys

sys.path.append(os.path.abspath('.'))

from produto import Produto
from utils.funcoes import (
    remover_acentos,
    fechar_carrinho_csv
)

from constants.const import (
    PRODUTOS_CSV,
    CABECALHO
)

class Pedido(Produto):
    def __init__(self, produtos: list) -> None:
        self.produto: list = produtos
        self.carrinho: list = []

    def comprar_produto(self):
        for produto in self.produto:
            for produto_csv in PRODUTOS_CSV:
                if remover_acentos(produto) == remover_acentos(produto_csv.get('nome_produto')):
                    self.carrinho.append(produto_csv)
        
        return 'Produto adicionado ao carrinho'
    
    def visualizar_carrinho(self):
        return self.carrinho
    
    def fechar_pedido(self):
        lista = []
        if len(self.carrinho) > 0:
            for produto in self.carrinho:
                for produto_csv in PRODUTOS_CSV:
                    if produto == produto_csv:
                        quantidade = int(produto_csv.get('quantidade_estoque'))
                        quantidade -= 1
                        produto_csv.update({'quantidade_estoque': quantidade})
                        print(produto_csv)
                    lista.append(produto_csv)
        
            fechar_carrinho_csv('produtos.csv', CABECALHO, lista)

            return 'Pedido concluido'


pedido1 = Pedido(['sabonete', 'biscoitos'])
print(pedido1.comprar_produto())
pedido1.fechar_pedido()
