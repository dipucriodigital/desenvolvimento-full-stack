from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List


class ProdutoSchema(BaseModel):
    nome: str = "IPhone 11"
    descricao: Optional[str] = "Na medida certa. Amplie seus horizontes com a câmera ulta-angular. "
    marca: str = "Apple"
    categoria: str = "Telefonia"
    imagem: str = "https://images-americanas.b2w.io/produtos/01/00/img/338827/0/338827081_2SZ.jpg"
    valor: float = 3599.10


class ProdutoBuscaSchema(BaseModel):
    id: Optional[int] = 1
    nome: Optional[str] = "IPhone 11"


class ProdutoViewSchema(BaseModel):
    id: int = 1
    nome: str = "IPhone 11"
    descricao: Optional[str] = "Na medida certa. Amplie seus horizontes com a câmera ulta-angular. "
    marca: str = "Apple"
    categoria: str = "Telefonia"
    imagem: str = "https://images-americanas.b2w.io/produtos/01/00/img/338827/0/338827081_2SZ.jpg"
    valor: float = 3599.10
    total_cometarios: int = 1
    nota_media: int = 0


class ProdutoDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_produto(produto):
    nota_media = 0
     
    return {
        "id": produto.id,
        "nome": produto.nome,
        "marca": produto.marca,
        "categoria": produto.categoria,
        "descricao": produto.descricao,
        "imagem": produto.imagem_path,
        "valor": float(produto.valor),
        "price": float(produto.valor),
        "nota_media": nota_media,
    }


class ProdutoListaViewSchema(BaseModel):
    produtos: List[ProdutoViewSchema]


def apresenta_lista_produto(produtos):
    result = []
    for produto in produtos:
        result.append(apresenta_produto(produto))
    return {"produtos": result}
