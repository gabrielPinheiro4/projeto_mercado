import os
import sys

sys.path.append(os.path.abspath(''))

from constants.const import (
    PRODUTOS_CSV,
    CABECALHO
)
from utils.funcoes import (
    matricula,
    escrita_csv
)


class Produto:
    def __init__(self, nome, preco, quantidade) -> None:
        self.nome: str = nome
        self.preco: float = preco
        self.quantidade: int = quantidade
        self.id: int = matricula()

    def cadastrar_produto(self):
        escrita_csv(
            'produtos.csv',
            CABECALHO,
            self.id,
            self.nome,
            self.preco,
            self.quantidade
        )

        return 'Produto cadastrado com sucesso'

    def listar_produtos(self) -> list:
        return PRODUTOS_CSV
    

produto1 = Produto('Sucrilhos', 25.99, 10)
produto2 = Produto('Fanta', 50.99, 20)
# print(produto1.cadastrar_produto())
