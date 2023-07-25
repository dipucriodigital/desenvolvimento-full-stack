from strawberry.fastapi import GraphQLRouter
from typing import Optional, List
from fastapi import FastAPI
from typing import List
import strawberry

from sqlalchemy import select


import models


@strawberry.type
class Comentario:
    id: strawberry.ID
    texto: str

    @classmethod
    def marshal(cls, model: models.Comentario) -> "Comentario":
        return cls(id=strawberry.ID(str(model.id)), texto=model.texto)


@strawberry.type
class Produto:
    id: strawberry.ID
    nome: str
    preco: float
    descricao: str
    marca: str
    categoria: str
    # comentarios: List[Comentario] = None

    @classmethod
    def marshal(cls, model: models.Produto) -> "Produto":
        return cls(
            id=strawberry.ID(str(model.id)),
            nome=model.nome,
            preco=model.preco,
            descricao=model.descricao,
            marca=model.marca,
            categoria=model.categoria
            # comentarios= [Comentario.marshal(c) for c in model.comentarios] if model.comentarios else []
        )

@strawberry.input
class ProdutoQueryInput:
    termo: Optional[str] = strawberry.UNSET

@strawberry.type
class ProdutoExists:
    message: str = "Produto de mesmo nome e marca já inserido na base"

@strawberry.type
class ProdutoNotFound:
    message: str = "Não foi possível encontrar o produto"


AddProdutoResponse = strawberry.union("AddProdutoResponse", (Produto, ProdutoExists, ProdutoNotFound))

@strawberry.type
class Query:

    @strawberry.field
    async def produtos(self) -> List[Produto]:
        async with models.get_session() as session:
            sql = select(models.Produto).order_by(models.Produto.nome)
            db_produtos = (await session.execute(sql)).scalars().unique().all()
        return [Produto.marshal(produto) for produto in db_produtos]

    @strawberry.field
    async def busca(self, query_input: Optional[ProdutoQueryInput] = None) -> List[Produto]:
        async with models.get_session() as session:
            if query_input:
                sql = select(models.Produto) \
                        .filter(models.Produto.nome.ilike(f"%{query_input.termo}%")).\
                            order_by(models.Produto.nome)
            else:
                sql = select(models.Produto).order_by(models.Produto.nome)

            db_produtos = (await session.execute(sql)).scalars().unique().all()
        return [Produto.marshal(produto) for produto in db_produtos]


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_produto(self, nome: str, preco: float, descricao: str, marca: str,
                          categoria: str) -> AddProdutoResponse:
        async with models.get_session() as session:

            sql = select(models.Produto).\
                filter(models.Produto.nome == nome).\
                    filter(models.Produto.marca == marca)
            db_produto_exists = (await session.execute(sql)).scalars().unique().all()

            if db_produto_exists:
                return ProdutoExists()

            db_produto = models.Produto(nome=nome, preco=preco, descricao=descricao,
                                        marca=marca, categoria=categoria)
            session.add(db_produto)
            await session.commit()

        return Produto.marshal(db_produto)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
