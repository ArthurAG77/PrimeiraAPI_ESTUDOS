### Oque eu aprendi com isso?

app é uma instancia do flask que é a base da nossa api
Route é a rota que ele deve seguir para buscar essas informações (url) nesse caso usamos "/livros..." hosteado localmente
Methods são as ações a serem realizadas, uma rota pode executar diferentes funções a depender do metodo utilizado
json é o padrão, então para recebermos dados recebemos com get_json e para demonstrarmos usamos jsonify para transformar em json
pode executar qualquer tarefa que uma função executa, inclusive ter conexão com dbs
deve retornar algo

@app.route("/URL", methods=["METHOD"]) METHOD pode ser -> GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS

significado dos metodos :
GET -> Obtém dados do servidor (api)
POST -> Cria um novo recurso -> No exemplo um novo livro
PUT -> Atualiza um recurso inteiro "Sobrescreve" 
PATCH -> Atualiza parte de um recurso
DELETE -> Exclui um recurso
HEAD -> retorna apenas os headers sem o corpo
OPTIONS -> Retorna métodos suportados para um endpoint (url)