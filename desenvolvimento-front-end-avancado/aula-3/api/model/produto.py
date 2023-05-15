from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    descricao = Column(String(4000))
    marca = Column(String(400))
    imagem_path = Column(String(2048))
    valor = Column(Float)
    categoria = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, descricao:str, marca:str, valor:float,
                 imagem_path:str, categoria: str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            descricao: descrição do produto.
            marca: qual a fabricante do produto.
            imagem_path: caminho ou URL de acesso a imagem do produto
            valor: valor esperado para o produto
            categoria: identifica a categoria do produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.imagem_path = imagem_path
        self.categoria = categoria
        if data_insercao:
            self.data_insercao = data_insercao
