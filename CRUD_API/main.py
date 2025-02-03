from flask import Flask, jsonify, request
from dataclasses import dataclass, field

id = 1

@dataclass
class fornecedor:
    id: int = field(init=False)
    razao_social: str
    cnpj: str
    categoria: str

    def __post_init__(self):
        global id
        self.id = id
        id += 1

fornecedores = []

app = Flask(__name__)

# Criar fornecedor
@app.route("/fornecedor", methods=["POST"])
def criar_fornecedor():
    data = request.get_json
    if not data:
        return jsonify({'erro':'Dados não fornecidos'})
    else:
        try:
            novo_fornecedor = fornecedor(
                data["razão social"],
                data['cnpj'],
                data['categoria']
                )
            
            fornecedores.append(
                {
                    'id' : novo_fornecedor.id,
                    'razao_social' : novo_fornecedor.razao_social,
                    'categoria' : novo_fornecedor.categoria
                }
            )

            return jsonify(fornecedores)
        except KeyError:
            return jsonify('erro':'Dados incompletos, siga a estrutura "Razão social" : str "CNPJ" : str "Categoria" : str')

# Ler lista de fornecedores
# Ler fornecedor em especifico 
# Editar fornecedor
# Editar informação de fornecedor
# Excluir fornecedor



app.run(host='localhost',port=5000,debug=True)
