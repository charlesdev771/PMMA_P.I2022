new commentfrom flask import *

app = Flask(__name__)


@app.route('/comments',methods=['GET'])
def get_comments():
    return jsonify(comments)

# Consultar(id)
@app.route('/comments/<int:id>',methods=['GET'])
def get_comments_by_id(id):
    for comment in comments:
        if comment.get('id') == id:
            return jsonify(comment)

@app.route('/comments/<int:id>',methods=['PUT'])
def edit_comments_by_id(id):
    comment_alter = request.get_json()
    for iterator,comment in enumerate(comments):
        if comment.get('id') == id:
            comments[iterator].update(comment_alter)
            return jsonify(comments[iterator])

@app.route('/comments',methods=['POST'])
def add_comment():
    new comment = request.get_json()
    comments.append(new_comment)

    return jsonify(comments)

@app.route('/comments/<int:id>',methods=['DELETE'])
def delete_comment(id):
    for iterator, comment in enumerate(comments):
        if comment.get('id') == id:
            del comments[iterator]

    return jsonify(comments)


app.run()
