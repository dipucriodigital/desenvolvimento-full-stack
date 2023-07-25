from locust import HttpUser, between, task


class LoadTest(HttpUser):
    """
    Configurando um teste de carga com o Locust
    """
    wait_time = between(1, 3)

    @task
    def add_produto(self):
        """ Fazendo a inserção de produtos aleatórios.
        """

        # criando o produto
        produto = {
            'nome': 'Camiseta',
            'categoria': 'Roupas',
            'descricao': 'Uma camiseta confortável e estilosa',
            'marca': 'MarcaX',
            'preco': '29.99'
        }
        # configurando a requisição
        headers = {'Content-Type': 'multipart/form-data'}
        response = self.client.post('produto', data=produto, headers=headers)

        # verificando a resposta
        data_response = response.json()
        if response.status_code == 200:
            print("Produto %s salvo na base" % produto["nome"])
        elif response.status_code == 409:
            print(data_response["mesage"] + produto["nome"])
        else:
            print('Falha na rota de adição de um produto')

    @task
    def listagem(self):
        """ Fazendo uma listagem dos items salvos.
        """
        # configurando a requisição
        response = self.client.get('produtos')
    
        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print('Total de items salvos: %d' % len(data["produtos"]))
        else:
            print('Falha na rota /produtos')

    @task
    def get_produto(self):
        """ Fazendo uma busca pelo produto de id 1.
        """
        # configurando a requisição
        response = self.client.get('produto?id=1')
    
        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print('Produto visitado: %s' % data["nome"])
        else:
            print('Falha na rota /produto?id=1')

    @task
    def busca_produto(self):
        """ Fazendo uma busca por produtos que no tem o termo "Camisa".
        """
        # configurando a requisição
        response = self.client.get('busca_produto?termo=Camisa')
    
        # verificando a resposta
        data = response.json()
        if response.status_code == 200:
            print('Total de produtos : %d' % len(data["produtos"]))
        else:
            print('Falha na rota /busca_produto')
