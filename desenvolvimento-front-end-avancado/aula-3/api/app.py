from email.mime import base
from sqlalchemy.exc import IntegrityError

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask_cors import CORS
from flask import redirect
from model import Session, Produto
from logger import logger
from schemas import *


info = Info(title="Minha querida API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")


@app.get('/')
def home():
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    session = Session()
    produto = Produto(
        nome=form.nome,
        descricao=form.descricao,
        marca=form.marca,
        valor=form.valor,
        imagem_path=form.imagem,
        categoria=form.categoria
        )
    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    try:
        # adicionando produto
        session.add(produto)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200
    except IntegrityError as e:
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar produto '{produto.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Faz a busca por um Produto a partir do id do produto

    Retorna uma representação dos produtos e comentários associados.
    """
    produto_id = query.id
    logger.debug(f"Coletando dados sobre produto #{produto_id}")
    session = Session()
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Produto econtrado: '{produto.nome}'")
        return apresenta_produto(produto), 200


@app.get('/produtos', tags=[produto_tag],
         responses={"200": ProdutoListaViewSchema, "404": ErrorSchema})
def get_produtos():
    """Lista todos os produtos cadastrados na base

    Retorna uma lista de representações de produtos.
    """
    logger.debug(f"Coletando lista de produtos")
    session = Session()
    produtos = session.query(Produto).all()
    print(produtos)
    if not produtos:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de produtos. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de produtos")
        return apresenta_lista_produto(produtos), 200


@app.delete('/produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    produto_id = query.id
    produto_nome = query.nome

    logger.debug(f"Deletando dados sobre produto #{produto_id}")
    session = Session()

    if produto_id:
        count = session.query(Produto).filter(Produto.id == produto_id).delete()
    else:
        count = session.query(Produto).filter(Produto.nome == produto_nome).delete()

    session.commit()
    if count:
        logger.debug(f"Deletado produto #{produto_id}")
        return {"mesage": "Produto removido", "id": produto_id}
    else: 
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 400

