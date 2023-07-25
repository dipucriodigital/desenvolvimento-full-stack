from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from typing import Union

from  models import Base, Produto


class Comentario(Base):

    # Comentário de aula: a tabela no banco pode seguir um menemônico e 
    # ter um nome diferente do que poderia ser "mais apropriado". Aqui 
    # a tabela que vai representar o comentãrio vinculado ao produto, 
    # que se chama 'prod_comentario'.
    __tablename__ = 'prod_comentario'

    # Supondo que os atributos seguintes já estejam em conformidade
    # com o menemônico adotado pela empresa, então não há necessidade
    # de fazer a definição de um "nome" de coluna diferente.
    id = Column(Integer, primary_key=True)
    texto = Column(String(4000))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o comentário e um produto.
    # Aqui está sendo definido a coluna 'produto' que vai guardar
    # a referencia ao produto, a chave estrangeira que relaciona
    # um produto ao comentário.
    produto_id = Column(Integer, ForeignKey(Produto.id), nullable=False)
    produto = relationship(Produto, uselist=False, lazy="joined", viewonly=True)

    def __init__(self, texto:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Comentário

        Arguments:
            texto: o texto de um comentário.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.texto = texto
        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):
        """
        Retorna a representação em dicionário do Objeto Comentario.
        """
        return{
            "id": self.id,
            "texto": self.texto,
            "data_insercao": self.data_insercao,
            "produto_id": self.produto.id
        }

    def __repr__(self):
        """
        Retorna uma representação do Comentario em forma de texto.
        """
        return f"Comentario(id={self.id}, texto='{self.texto}')"
