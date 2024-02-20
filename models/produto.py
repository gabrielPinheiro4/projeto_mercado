import os
import sys
from json import dumps

# Pega o caminho do diretório pai
sys.path.append(os.path.abspath('.'))

from constants.const import (
    PRODUTOS_CSV,
    CABECALHO
)
from utils.funcoes import (
    matricula,
    cadastrar_produto_csv
)


class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int) -> None:
        self.nome: str = nome
        self.preco: float = preco
        self.quantidade: int = quantidade
        self.id: int = matricula()

    # Escreve a instância do objeto no arquivo produtos.csv
    def cadastrar_produto(self):
        cadastrar_produto_csv(
            'produtos.csv',
            CABECALHO,
            self.id,
            self.nome,
            self.preco,
            self.quantidade
        )

        return 'Produto cadastrado com sucesso'

    # Lista todos os produtos do arquivo prosutos.csv indentado
    def listar_produtos(self) -> list:
        return dumps(PRODUTOS_CSV, indent=4)
