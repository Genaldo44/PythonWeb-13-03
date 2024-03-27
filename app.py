from flask import Flask, render_template, g
import sqlite3


app  = Flask("Olá")

app.config.from_object(__name__)

DATABASE = "banco.bd"
SECRET_KEY = "1234"

def conectar():
    return sqlite3.connect(DATABASE)

def before_request():
    g.bd =  conectar() 

def teardown_request():
    g.bd.close()

@app.route("/")
def ola():
    nomeUsuario = "Danilo"
    listaUsuario = ["Lorena", "Daniel", "Louise", "Demethrius"]
    posts = [{"titulo": "Meu titulo", "texto": "Meu texto", "data_criacao":"27/03/2024"},
             {"titulo": "Meu titulo2", "texto": "Meu texto2", "data_criacao":"26/03/2024"}]
    return render_template("hello.html", post=posts)


