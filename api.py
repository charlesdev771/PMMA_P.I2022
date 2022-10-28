from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLAlchmy_TRACK_MODIFICATIONS'] = True
app.config['SQLAlchmy_DATABASE_URI'] = 'mysql://root:@localhost/pmma'

db = SQLAlchemy(app)

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))

    def to_json(self):
        return {'id': id, 'emai': email}

@app.route('/email', methods=['POST'])
def update(id):
    email_ob = Newsletter.query.filter(id=id).first()
    body = request.get_json()

    try:
        email_ob = body['email']
        db.session.add(email_ob)
        db.session.commit()
    except Exception as e:
        raise

@app.route('/update/<id>/')
def create_user():
    body = request.get_json()

    try:
        email = Newsletter(email=body['email'])
        db.session.add(email)
        db.session.commit()
        return generate_resp(201, 'Created', email.to_json(), 'created')
    except Exception as e:
        print(e)


@app.route('/emails/<id>', methods=['GET'])
def select_email():
    emails = Newsletter.query.filter_by(id=id).first()
    email_json = emails.to_json()
    return generate_resp(200, 'Newsletter', email_json)

def generate_resp(status, email_body, email):

    body = {}
    body[email] = email_body

    return Response(json.dumps(body, status=status, minetype='application/json'))
