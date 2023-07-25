from pydantic import BaseModel
from typing import Optional, List
from models.produto import Produto


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Camiseta"
    preco: float = 29.99
    descricao: str = "Uma camiseta confortável e estilosa"
    marca: str = "MarcaX"
    categoria: str = "Roupas"


class ProdutoViewSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Camiseta"
    preco: float = 29.99
    descricao: str = "Uma camiseta confortável e estilosa"
    marca: str = "MarcaX"
    categoria: str = "Roupas"
    comentarios: List[str] = ["Só comprar se o preço realmente estiver bom!"]


class ProdutoBuscaPorNomeSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    termo: str = "Camiseta"


class ProdutoBuscaPorIDSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no ID do produto.
    """
    id: int = "1"


class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoViewSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ListagemProdutosSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "preco": produto.preco,
            "descricao": produto.descricao,
            "marca": produto.marca,
            "categoria": produto.categoria,
            "comentarios": [c.texto for c in produto.comentarios]
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Camiseta"
    preco: float = 29.99
    descricao: str = "Uma camiseta confortável e estilosa"
    marca: str = "MarcaX"
    categoria: str = "Roupas"
    total_cometarios: int = 1
    comentarios:List[str] = ["Só comprar se o preço realmente estiver bom!"]


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    id: int


def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "preco": produto.preco,
        "descricao": produto.descricao,
        "marca": produto.marca,
        "categoria": produto.categoria,
        "total_cometarios": len(produto.comentarios),
        "comentarios": [c.texto for c in produto.comentarios]
    }
