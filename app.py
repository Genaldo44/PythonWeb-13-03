from flask import Flask, render_template

app  = Flask("Olá")


@app.route("/teste")

def ola():
    return render_template("hello.html")


