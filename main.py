"""
TODO

Api - é um lugar para disponibilizar recursos e/ou funcionalidades 

# OBJETIVO - criar uma api de disponibiliza a consulta, criação, edição e exclusão dos livros
# URL Base - localhost
# Endpoints -
    - localhost/livros (GET)
    - localhost/livros (POST)
    - localhost/livros/id (GET)
    - localhost/livros/id (PUT)
    - localhost/livros/id (DELETE)
# Quais recursos - Livros

"""
from flask import Flask, jsonify, request

app = Flask(__name__) # instanciando flask

livros = [ # alguma base de dados
    {
        'id': 1,
        'titulo': "O senhor dos aneis",
        'autor': "Jubileu das neves"
    },
    {
        'id': 2,
        'titulo': 'Harry potter e a pedra filosofal',
        'autor': "J. K Rowling"
    },
    {
        'id': 3,
        'titulo': 'Animais fantasticos e onde habitam',
        'autor': 'J. K Rowlning '
    }
]

# Consultar todos
@app.route('/livros',methods=['GET']) # adiciona endpoint 
def obter_livros():
    return jsonify(livros)
# Consultar (ID)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    else:
        return "Livro não encontrado"
# Editar
@app.route("/livros/editar/<int:id>", methods=["PUT"])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get(id) == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar
@app.route("/livros", methods=["POST"])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# Excluir
@app.route("/livros/excluir/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return 

app.run(host='localhost', port=5000, debug=True) 

"""
O que aprendi com isso
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
"""