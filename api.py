from flask import *

app = Flask(__name__)


@app.route('/comments',methods=['GET'])
def get_comments():
    return jsonify(comments)

# Consultar(id)
@app.route('/comments/<int:id>',methods=['GET'])
def get_comments_by_id(id):
    for livro in comments:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/comments/<int:id>',methods=['PUT'])
def edit_comments_by_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(comments):
        if livro.get('id') == id:
            comments[indice].update(livro_alterado)
            return jsonify(comments[indice])

@app.route('/comments',methods=['POST'])
def add_book():
    novo_livro = request.get_json()
    comments.append(novo_livro)

    return jsonify(comments)

@app.route('/comments/<int:id>',methods=['DELETE'])
def delete_livro(id):
    for indice, livro in enumerate(comments):
        if livro.get('id') == id:
            del comments[indice]

    return jsonify(comments)

app.run()
