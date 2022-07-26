from flask import Flask, render_template

app = Flask("hello")

# Criação de rota para a aplicação - Comando route tb permite a criação de uma função (o @ é uma marcação para a rota)
@app.route("/")
def hello():
    return "Hello Word"

@app.route("/meucontato")
def meuContato():
    return  render_template('index.html')
