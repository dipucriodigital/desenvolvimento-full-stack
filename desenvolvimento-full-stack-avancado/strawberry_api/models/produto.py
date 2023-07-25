from sqlalchemy import Column, String, Integer, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  models import Base


class Produto(Base):

    # Comentário de aula: a tabela no banco pode seguir um menemônico e 
    # ter um nome diferente do que poderia ser "mais apropriado". Aqui 
    # a tabela que vai representar o produto, se chama 'prod_catalog',
    # supondo o cenário em que o sufixo "catalog" é utilizado para 
    # indicar que é uma tabela de catálogo de produtos.
    __tablename__ = 'prod_catalog'

    # O nome de uma coluna também pode ter no banco um nome diferente
    # como é apresentado aqui no caso do Produto.id que no banco será 
    # prod_catalog.pk_prod, o sufixo pk está sendo utilizado para 
    # indicar que é uma chave primária
    id = Column("pk_prod", Integer, primary_key=True)

    # Supondo que os atributos seguintes já estejam em conformidade
    # com o menemônico adotado pela empresa, então não há necessidade
    # de fazer a definição de um "nome" de coluna diferente.
    nome = Column(String(140))  # 140 é o número máximo de caracteres
    preco = Column(Float)
    descricao = Column(String(2000))
    marca = Column(String(140))
    categoria = Column(String(140))

    # A data de inserção será o instante de inserção caso não tenha
    # um valor definido pelo usuário
    data_insercao = Column(DateTime, default=datetime.now())

    # Criando um requisito de unicidade envolvendo uma par de informações
    __table_args__ = (UniqueConstraint("nome", "categoria", name="prod_unique_id"),)

    # Estabelecendo o relacionamento entre produto e comentários
    comentarios = relationship('Comentario', lazy="joined")

    def __init__(self, nome, preco, descricao, marca, categoria,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            preco: preço atual do produto
            descricao: descrição do produto fornecida pelo fabricante
            marca: identiicação da fabricante
            categoria: categoria atribuída ao produto pela loja
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.marca = marca
        self.categoria = categoria

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Produto.
        """
        return{
            "id": self.id,
            "nome": self.nome,
            "marca": self.marca,
            "categoria": self.categoria,
            "descricao": self.descricao,
            "preco": self.preco,
            "data_insercao": self.data_insercao,
            "comentarios": [c.to_dict() for c in self.comentarios]
        }

    def __repr__(self):
        """
        Retorna uma representação do Produto em forma de texto.
        """
        return f"Product(id={self.id}, nome='{self.nome}', preco={self.preco}, marca='{self.marca}', categoria='{self.categoria}')"

