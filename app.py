from flask import Flask

app = Flask("Olá")

@app.route("/")

def Ola():
    return "<p>Olá, Mundo</p>"