# Oque eu aprendi com isso?

App é uma instancia do flask que é a base da nossa api<br>
Route é a rota que ele deve seguir para buscar essas informações (url) nesse caso usamos "/livros..." hosteado localmente<br>
Methods são as ações a serem realizadas, uma rota pode executar diferentes funções a depender do metodo utilizado<br>
json é o padrão, então para recebermos dados recebemos com get_json e para demonstrarmos usamos jsonify para transformar em json<br>
pode executar qualquer tarefa que uma função executa, inclusive ter conexão com dbs<br>
deve retornar algo

## setando endpoint 
@app.route("/URL", methods=["METHOD"]) METHOD pode ser -> GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS

## significado dos metodos :
**GET** -> Obtém dados do servidor (api)<br>
**POST** -> Cria um novo recurso -> No exemplo um novo livro<br>
**PUT** -> Atualiza um recurso inteiro "Sobrescreve" <br>
**PATCH** -> Atualiza parte de um recurso<br>
**DELETE** -> Exclui um recurso<br>
**HEAD** -> retorna apenas os headers sem o corpo<br>
**OPTIONS** -> Retorna métodos suportados para um endpoint (url)<br>