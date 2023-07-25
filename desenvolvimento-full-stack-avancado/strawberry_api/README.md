# Minha API em GraphQL

Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Avançado** 

O objetivo aqui é apresetar uma API emplementada seguindo o padrão definido para permitir o GraphQL.

As principais tecnologias que serão utilizadas aqui é o:
 - [FastAPI](https://fastapi.tiangolo.com/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [Strawberry](https://strawberry.rocks/docs)
 - [SQLite](https://www.sqlite.org/index.html)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.


---
### Criando o Banco

A comunicação utilizando o Strawberry acontece de forma assíncrona, ao contrário do que foi feito na API REST. Com isso, a criação do banco aqui vai ser diferente.

Para criar o banco será necessário executar:

```
python creat_db.py 
```

---
### Executando o servidor

Para executar a API basta executar:

```
(env)$ uvicorn app:app --host 0.0.0.0
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ uvicorn app:app --reload --host 0.0.0.0
```

Uma vez executando o servidor, você pode acessar o painel do GraphiQL pelo link [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql ).

---
## Uso do GraphiQL

O GraphiQL é um ambiente de desenvolvimento para o GraphQL. Você não precisa instalar nada para ter acesso, ele já vem junto com o strawberry.

Nesse painel é possível fazer consultas simples aqui temos alguns exemplos.

>
> **Inserindo um novo produto**
> ```
> mutation Produto{
>   addProduto(nome: "Tênis ABC", preco: 29.99, descricao: "Um tênis confortável e estiloso", marca: "MarcaX", categoria: "Roupas"){
>     ... on Produto{
>       nome
>       marca
>       preco
>     }
>     ... on ProdutoExists{
>       message
>     }
>   }
> }
> ```
>
> **Listando produtos cadastrados**
> ```
> query {
>  produtos{
>    nome
>    marca
>    preco
>  }
>}
> ```
> A dica aqui é remover alguns dos campos e ver qual é o retorno. Por exemplo, removendo o `nome`.
>
> **Fazendo uma busca por produto que tenha o termo no nome**
> ```
> query{
>   busca(queryInput: {termo: "tênis"}){
>     nome
>     preco
>   }
> }
> ```
> A dica aqui é alterar o termo "tênis".
