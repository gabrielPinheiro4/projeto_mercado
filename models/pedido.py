import os
import sys

# Pega o caminho do diretório pai
sys.path.append(os.path.abspath('.'))

from utils.funcoes import (
    remover_acentos,
    fechar_carrinho_csv
)

from constants.const import (
    PRODUTOS_CSV,
    CABECALHO
)

class Pedido:
    def __init__(self, produtos: list) -> None:
        self.produtos: list = produtos
        self.carrinho: list = []

    def comprar_produto(self) -> str:
        for produto in self.produtos:
            for produto_csv in PRODUTOS_CSV:

                # Se o produto passado pelo usuário for igual a um produto no 
                # arquivo produtos.csv, adiciona o produto no carrinho
                if remover_acentos(produto) == remover_acentos(produto_csv.get('nome_produto')):
                    self.carrinho.append(produto_csv)
        
        return 'Produto adicionado ao carrinho'
    
    # Mostra o carrinho
    def visualizar_carrinho(self) -> list:
        return self.carrinho
    
    # Calcula qual foi o preço total dos produtos
    def verificar_preco_total(self) -> float:
        valor_total = []
        for produto in self.carrinho:
            
            # Converte os valores dos produtos para float e adiciona na lista
            valor_total.append(float(produto.get('preco')))
         
        # Retorna a soma dos valores
        return sum(valor_total)
    
    def fechar_pedido(self) -> str:
        
        # Se o carrinho não estiver vazio
        if len(self.carrinho) > 0 or self.carrinho != []:
            lista = []

            # Printa o valor total dos produtos
            print(f'Valor Total: {self.verificar_preco_total()}')
            
            # Valor pago pelo cliente
            valor_pagar = float( input('Digite o valor pago: '))

            # Cálculo do troco
            troco = abs(self.verificar_preco_total() - valor_pagar)

            # Faz um for no carrinho
            for produto in self.carrinho:
                
                # Se o valor pago pelo cliente for menor que o valor do produto
                if valor_pagar < self.verificar_preco_total():
                    return 'Valor insuficiente'
                
                # Faz um for no arquivo produtos.csv
                for produto_csv in PRODUTOS_CSV:

                    # Se um produto no carrinho for igual a um produto em
                    # produtos.csv
                    if produto == produto_csv:

                        # Converte a quantidade do produto para int
                        quantidade = int(produto_csv.get('quantidade_estoque'))

                        # Diminui a quantidade
                        quantidade -= 1

                        # Atualiza a quantidade
                        produto_csv.update({'quantidade_estoque': quantidade})

                    # Joga os dados atualizados numa lista
                    lista.append(produto_csv)

            # Sobreescreve o arquivo produtos.csv com a lista atualizada
            fechar_carrinho_csv('produtos.csv', CABECALHO, lista)

            # Limpa o carrinho
            self.carrinho.clear()

            return (
                'Pedido concluido \n'
                'O carrinho foi zerado \n'
                f'Troco: {troco}'
            )
        
        return 'Seu carrinho está vazio'
