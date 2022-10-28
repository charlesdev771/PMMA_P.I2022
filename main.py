from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='templates')

conexao = 'sqlite:///meubanco.sqlite'

SQLALCHEMY_DATABASE_URI = conexao
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False





@app.route('/', methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/about', methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route('/prevention', methods=["GET","POST"])
def prevention():
    return render_template("Prevention.html")

@app.route('/causes', methods=["GET","POST"])
def causes():
    return render_template("Causes.html")

@app.route('/types', methods=["GET","POST"])
def types():
    return render_template("Types.html")

@app.route('/treatment', methods=["GET","POST"])
def treatment():
    return render_template("Treatment.html", comments=comments)
if __name__ == '__main__':
  app.run()
