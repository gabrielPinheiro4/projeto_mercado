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

    def comprar_produto(self) -> str:
        for produto in self.produto:
            for produto_csv in PRODUTOS_CSV:
                if remover_acentos(produto) == remover_acentos(produto_csv.get('nome_produto')):
                    self.carrinho.append(produto_csv)
        
        return 'Produto adicionado ao carrinho'
    
    def visualizar_carrinho(self) -> list:
        return self.carrinho
    
    def verificar_preco_total(self) -> float:
        valor_total = []
        for produto in self.carrinho:
            valor_total.append(float(produto.get('preco')))
        
        return sum(valor_total)
    
    def fechar_pedido(self) -> str:
        
        if len(self.carrinho) > 0 or self.carrinho != []:
            lista = []
        
            print(f'Valor Total: {self.verificar_preco_total()}')

            valor_pagar = float( input('Digite o valor pago: '))
            troco = abs(self.verificar_preco_total() - valor_pagar)

            for produto in self.carrinho:
                
                if valor_pagar < self.verificar_preco_total():
                    return 'Valor insuficiente'
                
                for produto_csv in PRODUTOS_CSV:
                    if produto == produto_csv:
                        quantidade = int(produto_csv.get('quantidade_estoque'))
                        quantidade -= 1
                        produto_csv.update({'quantidade_estoque': quantidade})

                    lista.append(produto_csv)

            fechar_carrinho_csv('produtos.csv', CABECALHO, lista)
            self.carrinho.clear()

            return (
                'Pedido concluido \n'
                'O carrinho foi zerado \n'
                f'Troco: {troco}'
            )
        return 'Seu carrinho está vazio'


pedido1 = Pedido(['sabonete'])
print(pedido1.comprar_produto())
print(pedido1.fechar_pedido())
# pedido1.verificar_preco_total()
