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
    return render_template("hello.html", nome=listaUsuario)


